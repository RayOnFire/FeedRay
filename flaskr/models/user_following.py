from ..flaskr import db

class UserFollowing(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	followee_id = db.Column(db.Integer, db.ForeignKey('user.id'))
