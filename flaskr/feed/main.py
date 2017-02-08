from pymongo import MongoClient
import random
import pprint

client = MongoClient('mongodb://localhost:27017/')

db = client.test_database
db.drop_collection('users_collection')
db.drop_collection('posts_collection')
users_collection = db.users_collection
posts_collection = db.posts_collection

from faker import Factory
fake = Factory.create()

users = []
# 100 fake users
for i in range(100):
	name = fake.name()
	password = fake.pystr(min_chars=6, max_chars=20)
	email = fake.email()
	username = fake.user_name()
	users.append({'name': name, 'password': password, 'email': email, 'username': username, 'following': []})

results = users_collection.insert_many(users)


# every user follows 10 other users randomly
for index, user in enumerate(users):
	count = 0
	random_list = []
	following = []
	while count < 10:
		r = int(random.random()*100)
		if r != index:
			random_list.append(r)
			count += 1
	for i in random_list:
		following.append(users[i]['_id'])
	users_collection.find_one_and_update({'_id': user['_id']}, {'$set': {'following': following}})

# every user have 20 posts
for user in users:
	posts = []
	for i in range(20):
		title = fake.sentence(nb_words=6, variable_nb_words=True)
		content = fake.paragraph(nb_sentences=5, variable_nb_sentences=True)
		published_time = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
		posts.append({'title': title, 'content': content, 'published_time': published_time, 'user': user['_id']})

results = posts_collection.insert_many(posts)


for user in users_collection.find():
	pprint.pprint(user)

