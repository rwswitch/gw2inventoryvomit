#!/usr/bin/python3

import json

inventory = json.load(open('items.json'))

for character in inventory:
	print(character)

items = dict()
bags = {}

#yo dawg, i herd u liek nested for loops for ungodly object lists
for character in inventory:
	print(character)
	if inventory[character]['bags']:
		for bag in inventory[character]['bags']:
			if bag:
				for item in bag['inventory']:
					if item:
						print(item['id'])
						if item['id'] not in items:
							item_characters = {character}
							items.update({item['id']:{'characters':item_characters}})
						else:
							print("item in set, adding: ", character, " to list of characters that hold: ", item['id'])
							items[item['id']]['characters'].add(character)
#							item_characters = items['id']['characters']
#							item_characters.add(character)
#							items.update({item['id']:new})


##item_request_json = set()
##for key in items.keys():
##	print(key)
##	item_request_json.add(key)
##
##print(item_request_json)

item_request_json = items.keys()

print(item_request_json)
print(json.dumps(list(item_request_json)))

items_obj = {}
for key in items:
        items_obj[key] = list(items.get(key)['characters'])

with open('itemobjectlist.json', 'w') as vomit:
        json.dump(items_obj, vomit)


##json.dump(items, open('itemdict.json', 'w'))
##
##with open('item_request.json', 'w') as outfile3:
##        json.dump(item_request_json, outfile3)
