#!/usr/bin/python3

import requests
import json
import urllib

#TODO: refactor to pull external apikey
apikey = ''
url = 'https://api.guildwars2.com/'
version = 'v2'
endpoint = ''

uri = url + version + '/' + endpoint

#TODO: do a better job of debugging: stop using prints for that.
print (uri)

auth = {'Authorization':'Bearer ' + apikey}
print (auth['Authorization'])

uri = uri + 'characters'
characters = requests.get(uri ,headers=auth)

inventory = {}
inventory_response = {}
for character in characters.json():
	inventory_uri = uri + '/' + urllib.parse.quote(character) + '/inventory'
	print('Accessing: ' + inventory_uri)
	inventory_response[character] = requests.get(inventory_uri, headers=auth)
	inventory[character] = inventory_response[character].json()

def update_index(dictionary = dict(), key = None, value = None):
	if key in dictionary:
		dictionary.update(key,{dictionary[key],value})
		return
	else:
		dictionary.update(key,value)


with open('items.json', 'w') as outfile:
	json.dump(inventory, outfile)

items = dict()
bags = {}

#I threw up a little trying to get the nested data in a clean way
#TODO: refactor to use a actual object to handle this nightmare

#What it does is a) iterate through things b) nullcheck to not die, because that would happen sometimes c) grab items and map to list of characters
for character in inventory:
	print(character)
	if inventory[character]['bags']:
		for bag in inventory[character]['bags']:
			if bag:
				for item in bag['inventory']:
					if item:
						print(item['id'])
						if item['id'] not in items:
							items.update({item['id']:{character}})
						else:
							print("item in set, adding: ", character, " to list of characters that hold: ", item['id'])
							items[item['id']]['characters'].add(character)

item_request_json = ''
for key in items.keys():
	print(key)
	item_request_json.join(',', key)

print(item_request_json)
	
#item_request_json = {'items':item_request_json}
print(item_request_json)


#I could have sworn this vomits to a file somewhere. Maybe I've just been using the console for that step until I go back through babby's first program
#TODO: output junk to files
#TODO: get item data
