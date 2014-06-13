#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Author: SivaCoHan <sivacohan@gmail.com>
# Date: 2014-06-13
# File: manage.py

import os
import sys
from flask import current_app
from flask.ext.script import Manager, prompt, prompt_pass,\
    prompt_bool, prompt_choices
from flask.ext.script import Server

from basesite import create_app
from basesite import configs
from basesite.models import db, UserModel

manager = Manager(create_app)
app = create_app


@manager.command
def initdb():
    if prompt_bool("Are you sure? You will init your database"):
        db.create_all()


@manager.command
def dropdb():
    if prompt_bool("Are you sure? You will lose all your data!"):
        db.drop_all()


@manager.option('-u', '--username', dest='username', required=True)
@manager.option('-p', '--password', dest='password', required=True)
def createuser(username=None, password=None):
    u = UserModel(username=username, password=password)
    db.session.add(u)
    db.session.commit()

manager.add_command('runserver', Server())

if __name__ == '__main__':
    manager.run()
