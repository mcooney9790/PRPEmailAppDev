import os
from django_project.settings import MEDIA_ROOT
from emaillistcreator.forms import ImportListForm
from emaillistcreator.forms import ImportAttachmentForm
# ====
# Build file list from directory
# ====
def create_csv_list(folder):
    list_loop = os.listdir(os.path.join(MEDIA_ROOT, folder))
    file_list = []
    for file in list_loop:
        if file[-4:] == '.csv':
            file_list.append(file)
        else:
            pass
    return file_list

# ====
# Build attachment list
# ====
def create_attachment_list(dir):
    att_loop = os.listdir(os.path.join(MEDIA_ROOT,dir))
    attachment_list = []
    for file in att_loop:
        if file == "":
            pass
        else:
            attachment_list.append(file)
    return attachment_list


def upload_page_dict(confirm):
    email_list_form = ImportListForm()
    attachment_form = ImportAttachmentForm()
    csv_list = create_csv_list('contactlists')
    attachment_list = create_attachment_list('email_attachments')
    j = {
        'email_list_form': email_list_form,
        'attachment_form': attachment_form,
        'attachments': attachment_list,
        'email_lists': csv_list,
        'confirm': confirm,
    }

    return j