from django import forms

class ImportListForm(forms.Form):

    docfile = forms.FileField(

        label='Upload an email list here'

    )

class ImportAttachmentForm(forms.Form):

    docfile = forms.FileField(

        label='Upload an attachment here'

    )