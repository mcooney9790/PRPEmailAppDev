from django.shortcuts import render_to_response
from django.template import RequestContext
from templatecreator.models import EmailTemplate
from emaillistcreator.forms import ImportListForm
from emaillistcreator.forms import ImportAttachmentForm
from django_project.settings import MEDIA_ROOT
from templatecreator.forms import EmailTemplateForm
import os

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

        email_list_form = ImportListForm()
        attachment_form = ImportAttachmentForm()

        return render_to_response('UploadEmailList.html',{'email_list_form':email_list_form, 'attachment_form':attachment_form}, context_instance=RequestContext(request))

    elif i == 3:
        # List the options for email templates
        list = EmailTemplate.objects.values_list('name')

        # Append them to a list
        template_list = []
        for item in list:
            template_list.append(str(item[0]))

        #====
        # Build contact csv list
        #====
        # Create lists
        list_loop = os.listdir(os.path.join(MEDIA_ROOT,'contactlists'))
        csv_list = []
        for file in list_loop:
            if file[-4:] == '.csv':
                csv_list.append(file)
            else:
                pass
        # ====
        # Build attachment list
        # ====

        att_loop = os.listdir(os.path.join(MEDIA_ROOT,'email_attachments'))
        attachment_list = []
        for file in att_loop:
            if file == "":
                pass
            else:
                attachment_list.append(file)


        # data sent to browser
        j = {}
        j['email_templates'] = template_list
        j['email_lists'] =  csv_list
        j['attachments'] = attachment_list

        return render_to_response('SendEmail.html', j , context_instance=RequestContext(request))
