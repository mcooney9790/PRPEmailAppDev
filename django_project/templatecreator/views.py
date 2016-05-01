from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import JsonResponse
from modules.buildEmail import build_message, send_gmail
from .models import EmailTemplate
from .forms import EmailTemplateForm
# Create your views here.

# ===================
# Create a new template
# ===================

def create_new_temp(request):
    if request.method == 'POST':

        form = EmailTemplateForm(request.POST)

        if form.is_valid():

            form.save()

            new_temp_name = request.POST['name']

            result = "successful"

            j = {'result': result, 'new_temp_name': new_temp_name}

            return render_to_response('formcompletion/template_made.html',j,context_instance=RequestContext(request))
