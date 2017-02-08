from . import blogger
from ..models.post import Post
#from flaskr import get_db
from flask import render_template, session, redirect, url_for, request, abort, flash

@blogger.route('/')
def show_entries():
    entries = Post.query.all()
    return render_template('show_entries.html', entries=entries)

@blogger.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@blogger.route('/logintest', methods=['POST', 'GET'])
def login_test():
	return render_template('login.html')