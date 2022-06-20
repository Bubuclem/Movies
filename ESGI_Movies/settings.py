import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pc+y641rlw-y880!fl39p2e_$7s*t+$(yw0pr%ld%jj%zn!kxu'
SECRET_KEY_TMDB = '907eefe505cd622142ef9afae861393d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
INTERNAL_IPS = ALLOWED_HOSTS

# Application definition

INSTALLED_APPS = [
    'movies',
    'shows',
    'actors',
    'management',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_extensions',
    'social_django',
    'tailwind',
    'theme',
    'django_browser_reload'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'ESGI_Movies.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'ESGI_Movies.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'theme/static/'

STATICFILES_DIRS = [os.path.join(BASE_DIR, STATIC_URL)]

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, STATIC_URL)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django-Tailwind
# https://django-tailwind.readthedocs.io/en/latest/installation.html

TAILWIND_APP_NAME = 'theme'

# Django Rest Framework
# https://www.django-rest-framework.org/tutorial/quickstart/

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}

# Login page
# https://docs.djangoproject.com/fr/4.0/ref/settings/#login-url

LOGIN_URL = '/authentification/'

# Oauth2
# https://python-social-auth.readthedocs.io/en/latest/configuration/django.html

# Twitter
SOCIAL_AUTH_TWITTER_KEY = 'oHqs6gUI9vIXUX4eKdvy8JtB3'
SOCIAL_AUTH_TWITTER_SECRET = 'eqIPBcHLNQErgY8CPi67hu4tF5o6W5B8EDwPryRHFiQfs9RBSi'

# GitHub
SOCIAL_AUTH_GITHUB_KEY = 'a337eadc733ab66d3fec'
SOCIAL_AUTH_GITHUB_SECRET = '79eb4603cf0df2726d0c5905e925ecb5973c5ae3'

# Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'fd7ab943d6304818cfbb2b44103c30f507eda40c'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCvSTL/18cyP1to\nVGbh5HI6IlC044guVvAZYns0movV8Zk0nbpDnBTxZ+XzE2V8xO+8QmNVpHnVpKn7\nYH/jV53CNLF4/8JPo/qftZ4Nha6IavvbmDL8S5Hoy2Uen68MW7sKI4Z85qIz3Wl6\nQHThRciHuls/4gwFWviZN6pr7kDr6kPCiyS2vEKv6OkJ9bDWxHsnZDN+U3ylPlIn\nZmXvHGpXT3GJYqsJiRiLvq6pzxYd19hUdTVSr4kp1MS+r2f2wjxB1NE6VxU46oSp\nCTZI3QyM/17cZvrYnsSTyI1Ug5db/KnKyEWSj5W4udmyzGYAaLZdXAaBzlXDrMbb\nV6+LaAqPAgMBAAECggEAPhkHFccqXR0/806PYjCN3RWCFQtUl+IZzkxqzICB0Kn2\nNkM4lTIq4zkFKF+zQQf9zGqSiWkq9mqPA6y0seQ80evcAbtN6ev0YnczhqPY6KBK\nGIoraeEV0GyaJsa4e37V3Oon/4CvbwNeFj7WiWYw/BCjuhaJXq5TSuiDGhh+bHTr\nOQQwJRNVM1w7TnFZh9pIuhDJA99bqCKz5wMpiLBJ8ZrUxxE7zfzRTQJ2z/qSen9D\nHvlsbNqmlC0ddJh8z3ztgOqrl7ZF21+YjQrXVMpdxSNuMx/yczr0mTYGJd2MTb8y\ninDaDq/iz701YRihveyw3QS+ABpmLpCJZTrcKoXw+QKBgQDtdLrOvI3pz1j+D/2S\nXhdJW2ALTxD5qbR3XIVg9Tg9ctekG3tQpQKwCaaf8YvJzdVDlzJkTQGUA7X9Si4E\ngnMF0S5Uj86Im6yHxs99MAs7qzLRhgleOIdkCL21BqiyzkaA8V5dZjKGMIGwKzeY\ntz1ribzjFScAIL3IqXTIzGu1BwKBgQC8+Y2Gyu8lzUc1ofe47eAtut1qZ/DzZmDJ\ni5JQbKBDhPH9flUkXK22nSpyElkR2d4Zgh28kjOff+M7GchjEv7Qwio0mEwvjqqD\ngZJA5jZ78opA6Kz+blY3lajB+jPwMDy7Ejz8gU9J/Gbg9/RNIjKnk5HJFU+c2thH\njIvRXhpkOQKBgQDMX0lhIhwqfpGjqXOfhGgadRDG6vg7SXrPuMv7VVNgX/WFgzmx\ngTQ8+zF0O9sKh6PkFsACX9zZ3g/Gvw+4ReZlvVJY6aTjIslt2wk+QBmK86A7gVeS\nxqiQyo0sv1x2+N7pn9SOIqWdpSYZ0Dh7skqkwdnWwJ/elk+B44dmQ7r4BQKBgBv/\npXZpLtGc/oX1v2xI4kQkQZX4XHzTmFeENGNyFLSsR+ZVB2xhxuMdmiJYkZXRf9Sr\nsJg12SwymIozIbt8HwDzI6mzPuZ07tKZKgAvm7b1koJXdvojguatZ9mFpphZrUXS\nR/LpfcPqf5upYSrkfDjT5m+ylp8Y1Z6UNksI9EQRAoGBAOaxWm9q4/DYmKHeoxhV\n1n7EJSqwNjTmgYtL2iT3Pw3TQAbLbBFmo5zUwxHdLG7gf3J8DjJnEwAXgxaazvs2\nSEifmUyWvBTNjW6E/3VqmBTAWuu+rpT3UsVdbMQihBH+YdVWUDx85hI8Eqh1Gnd7\ncIQ6kOntGXHEoaKLyHpQeaz0'

SOCIAL_AUTH_URL_NAMESPACE = 'social'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)