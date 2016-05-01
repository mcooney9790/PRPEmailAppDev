
# Create your tests here.
from django.http import JsonResponse
from templatecreator.models import EmailTemplate
from django_project.settings import AWS_S3_CUSTOM_DOMAIN
from modules.buildEmail import queryForTemplate
from modules.buildEmail import send_gmail
from modules.buildEmail import build_message
from modules.buildEmail import replace_html
import time
import pandas as pd

try:
    # Get variables from request
    file = 'testlist.csv'
    email_template = 'Grassroots'

    # ===============
    # Get list
    # ===============

    bucket = 'contactlists'
    url = "http://{}/{}/{}".format(AWS_S3_CUSTOM_DOMAIN, bucket, file)

    df = pd.read_csv(url)

    # ===============
    # Get template
    # ===============

    # Query EmailTemplate object
    template_object = queryForTemplate(email_template)

    # Get Subject and Body
    body = template_object.get_body()
    subject = template_object.get_subject()

    name_series = df['Name']
    email_series = df['E-Mail']
    brand_series = df['Brand']

    i = 0
    error_list = []
    sent_dict = {}
    while i < len(df):
        try:
            myemail = 'mcooney9790@gmail.com'
            subject = replace_html(brand_series[i], name_series[i], subject)
            body = replace_html(brand_series[i], name_series[i], body)
            msg = build_message(email_series[i], myemail, subject, body)
            send_gmail(msg, 'mcooney9790', 'coleman1223', myemail, email_series[i])

            time.sleep(3)

            sent_dict[i] = 'Email sent to {}'.format(email_series[i])

            i += 1

        except Exception as e:

            print 'error'

except:
    print 'fao;'