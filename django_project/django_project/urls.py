from django.conf.urls import patterns, include, url
from templates.views import homepage
from templatecreator.views import create_new_temp
from templates.views import load_create_template
from sendmail.views import load_template_to_page
from sendmail.views import preview_list
from sendmail.views import send_email_blast
from emaillistcreator.views import upload_list
from emaillistcreator.views import upload_attachment
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

# Examples:
# url(r'^$', 'django_project.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', homepage),
    url(r'^admin/', admin.site.urls),
    url(r'^show-template/', load_template_to_page),
    url(r'^upload-list-file/', upload_list),
    url(r'^upload-attachment/', upload_attachment),

    url(r'^previewlist', preview_list),
    url(r'^load-create-template/', load_create_template),
    url(r'^email-blast/', send_email_blast),
    url(r'^create-new-template/', create_new_temp, name='make-new-temp'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)