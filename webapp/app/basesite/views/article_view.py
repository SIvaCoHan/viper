#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Author: sivacohan <sivacohan@gmail.com>
# Date: 2014-06-20
# File: article_view.py

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


instance = Blueprint('article', __name__)


class PostArticleView(MethodView):
    def get(self):
        return render_template('post.html')


class GetArticleView(MethodView):
    def get(self):
        return render_template('article.html')


class ArticleListView(MethodView):
    def get(self):
        return render_template('article_list.html')


# Add instance
instance.add_url_rule(
    '/register',
    view_func=RegisterView.as_view('register'),
    methods=['GET', ]
)
