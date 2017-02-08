from datetime import datetime
from .user import User
from ..flaskr import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    #category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    #category = db.relationship('Category',
    #    backref=db.backref('posts', lazy='dynamic'))
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User',
        backref=db.backref('posts', lazy='dynamic'))

    def _create(self, title, body, pub_date, author):
        self.title = title
        self.body = body
        self.pub_date = pub_date
        self.author = author

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def _create(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name