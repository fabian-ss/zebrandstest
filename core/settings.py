import os
from pathlib import Path
from decouple import config
from datetime import timedelta

BASE_DIR = Path(__file__).resolve().parent.parent

try:
    SECRET_KEY = config("SECRET_KEY")
except KeyError as e:
    raise RuntimeError("Could not find a SECRET_KEY in environment")

try:
    DEBUG = config("DEBUG")
except KeyError as e:
    raise RuntimeError("Could not find a DEBUG in environment")

# Variables for the db
try:
    DB_ENGINE = config("DB_ENGINE")
except KeyError as e:
    raise RuntimeError("Could not find a DB_ENGINE in environment")

try:
    SQL_NAME = config("SQL_NAME")
except KeyError as e:
    raise RuntimeError("Could not find a SQL_NAME in environment")


# Variables for the email services
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True

try:
    EMAIL_HOST = config("EMAIL_HOST")
except KeyError as e:
    raise RuntimeError("Could not find a EMAIL_HOST in environment")
try:
    EMAIL_HOST_USER = config("EMAIL_HOST_USER")
except KeyError as e:
    raise RuntimeError("Could not find a EMAIL_HOST_USER in environment")
try:
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
except KeyError as e:
    raise RuntimeError("Could not find a EMAIL_HOST_PASSWORD in environment")


ALLOWED_HOSTS = []

# CSRF_ORIGIN_WHITELIST = config("CSRF_ORIGIN_WHITELIST_DEV")
# CSRF_TRUSTED_ORIGIN = config("CSRF_TRUSTED_ORIGIN_DEV")

# LOGGIN = {
#     'version':1,
#     'disable_existing_loggers':False,
#     'handlers': {
#         'console': {
#             'class': 'loggin.StreamHanlder',
#         },
#     },
#     'loggers':{
#         'django': {
#             'handlers': ['console'],
#             'level': 'DEBUD',
#         }
#     }
# }
 
SITE_ID=1

# Application definition
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_APPS = [
    'apps.products',
    'apps.users',
]

THIRD_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'coreapi',
]

INSTALLED_APPS = DJANGO_APPS + MY_APPS + THIRD_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',    
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'NAME': BASE_DIR / SQL_NAME,
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = []
    
AUTH_USER_MODEL = 'users.User'

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    'DEFAULT_PERMISSIONS_CLASSES':[
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",
}