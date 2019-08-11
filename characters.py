#!/usr/bin/python3

from api import Gw2API
import urllib


class Character:
    def __init__(self, name='', api=None):
        assert type(name) == str, "Name provided was not a string, value provided was: " + str(name)
        assert api is not None, "API not provided for character creation, required for any get details operations"
        self.name = name
        assert isinstance(api, Gw2API)
        self.api = api

        # holding off defining details until it is required
        self.details = None

    def __str__(self):
        return self.name

    def get_character_details(self):
        self.details = self.api.get_endpoint('characters/' + urllib.parse.quote(self.name))
        return self.details

    def get_character_inventory(self):
        if self.details is None:
            self.get_character_details()

    def get_full_character_inventory(self):
        assert self.api is not None, "API not provided"
        if self.details is None:
            self.get_character_details()

        data = self.get_character_details()
        for item in data['Equipment']:
            pass
        for item in data['']:
            pass

# todo: define inventory


def get_characters_using_api(api):
    characters = api.get_endpoint ('characters')
    return characters


class CharacterList (list):
    def __init__(self, characters=None, api=None):
        """

        :param characters: List of character names
        :param api: api object
        """
        super(CharacterList, self).__init__()
        if characters is None:
            assert api is not None, "No characters or API provided"
            characters = get_characters_using_api(api)

        assert type (
            characters) == list, 'Function either did not receive a list or was unable to get list using the API ' \
                                 ' initialization was not a list, instead it got a: ' \
                                 + str (type (characters))
        for character in characters:
            assert type (
                character) == str, "When adding characters from the given list one of them was not a string instead " \
                                   "it was: " + str (type (character)) + " with content: " + str (character)
            self.append (Character (character, api=api))

# todo: define init case for no provided list
# todo: define iterable interfaces, but should inherit from List
# todo: define string output to better handle displaying object
