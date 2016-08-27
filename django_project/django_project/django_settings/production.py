from base import *

# AWS s3 credentials
AWS_STORAGE_BUCKET_NAME = 'emailappstatic'
AWS_ACCESS_KEY_ID = 'AKIAJDLOTJODJELSS5LA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# For 'ckeditor' package
AWS_QUERYSTRING_AUTH = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': '37BOdHrTzn',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = "http://%s/" % AWS_S3_CUSTOM_DOMAIN

STATIC_URL = "http://%s/" % AWS_S3_CUSTOM_DOMAIN

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_in_pro", "our_static"),
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MEDIA_ROOT = os.path.join(PROJECT_ROOT,'media')

MEDIA_URL = '/media/'