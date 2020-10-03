# /src/config.py
import settings
import os

import sys
sys.path.append('../')


DATABASE_URL = settings.databaseurl


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    # JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    # JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')


app_config = {
    'development': Development,
    'production': Production,
}
