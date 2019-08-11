#!/usr/bin/python3

import requests
import os


class Gw2API:
    """
    TODO: change to implementation of requests, this way we can claim it as a specific implementation of requests
        override .get to our own needs while still mostly using the requests implementation and its children 🤯🤯

    """

    def __init__(self, apikey=None):
        # assert os.environ['gw2apikey'], 'gw2apikey not set, please set a gw2apikey environment variable'
        assert apikey is not None, 'apikey was not provided not set'
        self.url = 'https://api.guildwars2.com/'
        self.version = 'v2'
        self.apikey = os.environ['gw2apikey']
        self.authorization = {'Authorization': 'Bearer ' + self.apikey}

    def get_endpoint(self, endpoint: str = '') -> object:
        assert type(endpoint) == str, "Endpoint provided was not a string"
        uri = self.url + self.version + '/' + endpoint
        try:
            # TODO: rewrite to use requests builtin authorization functionality or override auth object to add bearer
            #  functionality
            request = requests.get (uri, headers=self.authorization)
        except ConnectionError:
            print ('A connection error has occurred. Status: ' + request.status_code + ': ' + request.reason)
            raise
        except TimeoutError:
            print(
                'There was a connection timeout when trying to reach this endpoint. '
                'Either it is unable to connect or the server took too long to respond')
            raise

        try:
            return request.json ()
        except ValueError:
            print ('Response is not valid json, dumping contents')
            print (request.text)
            raise
