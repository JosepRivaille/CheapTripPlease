import requests

api_key = 'ju971847285580486099277364592013'
url = 'http://partners.api.skyscanner.net/apiservices/'
urlStatic = 'reference/v1.0/'
header = {'Accept': 'application/json', 'Content-Type': 'application/x-www-form-urlencoded'}


class SkyScan:
    locale = ''
    market = ''
    currency = ''

    def __init__(self, lang=None, country=None, currency=None):
        if lang is not None:
            self.locale = lang
        else:
            self.locale = 'en-GB'
        if country is not None:
            self.market = country
        else:
            self.market = 'ES'
        if currency is not None:
            self.currency = currency
        else:
            self.currency = 'EUR'

    # Cached, 'old', data. We can't show this data without a disclaimer or pulling live data. First, use these
    def cheapest_by_route(self, list_of_cities_dates):
        city1 = list_of_cities_dates[0]
        city2 = list_of_cities_dates[1]
        date1 = list_of_cities_dates[2]
        date2 = list_of_cities_dates[3]
        r = requests.get(url + 'browseroutes/v1.0/' + self.market + '/' + self.currency + '/'
                         + self.locale + '/' +
                         city1 + '/' + city2 + '/' + date1 + '/' + date2,
                         params={'apiKey': api_key}, headers=header)
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
            else:
                return -5
        return r.json()

    def cheapest_by_date(self, list_of_cities_dates):
        city1 = list_of_cities_dates[0]
        city2 = list_of_cities_dates[1]
        date1 = list_of_cities_dates[2]
        date2 = list_of_cities_dates[3]
        r = requests.get(url + 'browsedates/v1.0/' + self.market + '/' + self.currency + '/'
                         + self.locale + '/' +
                         city1 + '/' + city2 + '/' + date1 + '/' + date2,
                         params={'apiKey': api_key}, headers=header)
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
            else:
                return -5
        return r.json()

    def cheapest_by_quotes(self, list_of_cities_dates):
        city1 = list_of_cities_dates[0]
        city2 = list_of_cities_dates[1]
        date1 = list_of_cities_dates[2]
        date2 = list_of_cities_dates[3]
        r = requests.get(url + 'browsequotes/v1.0/' + self.market + '/' + self.currency + '/'
                         + self.locale + '/' +
                         city1 + '/' + city2 + '/' + date1 + '/' + date2,
                         params={'apiKey': api_key}, headers=header)
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
            else:
                return -5
        return r.json()


defaultScanner = SkyScan()


def get_locales():
    r = requests.get(url + urlStatic + '/locales', params={'apiKey': api_key}, headers=header)
    if r.status_code >= 400:
        # error
        print('error ' + str(r.status_code))
        if r.status_code == 400:
            return -1
        elif r.status_code == 403:
            return -2
        elif r.status_code == 429:
            return -3
        elif r.status_code == 500:
            return -4
        else:
            return -5
    return r.json()


def get_market():
    r = requests.get(url + urlStatic + 'countries/' + defaultScanner.locale, params={'apiKey': api_key}, headers=header)
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
        else:
            return -5
    return r.json()


def get_currency():
    r = requests.get(url + urlStatic + 'currencies', params={'apiKey': api_key}, headers=header)
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
        else:
            return -5
    return r.json()


def auto_suggest_location(query):
    r = requests.get(url + 'autosuggest/v1.0/' + defaultScanner.market + '/' + defaultScanner.currency + '/'
                     + defaultScanner.locale + '/', params={'query': query, 'apiKey': api_key}, headers=header)
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
        else:
            return -5
    return r.json()
