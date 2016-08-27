from django.http import JsonResponse
from templatecreator.models import EmailTemplate
from django_project.settings import MEDIA_ROOT
from modules.buildEmail import queryForTemplate
from modules.buildEmail import send_gmail
from modules.buildEmail import build_message
from modules.buildEmail import replace_html
from modules.buildEmail import attach_files
from userprofile.models import Profile
import os
import time
import pandas as pd
import sys
# ===============
# Javascript sent request to GET different email templates
# ===============

def load_template_to_page(request):

    if request.method == 'GET':

        # Get request variable from JSON
        email_template_name = request.GET['temp']

        # Query EmailTemplate object
        template_object = queryForTemplate(email_template_name)

        # Get Subject and Body
        body = template_object.get_body()
        subject = template_object.get_subject()

        # Formulate Json
        j = {'subject':subject,'body':body}

        # Send Email Template back to Javascript
        return JsonResponse(j)

# ===============
# Preview CSV List in browser
# ===============

def preview_list(request):

    if request.method == 'GET':

        # Get filename
        file = request.GET['filename']

        # Build bucket url
        folder = 'contactlists'
        fp = os.path.join(MEDIA_ROOT,folder,file)

        # Create Dataframe with contact list data and a preview snippet of the table
        df = pd.read_csv(fp)
        df.columns = [x.lower() for x in df.columns]

        cols = ['brand','contact','e-mail']

        if all((col in df.columns for col in cols)):

            preview = df.head()
            preview_html = preview.to_html(index=False)

            j = {'preview_list': preview_html}

            return JsonResponse(j)

        else:

            j = {'preview_list' : 'Either the "brand","contact", or "e-mail" fields are not in your contact list'}

            return JsonResponse(j)


# ===============
# Send Blast
# ===============

def send_email_blast(request):

    # S3 connections

    if request.method == 'GET':
        try:
            # Get variables from request

            file = request.GET['email_list']
            google_prof = request.GET['google_user']
            email_template = request.GET['email_template']
            
            try:
                attachments = request.GET['att_str'].split("*JOINTO*")
            except:
                attachments = []

            # Get list

            folder = 'contactlists'
            fp = os.path.join(MEDIA_ROOT,folder,file)
            df = pd.read_csv(fp)
            
            # Get template
            # Query EmailTemplate object
            template_object = queryForTemplate(email_template)

            # Get Subject, Body, and Signature as well as GMail password
            body = template_object.get_body()
            subject = template_object.get_subject()
            google_prof_pw = str(Profile.objects.filter(google_username = google_prof).values()[0]['google_password'])
            signature = str(Profile.objects.filter(google_username = google_prof).values()[0]['signature'])
            
            # Attachments path
            attach_path = os.path.join(MEDIA_ROOT,'email_attachments')

            # Store list variables in DataFrame
            # objects to be iterated through

            df.columns = [x.lower() for x in df.columns]

            name_series = df['contact']
            email_series = df['e-mail']
            brand_series = df['brand']

            i = 0
            error_list = []
            sent_dict = {}

            while i < len(df):
                try:
                    # Get necessary information and credentials for email

                    if '@' in google_prof:
                        myemail = google_prof
                    else:
                        myemail = google_prof + '@gmail.com'
                    email_subject = replace_html(brand_series[i],name_series[i], subject)
                    email_body = replace_html(brand_series[i], name_series[i], body)

                    # Formulate message
                    
                    msg_content = build_message(email_series[i],myemail,email_subject,email_body, signature)

                    # Attach files
                    
                    msg = attach_files(attach_path ,msg_content,attachments)
                    send_gmail(msg,google_prof,google_prof_pw,myemail, email_series[i])
                    time.sleep(3)
                    sent_dict[i] = 'Email sent to {}' .format(email_series[i])

                except Exception as e:

                    time.sleep(3)
                    sent_dict[i] = "Email not sent to {} because of {}." .format(email_series[i],e)
                    error_list.append(e)

                i += 1

            return JsonResponse(sent_dict)

        except:
            error = "{}" .format(sys.exc_info()[0])
            return JsonResponse({'fail': error })