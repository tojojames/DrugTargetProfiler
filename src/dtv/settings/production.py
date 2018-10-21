# -*- coding: utf-8 -*-
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']

SECRET_KEY = 'zl+4@uzjjd0j(!4pi5espa@&)4=_-15_u=m(9_zo=mi-rqcyca'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
                'options': '-c search_path=network_visuals'
            },
        'NAME': 'compounds_20',
        'USER': 'fimm',
        'PASSWORD': 'pxqgBsFLTwTzc',
        'HOST': 'localhost',
        'PORT': ''
    }
}    