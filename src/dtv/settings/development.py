# -*- coding: utf-8 -*-
from .base import *

def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)
 
SECRET_KEY = get_env_variable('SECRET_KEY')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
                'options': '-c search_path=network_visuals,pharmacodb,drugtargetcommons'
            },
        'NAME': 'compounds_20',
        'USER': 'fimm',
        'PASSWORD': 'pxqgBsFLTwTzc',
        'HOST': 'localhost',
        'PORT': '6432'
    }
}