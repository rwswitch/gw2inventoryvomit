#!/usr/bin/python3
import unittest
import os
from api import Gw2API
from characters import Character, CharacterList
from items import Item,ItemList

assert os.environ['gw2apikey'], 'gw2apikey not set, please set a gw2apikey environment variable'
gw2_api_key = os.environ['gw2apikey']


class TestApi (unittest.TestCase):

    def test_check_apikey(self):
        self.assertEqual(type(gw2_api_key), str)
        print(gw2_api_key)

    # def test_init(self):
    # 	api = Gw2API()
    # 	# api.get_endpoint()
    # 	self.assertIsNotNone(api)

    def test_init_character_from_list(self):
        api = Gw2API(gw2_api_key)
        data = api.get_endpoint ('characters')
        self.assertEqual(type(data), list)
        print (data)
        # todo: better job of getting a test in here
        self.assertEqual(data,
                          ['Cola Warden', 'Justice Awesomeface', 'Switch Awesomeface', 'Gern Ogrebar', 'Wasted Dreams',
                           'Justice Ebonstring', 'Iron Switch', 'Glowing Switch', 'Edern Sommerled', 'Yan Zal',
                           'Canthan Schoolgirl', 'Buttsneks', 'Insp Smarty Pants', 'Prof Smarty Pants',
                           'Riddle Pickle'])
        characterlist = CharacterList(data, api)
        print(characterlist[0])
        print(characterlist)

    def test_init_character_no_list(self):
        api = Gw2API(gw2_api_key)
        characterlist = CharacterList(api=api)
        self.assertIsNotNone(characterlist, msg="Character list did not initialize")
        print(characterlist)

    def test_character_get_details(self):
        api = Gw2API(gw2_api_key)
        gern = Character(name='Gern Ogrebar', api=api)
        print(gern.get_character_details())
        print(gern, gern.details)


if __name__ == '__main__':
    unittest.main()
