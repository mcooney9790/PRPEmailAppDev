from __future__ import unicode_literals
from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.
class EmailTemplate(models.Model):

    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=500)
    body = RichTextField()

    def __unicode__(self):  # __unicode__ on Python 2

        return self.body