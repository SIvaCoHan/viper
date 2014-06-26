#! /usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# Author: SivaCoHan
# Date: 2014-06-22
# File: forms.py

from flask.ext.wtf import Form
from wtforms import validators, TextField, PasswordField,\
    TextAreaField

from sqlalchemy.orm.exc import NoResultFound

class RegisterForm(Form):
    "user register"
    username = TextField(u'用户名', [validators.Required(u'请输入用户名')])
    email = TextField(u'邮箱', [validators.Required(u'请输入邮箱')])
    password = PasswordField(
        u'密码',
        [
            validators.Required(u'请输入密码'),
            validators.EqualTo('confirm', message=u'两次输入密码不一致'),
        ]
    )
    confirm = PasswordField(u'重复密码')

    # TODO username not valide
    # TODO email not valide


class LoginForm(Form):
    username = TextField(u'用户名')
    password = PasswordField(u'密码')


class Article(Form):
    title = TextField(u'标题')
    content = TextAreaField(u'内容')
