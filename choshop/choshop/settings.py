"""
Django settings for choshop project.

Generated by 'django-admin startproject' using Django 2.2.17.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ciz7i&_!17%!c7v1%#1mtqlafk2wj@(di*+-m7(o@t@d86zqvm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.gis',
    # Outdoor apps 
    'rest_framework', # user Visits 
    'user_visit',
    # Graphene 
    'graphene_django',
    # Forms
    'ckeditor',
    'ckeditor_uploader',
    'webpack_loader',
    # Our apps 
    'account.apps.AccountConfig',
    'blog.apps.BlogConfig',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'markers.apps.MarkersConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'choshop.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'choshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
'''
# We need to install the SQLite spatial extension SpatiaLite:

# on Debian-based GNU/Linux distributions (es: Debian, Ubuntu, ???): 
###### apt install libsqlite3-mod-spatialite

# ADD THIS INSTEAD 
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.spatialite",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
'''


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(str(BASE_DIR), "staticfiles")
]

STATIC_ROOT =  f"{BASE_DIR}/cdn_test/static" # AWS S3 + Cloudfront, Google Cloud Storage, django-storages

MEDIA_URL = "/media/"
# any file field upload by default
MEDIA_ROOT =  f"{BASE_DIR}/cdn_test/media"

PROTECTED_MEDIA =  f"{BASE_DIR}/cdn_test/protected"

############## LOGGING 
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'blog': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'shop': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'account': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'markers': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'account': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'orders': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'cart': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },

    },
}


# USER MODEL 
AUTH_USER_MODEL = 'account.Account'

# URL 
ALLOW_UNICODE_SLUGS = True


### CK EDITOR 
CKEDITOR_UPLOAD_PATH = 'media/ckeditor/'


## SESSION STUFF 
# add this later in production 
SESSION_COOKIE_DOMAIN = None 
SESSION_COOKIE_SECURE = True 
SESSION_EXPIRE_AT_BROWSER_CLOSE =False
CART_SESSION_ID = 'cart'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES' : (
        'rest_framework.authentication.SessionAuthentication', 

    ), 
    'DEFAULT_PERMISSION_CLASSES' : (
        'rest_framework.permissons.IsAuthenticatedOrReadOnly',
    ),
}

LOGIN_REDIRECT_URL = 'shop:list'
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_email')


# REACT SETTING 

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}



# GRAPHQL 

GRAPHENE = {
    'SCHEMA': 'choshop.schema.schema',
    'MIDDLEWARE': [
        'graphql_jwt.middleware.JSONWebTokenMiddleware',
    ],

}



# DRF #
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}