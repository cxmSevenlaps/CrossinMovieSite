import urllib.request
import json
import time

import web
db = web.database(dbn='sqlite', db='MovieSite.db')

def add_movie(data):
	movie = json.loads(data)
	print(movie['title'])
	db.insert('movie',id=int(movie['id']),title=movie['title'],
		origin=movie['original_title'],
		url=movie['alt'],
		rating=movie['rating']['average'],
		image=movie['images']['large'],
		directors=','.join([d['name'] for d in movie['directors']]),
		casts=','.join([c['name'] for c in movie['casts']]),
		year=movie['year'],
		genres=','.join(movie['genres'])
		#countries=','.join(movie['countries']),
		#summary=movie['summary'],
 	)


movie_ids = []
for index in range(0, 10 ,10):
	print(index)
	#需要导入urllib.request，教程中的urllib.urlopen不行，可能是因为python3
	response = urllib.request.urlopen('http://api.douban.com/v2/movie/top250?start=%d&count=10' % index)
	data = response.read()
	# print data

	data_json = json.loads(data)
	movie250 = data_json['subjects']
	for movie in movie250:
		movie_ids.append(movie['id'])
		print(movie['id'], movie['title'])
	time.sleep(3)

#print(movie_ids)

count = 0
for mid in movie_ids:
	print(count, mid)
	response = urllib.request.urlopen('http://api.douban.com/v2/movie/subject/%s' % mid)
	data = response.read()
	add_movie(data)
	count += 1
	time.sleep(2)


