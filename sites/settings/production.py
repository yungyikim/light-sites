
import os

from util import get_server_info
from .base import *

SETTINGS = get_server_info('production')

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = SETTINGS['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = SETTINGS['ALLOWED_HOSTS']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': SETTINGS['DATABASES']['default']
}
BRAND = SETTINGS['BRAND']
TITLE = SETTINGS['TITLE']
DESCRIPTION = SETTINGS['DESCRIPTION']
