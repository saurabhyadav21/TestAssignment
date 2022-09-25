import os
from re import T
import warnings
from django.utils.translation import gettext_lazy as _
from os.path import dirname

warnings.simplefilter('error', DeprecationWarning)

SECRET_KEY = 'NhfTvayqggTBPswCXXhWaN69HuglgZIkM'

DEBUG = True
ALLOWED_HOSTS = []

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # Vendor apps
    'bootstrap4',

    # Application apps
    'main',
    'accounts',
    'book',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join('content', 'templates'),
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

WSGI_APPLICATION = 'app.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'DB_NAME',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ENABLE_USER_ACTIVATION = False
LOGIN_VIA_EMAIL = True
LOGIN_VIA_EMAIL_OR_USERNAME = True
LOGIN_REDIRECT_URL = 'index'
LOGIN_URL = 'accounts:log_in'
USE_REMEMBER_ME = False

RESTORE_PASSWORD_VIA_EMAIL_OR_USERNAME = False
ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE = True

SIGN_UP_FIELDS = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', _('English')),
    ('ru', _('Russian')),
    ('zh-Hans', _('Simplified Chinese')),
    ('fr', _('French')),
    ('es', _('Spanish')),
]

TIME_ZONE = 'UTC'
USE_TZ = True

STATIC_ROOT = os.path.join('content', 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join('content', 'media')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join('content', 'assets'),
]

LOCALE_PATHS = [
    os.path.join('content', 'locale')
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
