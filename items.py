#!/usr/bin/python3

from api import Gw2API


def get_item_information(item=None, api=None):
    assert item is not None, "Item was not defined"
    assert api is not None, "API was not defined"
    endpoint = "item"
    api.get_endpoint(endpoint + "/" + item.id)


class Item:
    def __init__(self, id: str=None, dict_id: dict=None, api: Gw2API=None):
        assert (id is not None) and (dict_id is not None), "ID and object not provided," \
                                                           " at least one is required to initialize Item"
        if id is not None:
            self.item_id = id
        if dict_id is not None:
            try:
                self.id = dict_id['id']
            except ValueError:
                raise

        self.api = api
        self.details = None
        self.information = None




class ItemList(list):
    def __init__(self, items=None):
        if id is not None:
            try:
                for item in items:
                    self.append (item)
            except ValueError:
                raise
