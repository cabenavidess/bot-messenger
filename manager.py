#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
import json
import os

# from handler import receive_message

app = Flask(__name__)

MY_SECRET = os.environ.get("token_auxilio_en_inteligencia")
TOKEN = os.environ.get("EAAVNRLajTlABAGIIsFKsprlEMKxC2iUtxLefRTaeEZB4gdcEWUZBLYewTg7aCMXZBul6uoJpvXn2rDcEFvYsTjBeXQbaSsZAYkTtjAYZCjnElz5jZBPftYK6l7gJgsA7sO1d3UkT0lB9AMtBZBYe7HgSZBosZBKdM4hqOL8IVbVdvLiAMoqYXOlA1")

@app.route("/webhook", methods=["GET", "POST"])
def webhook():

	if request.method == "POST":
		payload = request.get_data()
		data =  json.loads(payload)

		# for page_entry in data["entry"]:
		# 	for message_event in page_entry["messaging"]:
        #
		# 		if "message" in message_event:
		# 			# receive_message(message_event, TOKEN)
		# return "ok"

	else:
		verify_token = request.args.get("hub.verify_token", "")
		if verify_token == MY_SECRET:
			return request.args.get("hub.challenge", "")
		else:
			return "Token o secreto no valido."

if __name__ == "__main__":
	app.run(port = 8000, debug = True)
