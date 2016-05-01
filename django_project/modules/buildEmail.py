__author__ = 'mcooney9790'

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from templatecreator.models import EmailTemplate
import os
import urllib2

class queryForTemplate:

    def __init__(self,name):

        self.name = name

    def get_body(self):

        body_object = EmailTemplate.objects.filter(name=self.name)
        body = body_object.values_list('body')[0][0]

        return body

    def get_subject(self):

        subject_object = EmailTemplate.objects.filter(name=self.name)
        subject = subject_object.values_list('subject')[0][0]

        return subject

def replace_html(brand, name ,html):

    html_str = html.replace('xxxxBRANDxxxx',brand).replace('xxxxCONTACTxxxx',name)

    return html_str

def attach_files(basepath,msg,files=[]):

    for f in files or []:
        path = os.path.join(basepath,f)
        with open(path,'rb') as fil:
            msg.attach(MIMEApplication(
                fil.read(),
                Content_Disposition='attachment; filename="{}"' .format(os.path.basename(f)),
                Name=os.path.basename(f)
            ))

    return msg

def build_message(toaddress,fromaddress,subject,body):

    msg = MIMEMultipart('alternative')
    msg['To'] = toaddress
    msg['From'] = fromaddress
    msg['Subject'] = subject
    b = u"{}" .format(body)
    content = MIMEText(b.encode('utf-8') ,'html','UTF-8')

    msg.attach(content)

    return msg


def send_gmail(msg,username,password,fromaddress,toaddress):

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddress, toaddress , msg.as_string())
    server.quit()