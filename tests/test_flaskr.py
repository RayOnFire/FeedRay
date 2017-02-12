import os
import flaskr
import unittest
from flask import g
import timeit
from flaskr.models.user import User
from flaskr.models.post import Post
from flask_login import current_user, login_user
import random
import cProfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()
        with flaskr.app.app_context():
            g.db = 'abc'

    def tearDown(self):
        #os.close(self.db_fd)
        #os.unlink(flaskr.app.config['DATABASE'])
        pass

def test_db():
    db = flaskr.flaskr.db
    stmt = """\
users = list(db.session.query(User))
random_user = users[int(random.randint(0, len(users)-1))]
feeds = []
for user in random_user.following:
    feeds += Post.query.filter_by(author=user)
    feeds.sort(key=lambda x: x.pub_date, reverse=True)
    """

    stmt2 = """\
users = list(db.session.query(User))
random_user = users[int(random.randint(0, len(users)-1))]
random_user.get_following()
    """
    print(timeit.timeit(stmt=stmt, globals=globals(), number=100))
    print(timeit.timeit(stmt=stmt2, globals=globals(), number=100))

if __name__ == '__main__':
    #unittest.main()
    db = flaskr.flaskr.db
    app = flaskr.app.test_client()
    stmt2 = """\
users = list(db.session.query(User))
random_user = users[int(random.randint(0, len(users)-1))]
random_user.get_following()
    """
    #users = list(db.session.query(User))
    #random_user = users[int(random.randint(0, len(users)-1))]
    #print(timeit.timeit(stmt=stmt2, globals=globals(), number=1))
    #print(timeit.timeit('rv = app.get("/")', globals=globals(), number=100))
    print(timeit.timeit('rv = app.get("/feed")', globals=globals(), number=1000))
    print(timeit.timeit('rv = app.get("/feednew")', globals=globals(), number=1000))
    #cProfile.runctx(stmt2, globals(), None)


