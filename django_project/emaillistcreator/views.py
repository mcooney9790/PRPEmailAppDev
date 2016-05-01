from django.shortcuts import render_to_response, redirect
from django.http import JsonResponse
from django.core.files.base import ContentFile
from django.template import RequestContext
from .forms import ImportListForm
from .forms import ImportAttachmentForm
from .models import ContactFile
from .models import Attachment

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

    j = {
        'confirm':confirm
    }

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

