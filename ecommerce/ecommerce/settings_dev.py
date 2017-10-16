
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ["*"]

# DEFAULT_FROM_EMAIL = "OmoAds <theomoads@gmail.com>"
# SITE_URL = "http://omoads.com"

print ("-=-=-=-= using dev settings")

# URL to reference the static files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")

# where to store static files after collectstatic
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static_root")


STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "static_files"),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)
