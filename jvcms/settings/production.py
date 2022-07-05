import os
from .base import *

DEBUG = False
SECRET_KEY = os.getenv("APP_SECRET_KEY", 'django-insecure-*sl%whcx#i*k+gqy+(^2c(b57v22##+ks4*$zyilfxpz^gnny(')
CSRF_TRUSTED_ORIGINS = os.getenv("APP_CSRF_TRUSTED_ORIGINS", 'http://localhost,https://localhost').split(',')

ALLOWED_HOSTS = ['*'] 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
STATICFILES_STORAGE= 'django.contrib.staticfiles.storage.StaticFilesStorage'
COMPRESS_OFFLINE = True
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]
COMPRESS_CSS_HASHING_METHOD = 'content'
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "INFO", "handlers": ["file"]},
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "/app/django.log",
            "formatter": "app",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "INFO",
            "propagate": True
        },
    },
    "formatters": {
        "app": {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
}
try:
    from .local import *
except ImportError:
    pass
