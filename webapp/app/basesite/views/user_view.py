# -*- coding: utf-8 -*-

# author: notedit <notedit@gmail.com>
# date: 2012/12/01  morning

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


instance = Blueprint('what',__name__)

class RegisterView(MethodView):
    def get(self):
        return render_template('register.html')

instance.add_url_rule('/register',view_func=RegisterView.as_view('register'),methods=['GET',])
