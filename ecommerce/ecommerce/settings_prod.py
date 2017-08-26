import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DEBUG = False

TEMPLATE_DEBUG = False

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

print "-=-=--=- using prod settings"


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
#MEDIA_ROOT = '/Users/jmitch/Desktop/ecommerce/static/media/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static_root")

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "static_files"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', '')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', '')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME', '')

AWS_ACCESS_KEY_ID = 'AKIAJMCSWCDLXQ32QZGQ'
AWS_SECRET_ACCESS_KEY = 'zz03XTDELiu0ItloJDkfC7JL6eegCzUqsC/sZL+p'
AWS_STORAGE_BUCKET_NAME = 'omos'

# This will make sure that the file URL does not have unnecessary parameters like your access key.
AWS_QUERYSTRING_AUTH = False 
# AWS_S3_CUSTOM_DOMAIN = AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com'
#static media settings
# STATIC_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
aws_string = 'https://s3.ap-south-1.amazonaws.com/' + AWS_STORAGE_BUCKET_NAME 

STATIC_URL = aws_string + '/static/'
MEDIA_URL = aws_string + '/'

# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
    )