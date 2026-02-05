"""
Settings package initialization.
Imports the appropriate settings based on environment.
"""

import os

# Determine which settings to use based on DJANGO_SETTINGS_MODULE
# Default to development settings
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development').lower()

if ENVIRONMENT == 'production':
    from .prod import *
else:
    from .dev import *
