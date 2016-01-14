import os
import sys
import dj_database_url
from django.core.mail import send_mail

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')

DEBUG = False

ALLOWED_HOSTS = ['valeez.herokuapp.com', 'valeez.com']

SITE_ID = 2
# Application definition

INSTALLED_APPS = (
    'valeezapp',
    'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites.models',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'valeez.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'valeez.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'valeezdb2',
    }
}


LANGUAGE_CODE = 'en-US'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# these are for heroku deployment
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../valeezapp/static'),
)
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# registration redux
REGISTRATION_OPEN = True
ACCOUNT_ACTIVATION_DAYS = 3
REGISTRATION_AUTO_LOGIN = True
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'accounts/login/'

# email login// adding in sendgrid
EMAIL_HOST='smtp.sendgrid.net'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEFAULT_FROM_EMAIL = os.environ.get('APP_EMAIL')
EMAIL_HOST_USER = 'SENDGRID_USERNAME'
EMAIL_HOST_PASSWORD = 'SENDGRID_PASSWORD'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
#TO DO fix this line
send_mail('../valeezapp/templates/registration/activation_email_subject.txt', '../valeezapp/templates/registration/activation_email_subject.txt', os.environ.get('APP_EMAIL'), [''], fail_silently=False)

LOGIN_REDIRECT_URL = "home"

# #Postgres for heroku
# # Parse database configuration from $DATABASE_URL
DATABASES['default'] =  dj_database_url.config()
# Enable Persistent Connections
DATABASES['default']['CONN_MAX_AGE'] = 500
# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
