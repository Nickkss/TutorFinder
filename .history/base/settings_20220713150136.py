from pathlib import Path
from django.contrib.messages import constants as message_constants

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l!$v^8pzd5ra86k@us5_2k_577ea*twuz%%z(h1ylu_hr622i%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third Party Apps
    'ckeditor',
    'ckeditor_uploader',
    'rest_framework',
    'crispy_forms',
    "crispy_bootstrap5",
    
    # My Apps
    'frontend.apps.FrontendConfig',
    'common.apps.CommonConfig',
    'users.apps.UsersConfig',
    'language.apps.LanguageConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Language Middleware
    'django.middleware.locale.LocaleMiddleware',
    
    # Custom Middlewares
    'users.middleware.CreateProfile',
]

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
                # Custom Context Processors
                'common.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR.joinpath("static")
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath("media")


MESSAGE_TAGS = {message_constants.DEBUG: 'debug',
                message_constants.INFO: 'info',
                message_constants.SUCCESS: 'success',
                message_constants.WARNING: 'warning',
                message_constants.ERROR: 'danger'}

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_JQUERY_URL = 'https://code.jquery.com/jquery-3.6.0.min.js'

CKEDITOR_SETTINGS = {
    'allowedContent': True,
    'autoParagraph': False,
    'baseHref': '/media/',
    'enterMode': 'CKEDITOR.ENTER_BR',
    'extraAllowedContent': 'style;*;*{*}',
    'removePlugins': 'stylesheetparser,about,showblocks,language,form,flash,iframe',
}

CKEDITOR_CONFIGS = {
    'default':{
    'toolbar': 'Custom',
    'toolbar_Custom':[
		{ "name": 'document', "items": [ 'Source', '-', 'Save', 'NewPage', 'ExportPdf', 'Preview', 'Print', '-', 'Templates' ] },
		{ "name": 'clipboard', "items": [ 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo' ] },
		{ "name": 'editing', "items": [ 'Find', 'Replace', '-', 'SelectAll', '-', 'Scayt' ] },
		{ "name": 'forms', "items": [ 'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField' ] },
		'/',
		{ "name": 'basicstyles', "items": [ 'Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'CopyFormatting', 'RemoveFormat' ] },
		{ "name": 'paragraph', "items": [ 'NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl', 'Language' ] },
		{ "name": 'links', "items": [ 'Link', 'Unlink', 'Anchor' ] },
		{ "name": 'insert', "items": [ 'Image', 'Table', 'HorizontalRule', 'Smiley', 'EmojiPanel', 'SpecialChar', 'PageBreak', 'Iframe' ] },
		'/',
		{ "name": 'styles', "items": [ 'Styles', 'Format', 'Font', 'FontSize' ] },
		{ "name": 'colors', "items": [ 'TextColor', 'BGColor' ] },
		{ "name": 'tools', "items": [ 'Maximize', 'ShowBlocks' ] },
		{ "name": 'about', "items": [ 'About'] }
	],
     'height': 500,
    'width': 1000,
    'skin': 'office2013',
    'extraPlugins': ",".join(['colorbutton', 'emoji']),
    }
}

# Theme JAZZMIN SETTINGS
JAZZMIN_SETTINGS = {
    "site_title": f"Super Admin Dashboard",
    "site_header": f"Super Admin Dashboard",
    "site_brand": f"Super Admin",
    "site_logo": "/images/logo/logo-white.png",
    "site_logo_classes": "img-circle",
    "site_icon": "/assets/favicon.ico",
    "welcome_sign": f"Welcome to the Super Admin Dashboard",
    "copyright": "Designed & Developed by Hemant B",
    "search_model": "users.User",
    "user_avatar": "avtar",
    
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["users",],
    
    "icons": {
        "auth": "fas fa-users-cog",
        "users.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": False,
    "custom_css": None,
    "custom_js": None,
    "show_ui_builder": True,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
    "language_chooser": True,
}
JAZZMIN_SETTINGS = JAZZMIN_SETTINGS
JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-navy",
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-navy",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cosmo",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-danger",
        "success": "btn-success"
    }
}


VALID_IMAGE_FILETYPES = ['JPEG', 'PNG', 'SVG', 'GIF']


LOGIN_URL = "/auth/login/"

AUTH_USER_MODEL = 'users.User'