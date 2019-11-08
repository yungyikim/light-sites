
import os

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd=_c5q5h*+bp!e98io*&8g7djq7xzeq7y8(xx+21oykb!!sx6='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
