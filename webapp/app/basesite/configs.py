# -*- coding: utf-8 -*-

import datetime

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cache import Cache

db = SQLAlchemy()
cache = Cache()


class DefaultConfig(object):

    CONFIG_TYPE = 'default'

    DEBUG = True
    SECRET_KEY = 'it is secret'
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://xxxxxxxxxxxxx'
    SQLALCHEMY_ECHO = False


class TestConfig(object):

    CONFIG_TYPE = 'test'

    DEBUG = True
    SECRET_KEY = 'it is secret'
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://xxxxxxxxxxxxx'
    SQLALCHEMY_ECHO = False


class ProductionConfig(object):

    CONFIG_TYPE = 'product'

    DEBUG = False
    SECRET_KEY = 'it is secret'
    SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://xxxxxxxxxxxxx'
    SQLALCHEMY_ECHO = False
