import SkyScannerIO as ss
import GraphMap as gm
from datetime import date, datetime
from itertools import *

class ArrangementHandler:
    # Initiate instance specific usages
    search_instance = gm.Mapper
    scanner = ss.SkyScan
    ready = False

    # Define parameters assumed, used for limitations, and given by user
    min_days_between_flights = 2
    range_of_search_days = 2

    day_first = ''#to be filled with real data later
    day_last = ''
    days_tot = 0

    # Define structures of sorting & providing resources to the graph
    def new_search(self):
        self.search_instance = gm.Mapper

    def set_first_city(self, id):
        self.search_instance.city_first = id

    def set_last_city(self, id):
        self.search_instance.city_last = id

    def set_city_list(self, *arguments):
        self.search_instance.city_list = arguments
        self.search_instance.city_num = len(arguments) + 2

    def set_first_day(self, d):
        self.day_first = d
        if (not not self.day_last) and (
            (datetime.strptime(self.day_last,"%Y%m%d") - datetime.strftime(self.day_first,"%Y%m%d")) > 0):
            self.days_tot = datetime.strptime(self.day_last,"%Y%m%d") - datetime.strftime(self.day_first,"%Y%m%d")

    def set_last_day(self, d):
        self.day_last = d
        if (not not self.day_first) and (
            (datetime.strptime(self.day_last, "%Y%m%d") - datetime.strftime(self.day_first, "%Y%m%d")) > 0):
            self.days_tot = datetime.strptime(self.day_last, "%Y%m%d") - datetime.strftime(self.day_first, "%Y%m%d")

    #Create lists of lists of possibilities

    def ninjagecko_combinations(items):
        return (set(compress(items, mask)) for mask in product(*[[0, 1]] * len(items)))

    def run_algorithms(self):
        if(all([not not self.day_first, not not self.day_last, not not self.days_tot])):
            return False
        if not(self.ready or self.search_instance.set_graph()):
            return False
        else:
            ready = True
        poss = [self.ninjagecko_combinations(self.search_instance.city_list)]
        for i in poss:
            poss[i].insert[0,self.search_instance.city_first]
            poss[i].extend[self.search_instance.city_last]
