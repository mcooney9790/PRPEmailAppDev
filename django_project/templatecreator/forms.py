from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import EmailTemplate


class EmailTemplateForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = EmailTemplate
        fields = ('body','subject','name',)