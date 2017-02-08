import os
import traceback
import random
import pagan
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_user import SQLAlchemyAdapter, UserManager
from flask_login import LoginManager
from flask_admin.contrib.sqla import ModelView
from flask_restful import Api, Resource

app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__) # load config from this file , flaskr.py

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
    USER_ENABLE_CONFIRM_EMAIL = False,
    USER_ENABLE_LOGIN_WITHOUT_CONFIRM_EMAIL = True,
    USER_SEND_PASSWORD_CHANGED_EMAIL = False,
    USER_SEND_USERNAME_CHANGED_EMAIL = False,
    USER_LOGIN_TEMPLATE = 'login.html',
    USER_REGISTER_TEMPLATE ='register.html',
    USER_PROFILE_TEMPLATE = 'user_profile.html',
    USER_LOGIN_URL = '/login'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

try:
    from flaskr.models.user import User
    from flaskr.models.post import Post, Category
    from flaskr.models.user_following import UserFollowing


    db_adapter = SQLAlchemyAdapter(db, User)        # Register the User model
    user_manager = UserManager(db_adapter, app)     # Initialize Flask-User

    admin = Admin(app, name='microblog', template_mode='bootstrap3')
    admin.add_view(ModelView(Post, db.session))
    admin.add_view(ModelView(Category, db.session))

    api = Api(app)

    class HelloWorld(Resource):
        def get(self):
            return {'hello': 'world'}

    #api.add_resource(HelloWorld, '/feed')
    from flaskr.feed.get_feed import Feed
    api.add_resource(Feed, '/feed')

    from flaskr.blogger import blogger as blogger_blueprint
    from flaskr.userspace import userspace as userspace_blueprint
    app.register_blueprint(blogger_blueprint, url_prefix='/blogger')
    app.register_blueprint(userspace_blueprint, url_prefix='/user')

    # app.logger.info(app.url_map)
except Exception as e:
    traceback.print_exc()


@app.route('/')
def home():
    return render_template('index.html')

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.cli.command()
def test():
    print('test')

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    db.create_all()
    print('Initialized the database.')

@app.cli.command('dropdb')
def dropdb_command():
    db.drop_all()

@app.cli.command('fake')
def fake_command():
    from faker import Factory
    fake = Factory.create()
    users = []
    db.drop_all()
    db.create_all()
    for i in range(100):
        name = fake.name()
        password = fake.pystr(min_chars=6, max_chars=20)
        email = fake.email()
        username = fake.user_name()
        sign_up_time = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
        avatar_img = pagan.Avatar(username, pagan.SHA512)
        avatar = 'static/avatar/' + username + '.png'
        avatar_img.save('static/avatar/', username)
        u = User()
        u._create(username, password, name, email, sign_up_time, avatar)
        db.session.add(u)
        db.session.commit()
        users.append(u)
        # create 10 posts every user
        for _ in range(10):
            p = Post()
            title = fake.sentence(nb_words=6, variable_nb_words=True)
            content = fake.paragraph(nb_sentences=5, variable_nb_sentences=True)
            published_time = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)        
            p._create(title, content, published_time, u)
            db.session.add(p)
            db.session.commit()

    for user in users:
        count = 0
        while count < 10:
            i = random.randint(0, len(users)-1)
            if users[i] != user and not users[i] in user.following:
                user.following.append(users[i])
                count += 1
    #users[0].following.append(users[1])
    #users[1].following.append(users[0])
    db.session.commit()
    #for a in db.session.query(User).order_by(User.id):
    #    print(a.following)

@app.cli.command('testdb')
def testdb_command():
    #from flaskr.models.user import User
    import datetime
    from faker import Factory
    fake = Factory.create()
    '''
    #db.drop_all()
    #db.create_all()
    admin = User()
    admin.username = 'admin'
    admin.password = 'password'
    admin.email = 'admin@ray.com'
    admin.sign_up_time = datetime.datetime.now()
    admin.name = 'Ray Fire'
    #guest = User()
    db.session.add(admin)
    #db.session.add(guest)
    db.session.commit()
    #print(User.query.all())
    #print(User.query.filter_by(username='admin').first())
    '''
    admin = User.query.filter_by(username='admin').first()
    py = Category()
    py._create('python')
    p = Post()
    p._create('Python is great!', 'Hello World!', fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None), py, admin)
    db.session.add(py)
    db.session.add(p)
    db.session.commit()
    #print(py.posts.all())
    #print(admin.posts.all())
