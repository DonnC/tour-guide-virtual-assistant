'''
 * run server with command below
 * python3.6 -m rasa_core.server -d /home/donald/Projects/Python3.6/rasa bots/nust_tour_guide/models/dialogue -u /home/donald/Projects/Python3.6/rasa bots/nust_tour_guide/models/tour_guide/default/nlu --debug -o out.log --cors *
 * can use postman or the run this code for a more interactive 
 * console experience
 ** integrate with flask, webwhatsapi, texts, mqtt, IoT
'''

import requests as req
import json
from pprint import pprint
from time import sleep
from uuid import uuid4
import sys
import argparse

def check_arg(args=None):
	parser = argparse.ArgumentParser(description='get port and baud rate of hardware to serial link with Node-Red')
	parser.add_argument('-p', '--port',
						help= 'port number of hardware device',
						required = 'True')
	parser.add_argument('-b', '--baude_rate',
						help = 'baud rate of hardware device',
						required = 'True')

	results = parser.parse_args(args)
	return(results.port,
		   results.baude_rate)

if __name__ == "__main__":
	p, b = check_arg(sys.argv[1:])
	print('Port: ', p)
	print('Baud: ', b)

def chat(msg):
	data = '{"query": "%s"}' %msg
	url = "http://localhost:5005/conversations/{sender_id}/respond"
	res = req.post(url.format(sender_id=user_id), data=data)
	reply = res.json()
	#pprint(reply)
	#print("\n\n")
	
	if len(reply) != 1 and len(reply) > 1:
		for data in reply:
			bot_response = data.get("text") + "\n"
		return bot_response

	elif len(reply) ==1:
		return reply[0]['text']
	
	else:
		reply = "sorry, I don't know how to answer that ATM"
		return reply

	sleep(1)

def run_console():
	# give each user requests a unique id as sender ID
	user_id = uuid4()
	running = True
	while running:
		user = input("USER: ")
		# get bot response
		text = chat(user)
		bot = print("BOT: {}".format(text))


