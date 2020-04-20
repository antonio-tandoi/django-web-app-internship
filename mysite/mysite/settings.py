import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')48194p#1joh#_dgm8!0n8p^88br(@ki!bk53bgmapg!t-&ygo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'adminactions',
    #'django.contrib.admin',
    'maintenance_mode',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'material.admin',
    'material.admin.default',
    'attack.apps.AttackConfig',
    'django_csv_exports',
    #'social_django',
    'autocompletefilter',
    'sortedm2m',
    #'exportdb',
    #'extra_settings',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'maintenance_mode.middleware.MaintenanceModeMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'maintenance_mode.context_processors.maintenance_mode',
               
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'threat_set',
        'USER': 'threatUser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',   },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'it'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'statics'),
   ]

AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


MATERIAL_ADMIN_SITE = {
    'FAVICON':  'attack/favicon2.png', 
    #'MAIN_BG_COLOR':  'blue',  
    #'MAIN_HOVER_COLOR':  'white',
    'PROFILE_PICTURE':  'attack/admin.png',
    #'PROFILE_BG':  'attack/adminbg.jpg', 
    'LOGIN_LOGO':  'attack/login_logo.png',
    #'LOGOUT_BG':  'path/to/image',  
    'SHOW_THEMES':  True,
    #'TRAY_REVERSE': False,  # Hide object-tools and additional-submit-line by default
    'NAVBAR_REVERSE': True,
    'SHOW_COUNTS': True, 
}

#######################################################################################

# if True the maintenance-mode will be activated
MAINTENANCE_MODE = None
MAINTENANCE_MODE_STATE_FILE_PATH = 'maintenance_mode_state.txt'
MAINTENANCE_MODE_IGNORE_ADMIN_SITE = True
MAINTENANCE_MODE_IGNORE_ANONYMOUS_USER = False
MAINTENANCE_MODE_IGNORE_AUTHENTICATED_USER = False
MAINTENANCE_MODE_IGNORE_STAFF = False
MAINTENANCE_MODE_IGNORE_SUPERUSER = True

# list of ip-addresses that will not be affected by the maintenance-mode
# ip-addresses will be used to compile regular expressions objects
MAINTENANCE_MODE_IGNORE_IP_ADDRESSES = ()

#######################################################################################

# EXPORT_CONF = {
#     'models': {
#         'auth.User': {
#             'fields': ('username',),
#             'resource_class': 'app.tests.utils.UserResource'
#         },
#         'auth.Group': {
#             'resource_class': 'app.tests.utils.GroupResource'
#         },
#         'auth.Permission': {
#             'fields': ('name',)
#         }
#     }
# }

#######################################################################################

# if True the template tag will fallback to django.conf.settings,
# very useful to retrieve conf settings such as DEBUG.
EXTRA_SETTINGS_FALLBACK_TO_CONF_SETTINGS = True

# the upload_to path value of settings of type 'file'
EXTRA_SETTINGS_FILE_UPLOAD_TO = 'files'

# the upload_to path value of settings of type 'image'
EXTRA_SETTINGS_IMAGE_UPLOAD_TO = 'images'

