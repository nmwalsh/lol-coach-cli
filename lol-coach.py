# Server Response Generator
import json
import os
import sys
from os import system
import random


# Input Handling, Load Champion data into memory


input_champion = str(input('Enter: What champion are you having trouble with? \n'))
query_type = str(input('Would you like a Counter pick or a tip? Type `counter` or `tip` \n'))

json_file = 'champion_data/' + input_champion + '.json'

with open(json_file) as raw_json:
	data = json.load(raw_json)


# FUNCTIONS -------------------------------
# UNIQUE QUERIES
# return a list of counter champions
def counter(input_champion):
	raw_list = data['weak_against']
	counter_list = ""
	for entry in raw_list:
		champion = str(entry)
		counter_list = counter_list + ", " + champion
	output_text = "Strong counters for " + input_champion + " are: " + counter_list
	return output_text 

#return a random tip for the given champion
def tip(input_champion):
	available_tips = ['tip_0', 'tip_1','tip_2']
	random_tip= random.choice(available_tips)
	entry = data[random_tip]
	output_text= str(entry)
	return output_text

def generate_response(input_champion, query_type):
	if query_type == "counter":
		return counter(input_champion)
		#print(weak_against(input_champion))

	elif query_type == "tip":
		#print(tip(input_champion))
		return tip(input_champion)

print(generate_response(input_champion, query_type))
system("say %s" % generate_response(input_champion, query_type))
