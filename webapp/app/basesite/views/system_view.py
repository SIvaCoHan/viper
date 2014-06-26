#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Author: sivacohan <sivacohan@gmail.com>
# Date: 2014-06-20
# File: system_view.py

import sys
import time
import flask
from flask import Blueprint
from flask import request
from flask import render_template
from flask import g
from flask import redirect
from flask import url_for
from flask import Response
from flask import current_app
from flask import session
from flask import jsonify
from flask.views import MethodView
from flask.views import View

from basesite.configs import db
from basesite.forms import RegisterForm, LoginForm
from basesite.models import UserModel


instance = Blueprint('system', __name__)


class HomeView(MethodView):
    def get(self):
        return render_template('home.html')


class RegisterView(MethodView):
    def get(self):
        form = RegisterForm()
        ret = {
            'title' : u'注册',
            'form' : form,
        }
        return render_template('register.html', **ret)

    def post(self):
        form = RegisterForm()
        if not form.validate():
            # TODO fix here
            return "Something Wrong"
        u = UserModel(
            username= form.username.data,
            email = form.email.data,
            password = form.password.data,
        )
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('system.login'))


class LoginView(MethodView):
    def get(self):
        form = LoginForm()
        ret = {
            'title' : u'登录',
            'form' : form,
        }
        return render_template('login.html', **ret)

    def post(self):
        form = LoginForm()
        if not form.validate():
            # TODO
            return "Something Wrong"
        u = UserModel.query.filter(UserModel.username == form.username.data)
        if u.count() < 1:
            return u'用户名不存在'
        u = u.one()
        if u._hash_password(form.password.data) != u.passhash:
            return u'用户名或密码错误'
        else:
            return u'登录成功'


# Add instance
instance.add_url_rule(
    '/',
    view_func=HomeView.as_view('home'),
    methods=['GET', ]
)
instance.add_url_rule(
    '/register',
    view_func=RegisterView.as_view('register'),
    methods=['GET', 'POST' ]
)
instance.add_url_rule(
    '/login',
    view_func=LoginView.as_view('login'),
    methods=['GET', 'POST' ]
)
