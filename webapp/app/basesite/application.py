#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Author: SivaCoHan <sivacohan@gmail.com>
# Date: 2014-06-13
# File: application.py

import os
import logging
from flask import Flask

from basesite import configs
from basesite.configs import db, cache

from basesite.views import user_view
from basesite.views import system_view

__all__ = ['create_app']


DEFAULT_APP_NAME = 'basesite'

REGISTER_BLUE_PRINTS = (
    (system_view.instance, ''),
    (user_view.instance, '/user'),
)


def create_app(config=None, app_name=None):

    if app_name is None:
        app_name = DEFAULT_APP_NAME

    app = Flask(app_name)

    configure_app(app, config)
    configure_db(app)
    configure_blueprints(app)
    configure_cache(app)
    return app


def configure_app(app, config):
    app.config.from_object(configs.DefaultConfig())

    if config is not None:
        app.config.from_object(config)

    app.config.from_envvar('APP_CONFIG', silent=True)


def configure_db(app):
    db.init_app(app)


def configure_cache(app):
    cache.init_app(app)


def configure_blueprints(app):
    for blue, url_prefix in REGISTER_BLUE_PRINTS:
        app.register_blueprint(blue, url_prefix=url_prefix)
