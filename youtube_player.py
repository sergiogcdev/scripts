#!/usr/bin/python3

import subprocess
import json
from youtubesearchpython import SearchVideos

term = input('Introduce term to search ')

search = SearchVideos(term, offset = 1, mode = "json", max_results = 10)

json_data = json.loads(search.result())

results = json_data['search_result']

for item in results:
	print(item['index'], ') ', item['title'])
	print('Link: ', item['link'])

copy_link = input('\nDo you want to play some link? [y/N] ')

if(copy_link == 'Y' or copy_link == 'y'):
	num = int(input('Introduce index '))
	for video in results:
		if(video['index'] == num):
			command = ("playx {gotolink}".format(gotolink = video['title'])).split()
			subprocess.call(command)
else:
    print('Goodbye')

