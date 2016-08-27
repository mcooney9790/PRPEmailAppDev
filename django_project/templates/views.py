from django.shortcuts import render_to_response
from django.template import RequestContext
from templatecreator.models import EmailTemplate
from userprofile.models import Profile
from templatecreator.forms import EmailTemplateForm
from modules.app_functions import create_csv_list
from modules.app_functions import create_attachment_list
from modules.app_functions import upload_page_dict

def homepage(request):

    return render_to_response("index.html")

def load_create_template(request, i = 0):

    if request.method == 'GET':
        i = int(request.GET['button'])
    else:
        pass

    if i == 1:
        form = EmailTemplateForm()

        return render_to_response('CreateTemplate.html', {'form':form},context_instance=RequestContext(request))

    elif i == 2:

        j = upload_page_dict('')

        return render_to_response('UploadEmailList.html', j, context_instance=RequestContext(request))

    elif i == 3:
        # List the options for email templates
        list = EmailTemplate.objects.values_list('name')

        # Append them to a list
        template_list = []
        for item in list:
            template_list.append(str(item[0]))
       
        # List the options for uploaded CSVs
        csv_list = create_csv_list('contactlists')
        
        # List the options for uploaded email attachments
        attachment_list = create_attachment_list('email_attachments')
        
            
        # List gmail usernames (profiles) to send the the email blast from 
        username_list = []
        google_usernames = Profile.objects.all().values_list('google_username')
        for user in google_usernames:
            username_list.append(str(user[0]))        # data sent to browser
        j = {}
        j['email_templates'] = template_list
        j['email_lists'] =  csv_list
        j['attachments'] = attachment_list
        j['usernames'] = username_list 

        return render_to_response('SendEmail.html', j , context_instance=RequestContext(request))

    elif i == 4:

        return render_to_response('HowTo.html', context_instance=RequestContext(request))
    
    elif i == 5:

        list = Profile.objects.all()
        
        users = []
        pwords = []
        signatures = []
        for item in list:
            users.append(str(item.google_username))
        
        for item in list:
            pwords.append(str(item.google_password))
        
        for item in list:
            signatures.append(str(item.signature))
            
        j = {}
        
        finallist = zip(users,pwords,signatures)
        
        j['finallist'] = finallist

        return render_to_response('UserProfile.html', j ,context_instance=RequestContext(request))
        