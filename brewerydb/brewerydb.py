# -*- coding: utf-8 -*-

__author__ = 'Derek Stegelman'

import json
import requests
import urllib

from .beer import Beer, Beers

BASE_URL = 'http://api.brewerydb.com/v2'


class BreweryDB(object):
    def __init__(self, api_key):
        self.api_key = api_key
        
    def _auth(self):
        return "key=%s" % self.api_key
        
    def _call(self, resource_url, params=None):
        url = "%s/%s" % (BASE_URL, resource_url)
        
        if params:
            url += "?%s&%s" % (params, self._auth())
        else:
            url += "?%s" % self._auth()
        
        return requests.get(url)
    
    def _params(self, params):
        """
        Takes dictionary of parameters and returns
        urlencoded string

        :param params: Dict of query params to encode
        :type params: dict
        
        :returns:  str -- URL encoded query parameters
        """
        return urllib.urlencode(params)
    
    def search_beer(self, beer_name):
        response = json.loads(self._call(Beers.resource_url, self._params(params={'name': beer_name})).text)
        beers = []
        for beer in response['data']:
            beers.append(Beers(beer))
        return beers
        
    def get_beer(self, id):
        response = json.loads(self._call("%s/%s" % (Beer.resource_url, id), self._params({'withBreweries': 'Y'})).text)
        return Beer(response['data'])
    
    def get_brewery(self, id):
        return