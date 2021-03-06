from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

def gettext(s): return s


DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for the_irene_blog project.

Generated by 'django-admin startproject' using Django 3.1.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '7@da5_te8xtuybrs=9sxs54m+s1^7br!$6an9pzp2#0r-1+a_9'
DEBUG = True
ALLOWED_HOSTS = []
ROOT_URLCONF = 'the_irene_blog.urls'
WSGI_APPLICATION = 'the_irene_blog.wsgi.application'
AUTH_PASSWORD_VALIDATORS = [{'NAME':
                             'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
                             }, {'NAME':
                                 'django.contrib.auth.password_validation.MinimumLengthValidator'}, {
    'NAME':
    'django.contrib.auth.password_validation.CommonPasswordValidator'}, {
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Atlantic/Reykjavik'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')
STATICFILES_DIRS = os.path.join(BASE_DIR, 'the_irene_blog', 'static'),
SITE_ID = 1
TEMPLATES = [{'BACKEND': 'django.template.backends.django.DjangoTemplates',
              'DIRS': [os.path.join(BASE_DIR, 'the_irene_blog', 'templates')],
              'OPTIONS': {'context_processors': [
                  'django.contrib.auth.context_processors.auth',
                  'django.contrib.messages.context_processors.messages',
                  'django.template.context_processors.i18n',
                  'django.template.context_processors.debug',
                  'django.template.context_processors.request',
                  'django.template.context_processors.media',
                  'django.template.context_processors.csrf',
                  'django.template.context_processors.tz',
                  'sekizai.context_processors.sekizai',
                  'django.template.context_processors.static',
                  'cms.context_processors.cms_settings'], 'loaders': [
                  'django.template.loaders.filesystem.Loader',
                  'django.template.loaders.app_directories.Loader']}}]
MIDDLEWARE = ['cms.middleware.utils.ApphookReloadMiddleware',
              'django.contrib.sessions.middleware.SessionMiddleware',
              'django.middleware.csrf.CsrfViewMiddleware',
              'django.contrib.auth.middleware.AuthenticationMiddleware',
              'django.contrib.messages.middleware.MessageMiddleware',
              'django.middleware.locale.LocaleMiddleware',
              'django.middleware.common.CommonMiddleware',
              'django.middleware.clickjacking.XFrameOptionsMiddleware',
              'cms.middleware.user.CurrentUserMiddleware',
              'cms.middleware.page.CurrentPageMiddleware',
              'cms.middleware.toolbar.ToolbarMiddleware',
              'cms.middleware.language.LanguageCookieMiddleware']
INSTALLED_APPS = [
    'djangocms_admin_style', 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin', 
    'django.contrib.sites',
                        
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    'django.contrib.sitemaps', 
    'django.contrib.staticfiles',
    'django.contrib.messages', 
    'cms', 'menus', 'sekizai', 
    'treebeard',
    'djangocms_text_ckeditor', 
    'filer', 'easy_thumbnails',
    'djangocms_bootstrap4',
    'djangocms_bootstrap4.contrib.bootstrap4_alerts',
    'djangocms_bootstrap4.contrib.bootstrap4_badge',
    'djangocms_bootstrap4.contrib.bootstrap4_card',
    'djangocms_bootstrap4.contrib.bootstrap4_carousel',
    'djangocms_bootstrap4.contrib.bootstrap4_collapse',
    'djangocms_bootstrap4.contrib.bootstrap4_content',
    'djangocms_bootstrap4.contrib.bootstrap4_grid',
    'djangocms_bootstrap4.contrib.bootstrap4_jumbotron',
    'djangocms_bootstrap4.contrib.bootstrap4_link',
    'djangocms_bootstrap4.contrib.bootstrap4_listgroup',
    'djangocms_bootstrap4.contrib.bootstrap4_media',
    'djangocms_bootstrap4.contrib.bootstrap4_picture',
    'djangocms_bootstrap4.contrib.bootstrap4_tabs',
    'djangocms_bootstrap4.contrib.bootstrap4_utilities', 
    'djangocms_file',
    'djangocms_icon', 
    'djangocms_link', 
    'djangocms_picture',
    'djangocms_style',
    'djangocms_googlemap', 
    'djangocms_video',
    'the_irene_blog', 
    'aldryn_apphooks_config', 
    'parler', 
    'taggit',
    'taggit_autosuggest',
    'meta', 
    'djangocms_blog', 
    'sortedm2m',
    'discussions'
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

LANGUAGES = ('en', gettext('en')),
CMS_LANGUAGES = {(1): [{'code': 'en', 'name': gettext('en'),
                        'redirect_on_fallback': True, 'public': True, 'hide_untranslated':
                        False}], 'default': {'redirect_on_fallback': True, 'public': True,
                                             'hide_untranslated': False}}
CMS_TEMPLATES = ('fullwidth.html', 'Fullwidth'), ('homepage.html',
                                                  'Homepage'), ('sidebar_right.html', 'Sidebar Right')
X_FRAME_OPTIONS = 'SAMEORIGIN'
CMS_PERMISSION = True
CMS_PLACEHOLDER_CONF = {}
DATABASES = {'default': {'CONN_MAX_AGE': 0, 'ENGINE':
                         'django.db.backends.sqlite3', 'HOST': 'localhost', 'NAME': 'project.db',
                         'PASSWORD': '', 'PORT': '', 'USER': ''}}
THUMBNAIL_PROCESSORS = ('easy_thumbnails.processors.colorspace',
                        'easy_thumbnails.processors.autocrop',
                        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
                        'easy_thumbnails.processors.filters')
META_SITE_PROTOCOL = 'https'
META_USE_SITES = True
META_USE_OG_PROPERTIES = True
META_USE_TWITTER_PROPERTIES = True
META_USE_SCHEMAORG_PROPERTIES = True


BLOG_AVAILABLE_PERMALINK_STYLES = (
    ('full_date', _('Full date')),
    ('short_date', _('Year /  Month')),
    ('category', _('Category')),
)
BLOG_PERMALINK_URLS = {
    "full_date": "<int:year>/<int:month>/<int:day>/<str:slug>/",
    "short_date": "<int:year>/<int:month>/<str:slug>/",
    "category": "<str:category>/<str:slug>/",
}

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '788455549082-fltgfngg9qmo28954mal17fllrhf35ob.apps.googleusercontent.com',
            'secret': 'nuRsroHhInNKAeEHgQ_78Fim',
        }
    },
    'facebook': {
        'METHOD': 'js_sdk',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        'VERIFIED_EMAIL': True,
        'VERSION': 'v7.0',
    }
}

SOCIAL_AUTH_FACEBOOK_KEY = '1524159057923231'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET ='f7f935c1285b144cc24ae11703fa7962' #app key
ACCOUNT_EMAIL_REQUIRED=True
ACCOUNT_AUTHENTICATION_METHOD="email"
LOGIN_REDIRECT_URL = "/"
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_FORMS = {
    'login': 'accounts.forms.LoginForm',
    'signup': 'accounts.forms.SignupForm'
}

DISCUSSION_PLUGIN_TEMPLATES = [
    ("discussions/plugins/discussion_template1.html", "Template 1")
]