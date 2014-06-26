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

    def post(self):
        pass


class UpdateArticleView(MethodView):
    def get(self):
        return render_template('post.html')

    def post(self):
        pass


class GetArticleView(MethodView):
    def get(self):
        return render_template('article.html')


class ListArticleView(MethodView):
    def get(self):
        return render_template('article_list.html')


# Add instance
instance.add_url_rule(
    '/post',
    view_func=PostArticleView.as_view('post_article'),
    methods=['GET', ]
)
instance.add_url_rule(
    '/update',
    view_func=UpdateArticleView.as_view('update_article'),
    methods=['GET', ]
)
instance.add_url_rule(
    '/t',
    view_func=GetArticleView.as_view('get_article'),
    methods=['GET', ]
)
instance.add_url_rule(
    '/list',
    view_func=ListArticleView.as_view('list_article'),
    methods=['GET', ]
)
