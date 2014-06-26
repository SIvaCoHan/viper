#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Author: SivaCoHan <sivacohan@gmail.com>
# Date: 2014-06-13
# File: configs.py

import datetime

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.cache import Cache

db = SQLAlchemy()
cache = Cache()

DB_SALT = 'goodsalt'


class DefaultConfig(object):

    CONFIG_TYPE = 'default'

    DEBUG = True
    SECRET_KEY = 'it is secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dbu:dddd@localhost/viper'
    SQLALCHEMY_ECHO = False


class TestConfig(object):

    CONFIG_TYPE = 'test'

    DEBUG = True
    SECRET_KEY = 'it is secret'
    SQLALCHEMY_DATABASE_URI= 'postgresql+psycopg2://dbu:dddd@localhost/viper'
    SQLALCHEMY_ECHO = False


class ProductionConfig(object):

    CONFIG_TYPE = 'product'

    DEBUG = False
    SECRET_KEY = 'it is secret'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dbu:dddd@localhost/viper'
    SQLALCHEMY_ECHO = False
