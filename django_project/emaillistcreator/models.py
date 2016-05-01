from __future__ import unicode_literals
from django.db import models
from django.core.files.storage import FileSystemStorage


# Create your models here.
AWS_STORAGE_BUCKET_NAME = 'emailappstatic'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
MEDIA_URL = "https://%s/media/" % AWS_S3_CUSTOM_DOMAIN
contact_list_folder = "contactlists/"

att_fs = FileSystemStorage(location='/home/')

class ContactFile(models.Model):

    docfile = models.FileField(upload_to='contactlists')

class Attachment(models.Model):

    docfile = models.FileField(upload_to='email_attachments')