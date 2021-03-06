from flask_restful import Resource, reqparse
from flask_login import current_user, login_user
from ..flaskr import user_manager, db
from ..models.post import Post
from ..models.user import User
import random
from datetime import timedelta
from flask import make_response, request, current_app
from functools import update_wrapper
from six import string_types

class Feed(Resource):

    #@crossdomain(origin='*')
    def get(self):
        if not current_user.is_authenticated:
            #users = list(db.session.query(User))
            #random_user = users[int(random.randint(0, len(users)-1))]
            #login_user(random_user)
            current_user.unauthorized()
        #app.logger.info(current_user)
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, help='Rate to charge for this resource')
        args = parser.parse_args()
        if args['page'] == None:
            args['page'] = 1
        feeds = []
        for user in current_user.following:
            feeds += Post.query.filter_by(author=user)
        feeds.sort(key=lambda x: x.pub_date, reverse=True)
        feeds = [{'username': item.author.name,
                'avatar': item.author.avatar, 
                'title': item.title, 
                'body': item.body, 
                'pub_date': str(item.pub_date)} for item in feeds][(args['page']-1)*20:(args['page']*20)]
        return {'count': len(feeds), 'posts_list': feeds}, 200, {'Access-Control-Allow-Origin': '*'} 