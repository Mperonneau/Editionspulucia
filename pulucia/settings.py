"""
Django settings for pulucia project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import os.path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '05yt^+j8snkvtutmmc=ox)v&2_qk(%7pv)-@3%o5ntz5^tfvp8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['pulucia.herokuapp.com',  'www.editionspulucia.com'] #192.168.1.5: test the web on phone....


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'pwa',
    "sslserver",
    'social_django',
    'django_filters',
    'mathfilters', # pip install django-mathfilters: to do calcul in django template
    'pulucia_web',  
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

#redirect the app to HTTPS after configuring a SSL certificate (to add only in production not in developpement)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True


#---------------------------------------------------------------------------
#social_app/settings.py


SESSION_COOKIE_SAMESITE = None
#add this
AUTHENTICATION_BACKENDS = [
    'social_core.backends.facebook.FacebookOAuth2',
     'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
  
    
]

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'redirect'


# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '3839180016106466'       # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '8542da8d2b513d6f77b002bb122beae5'  # App Secret

# in way to get more infos from the account facebook user's
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'public_profile'] # add this 
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       # add this
  'fields': 'id, name, email'
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                 # add this
    ('name', 'name'),
    ('email', 'email'),
]

#Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '706304577978-262rf4meke4nb3a06efn12lrhmv55vco.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'xSEeoD1HQYXXFKoIzJHACmap'


SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile'
]




#----------------------------------------------------------------------------

ROOT_URLCONF = 'pulucia.urls'

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
                'social_django.context_processors.backends', # add this # login social media account
                'social_django.context_processors.login_redirect', # add this #login with social media account
            ],
        },
    },
]

WSGI_APPLICATION = 'pulucia.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS = (
     os.path.join(BASE_DIR, 'static'),
)





MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'






EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_USE_TLS = True
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'peronneaumoliere@gmail.com'
#EMAIL_HOST_PASSWORD = 'ppcjvfnnnrohfngc'


#configuration for sendgrid!
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = "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" # the code generate when create the api key
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# paypal payment 
PAYPAL_CLIENT_ID  = "AWrTS0pPlZm2-lgpyS346AhjMRWmu1A8Q50ndMPU8JHSoXNGxU43L_490RYHNuBHXkB7H0l1QODgiDoH"
PAYPAL_SECRET_ID  =  "ELKsvy7D4FWhCyZcW9IyDBEo_JEsmLokiTtUbcrXi7mbqSfqStj4LqG0hT7dK4N0ChfT_g15XADEejO-"


#progressive web app configuration
PWA_APP_NAME = 'Pulucia'
PWA_APP_DESCRIPTION = "Pulucia PWA"
PWA_APP_THEME_COLOR = '#000000'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': 'static/img/pulucia-pwa.png',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': 'static/img/pulucia-pwa.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': 'static/img/logo_pulucia.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'
