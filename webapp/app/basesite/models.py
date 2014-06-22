# -*- coding: utf-8 -*-


# add your models here
from basesite.configs import db


class UserModel(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.VARCHAR(128), nullable=False)
    passhash = db.Column(db.CHAR(40), nullable=False)
    dt_create = db.Column(
        db.DateTime(),
        nullable=False,
        default=db.func.current_timestamp()
    )

    def __init__(self, email, password):
        self.email = email
        self.passhash = self._hash_password(password)

    def _hash_password(self, password):
        return sha1(password).hexdigest()

    def verify_password(self, password):
        if(self._hash_password(password) == self.passhash):
            return True
        return False


class ProfileModel(db.Model):

    __tablename__ = 'profile'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.VARCHAR(128), nullable=False)
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
