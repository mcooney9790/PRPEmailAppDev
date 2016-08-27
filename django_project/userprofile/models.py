from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
class Profile(models.Model):

    google_username = models.CharField(max_length=100,primary_key=True)
    google_password = models.CharField(max_length=100)
    signature = RichTextField()
    
    def __unicode__(self):  # __unicode__ on Python 2
        return self.google_username

# Create your models here.
