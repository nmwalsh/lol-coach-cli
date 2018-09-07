#champion image scraper
import json
import os
import sys

base_url = "http://ddragon.leagueoflegends.com/cdn/6.24.1/img/champion/"

#import JSON data
with open('champion_name_and_id.json') as raw_json:
	data = json.load(raw_json)
	#print(data)
#get list of all hero id's from JSON
#names = data['data'][1]['key']
print(names)

ids = data['data'][]
#for NAME in champ_names, query URL and save image to SAVE_DIR with name NAME

#for name in champ_names
