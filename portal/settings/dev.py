"""
Django development settings for portal project.
Extends base settings with development-specific configurations.
"""

from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

# Development database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Disable security middleware for development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False

# Email configuration for development (console backend)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Install django-extensions for development helpers
if 'django_extensions' not in INSTALLED_APPS:
    INSTALLED_APPS += ['django_extensions']

# Enable detailed error pages
INTERNAL_IPS = ['127.0.0.1']
