from ..flaskr import db
from flask_user import UserMixin
from .user_following import UserFollowing

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)

    # User authentication information
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')

    # User email information
    email = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False, server_default='')
    sign_up_time = db.Column(db.DateTime())

    # User information
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')

    following = db.relationship('User',
                           secondary=UserFollowing.__table__,
                           primaryjoin=id==UserFollowing.follower_id,
                           secondaryjoin=id==UserFollowing.followee_id)

    admin = db.Column('is_admin', db.Boolean, nullable=False, server_default='0')

    avatar = db.Column(db.String(100), nullable=False)

    def _create(self, username, password, name, email, sign_up_time, avatar):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.sign_up_time = sign_up_time
        self.avatar = avatar

    def get_following(self):
        following = db.session.execute("SELECT name, avatar, title, body, pub_date FROM user_following AS a JOIN post AS b ON a.followee_id = b.author_id JOIN user AS c ON a.followee_id = c.id WHERE a.follower_id = :user_id ORDER BY b.pub_date DESC", {'user_id':self.id})
        return following.fetchall()