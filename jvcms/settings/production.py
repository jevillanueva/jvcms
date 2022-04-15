import os
from .base import *

DEBUG = False
SECRET_KEY = os.getenv("APP_SECRET_KEY", 'django-insecure-*sl%whcx#i*k+gqy+(^2c(b57v22##+ks4*$zyilfxpz^gnny(')
ALLOWED_HOSTS = ['*'] 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
try:
    from .local import *
except ImportError:
    pass
