from skyscanner.skyscanner import Flights, FlightsCache
import requests
import json
from time import sleep

api_key = 'ju971847285580486099277364592013'
url = 'http://partners.api.skyscanner.net/apiservices/autosuggest/v1.0/'
header = {'Accept': 'application/json'}
flights_service = Flights(api_key)
flights_cache_service = FlightsCache(api_key)

class SkyScan:
    locale = ''
    market = ''
    currency = ''

    def __init__(self, lang, country, currency):
        self.locale = lang
        self.market = country
        self.currency = currency

defaultScanner = SkyScan( 'en-GB', 'ES', 'EUR')

def getLocales():
    r = requests.get( url + '/locales', params={'apiKey': api_key }, headers=header )
    if r.status_code >= 400:
        # error
        print('error' + r.status_code)
        if r.status_code == 400:
            return -1
        elif r.status_code == 403:
            return -2
        elif r.status_code == 429:
            return -3
        elif r.status_code == 500:
            return -4
    return r

def getMarket():
    r = requests.get( url + 'countries/' + defaultScanner.locale, params={'apiKey': api_key }, headers=header )
    if r.status_code >= 400:
        # error
        print('error' + r.status_code)
        if r.status_code == 400:
            return -1
        elif r.status_code == 403:
            return -2
        elif r.status_code == 429:
            return -3
        elif r.status_code == 500:
            return -4
    return r

def getCurrency():
    r = requests.get( url + 'currencies', params={'apiKey': api_key }, headers=header )
    if r.status_code >= 400:
        # error
        print('error' + r.status_code)
        if r.status_code == 400:
            return -1
        elif r.status_code == 403:
            return -2
        elif r.status_code == 429:
            return -3
        elif r.status_code == 500:
            return -4
    return r

def autoSuggestLocation( query ):
    r = requests.get( url + defaultScanner.market + '/' + defaultScanner.currency + '/' + defaultScanner.locale + '/',
                      params={ 'query': query, 'apiKey': api_key }, headers=header )
    if r.status_code >= 400:
        # error
        print('error' + r.status_code)
        if r.status_code == 400:
            return -1
        elif r.status_code == 403:
            return -2
        elif r.status_code == 429:
            return -3
        elif r.status_code == 500:
            return -4
    return r
