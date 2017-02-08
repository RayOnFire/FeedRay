from . import userspace
from ..models.user import User
from flask import render_template, session, redirect, url_for, request, abort, flash
from flask_login import login_user
from ..flaskr import db
import random

@userspace.route('/random_login')
def random_login():
	users = list(db.session.query(User))
	random_user = users[int(random.randint(0, len(users)-1))]
	login_user(random_user)
	return redirect(url_for('user.profile'))
