#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-
# Author: SivaCoHan <sivacohan@gmail.com>
# File: models.py
# Date: 2014-06-26

from hashlib import sha1

from basesite.configs import db
from basesite.configs import DB_SALT


class UserModel(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(128), nullable=False, unique=True)
    email = db.Column(db.VARCHAR(128), nullable=False, unique=True)
    passhash = db.Column(db.CHAR(40), nullable=False)
    dt_create = db.Column(
        db.DateTime(),
        nullable=False,
        default=db.func.current_timestamp()
    )

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.passhash = self._hash_password(password)

    def _hash_password(self, password):
        passhash = sha1(DB_SALT+sha1(password+DB_SALT).hexdigest()).hexdigest()
        return passhash


class ProfileModel(db.Model):

    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    school = db.Column(db.VARCHAR(128), nullable=False)
    startyear = db.Column(db.Integer, nullable=False)
    endyear = db.Column(db.Integer, nullable=False)
    dt_create = db.Column(
        db.DateTime(),
        nullable=False,
        default=db.func.current_timestamp()
    )


class ArticleModel(db.Model):

    __tablename__ = 'article'

    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.VARCHAR(100), nullable=False)
    content = db.Column(db.TEXT, nullable=False)
    dt_create = db.Column(
        db.DateTime(),
        nullable=False,
        default=db.func.current_timestamp()
    )
