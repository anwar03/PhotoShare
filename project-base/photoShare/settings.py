"""
Django settings for photoShare project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The root of the git repo - Could be ~/project or ~/repo
REPO_DIR = os.path.realpath(os.path.join(BASE_DIR, '..'))
# The directory of the current user ie /home/django a.k.a. ~
HOME_DIR = os.path.realpath(os.path.join(REPO_DIR, '..'))
# The directory where collectstatic command copies/symlinks the files to
# This can/should be located at ~/staticfiles, preferrably outside the git repo
STATIC_DIR = os.path.realpath(os.path.join(HOME_DIR, 'staticfiles'))
# The directory where different applications uploads media files to
# This can/should be located at ~/media, preferrably outside the git repo
MEDIA_DIR = os.path.realpath(os.path.join(REPO_DIR, 'media'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_&ard99n^kdawrw_aing7ub@4p+qaepmvwo%$bmu!7^p6rdh!g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'widget_tweaks',
    'publisher',
    'album',
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'photoShare.urls'

WSGI_APPLICATION = 'photoShare.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'PhotoShare',
        'USER': 'photoshare',
        'PASSWORD': 'asdf1234',
        'HOST': 'localhost',
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(REPO_DIR, 'static'),
]


LOGIN_URL = '/login/'
LOGOUT_REDIRECT_URL = 'login'
LOGIN_REDIRECT_URL = 'home'

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = '/media/'
