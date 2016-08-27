from django.shortcuts import render_to_response, redirect
from django.http import JsonResponse
from django.core.files.base import ContentFile
from django.template import RequestContext
from .forms import ImportListForm
from .forms import ImportAttachmentForm
from .models import ContactFile
from .models import Attachment
from django_project.settings import MEDIA_ROOT
from modules.app_functions import upload_page_dict
import os

# Create your views here.

def upload_attachment(request):
    try:
        if request.method == 'POST':
            form = ImportAttachmentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Attachment(docfile=request.FILES['docfile'])
                newdoc.save()
            confirm = "File saved."
    except:
            confirm = "File not saved."

    j = {'confirm':confirm}

    return render_to_response('formcompletion/file_uploaded.html',j,context_instance=RequestContext(request))


def upload_list(request):
    try:
        if request.method == 'POST':
            form = ImportListForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = ContactFile(docfile=request.FILES['docfile'])
                newdoc.save()
            confirm = "File saved."
    except:
            confirm = "File not saved."

    j = {'confirm':confirm}

    return render_to_response('formcompletion/file_uploaded.html',j,context_instance=RequestContext(request))

def delete_attachment(request):

    if request.method == 'GET':
        file = request.GET['file']
        path = os.path.join(MEDIA_ROOT, 'email_attachments', file)
        os.remove(path)
        confirm = "File {} deleted." .format(file)
        j = upload_page_dict(confirm)

        return render_to_response('UploadEmailList.html', j, context_instance=RequestContext(request))

def delete_contact_list(request):

    if request.method == 'GET':
        file = request.GET['file']
        path = os.path.join(MEDIA_ROOT, 'contactlists', file)
        os.remove(path)
        confirm = "File {} deleted.".format(file)
        j = upload_page_dict(confirm)

        return render_to_response('UploadEmailList.html', j, context_instance=RequestContext(request))
