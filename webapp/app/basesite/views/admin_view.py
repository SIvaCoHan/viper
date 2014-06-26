#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Author: sivacohan <sivacohan@gmail.com>
# Date: 2014-06-20
# File: admin_view.py

import sys
import time
import flask
from flask import Blueprint
from flask import request
from flask import render_template
from flask import g
from flask import Response
from flask import current_app
from flask import session
from flask import jsonify
from flask.views import MethodView
from flask.views import View


instance = Blueprint('admin', __name__)


class LoginView(MethodView):
    def get(self):
        return render_template('login.html')


class ProfileView(MethodView):
    def get(self):
        return render_template('profile.html')


# Add instance
