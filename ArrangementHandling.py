import SkyScannerIO as ss
import GraphMap as gm
from datetime import *
import json

class Day(date):
    def __init__(self, dd, mm, yyyy):
        date_date = date(yyyy,mm,dd)
        date_str = date_date.isoformat()

class ArrangementHandler:
    # Initiate instance specific usages
    search_instance = gm.Mapper
    scanner = ss.SkyScan
    ready = False

    # Define parameters assumed, used for limitations, and given by user
    min_days_between_flights = 2
    range_of_search_days = 2

    day_first = []
    day_last = []
    days_tot = 0
    days_av = 0

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

    def generate_travel_dates(self):
        my_list = []
        for i in range(1,self.search_instance.city_num-1):
            my_list.append(list(self.day_first.date_date + datetime.timedelta(days= x + i*self.days_av)
                                for x in range(-self.range_of_search_days,self.range_of_search_days)))
        my_list.insert(0,list(self.day_first.date_date + datetime.timedelta(days= x)
                              for x in range(0,self.range_of_search_days)))
        my_list.append(list(self.day_last + datetime.timedelta(days= x)
                            for x in range(-self.range_of_search_days, 0)))
        return my_list

    def __init__(self, bundle_days_orig_dest_citiesset):
        self.day_first = Day(*bundle_days_orig_dest_citiesset[0])
        self.day_last = Day(*bundle_days_orig_dest_citiesset[1])
        self.days_tot = (self.day_last.date_date-self.day_first.date_date).days
        self.set_first_city(bundle_days_orig_dest_citiesset[2])
        self.set_last_city(bundle_days_orig_dest_citiesset[3])
        self.set_city_list(bundle_days_orig_dest_citiesset[4:])
        self.days_av = self.days_tot // (self.search_instance.city_num-2)
        if self.days_av <= self.range_of_search_days:
            self.range_of_search_days = self.days_av - 1
        ready = self.search_instance.set_graph()

    #Create Lists of Lists of possibilities, n! amount and find the
    def run_algorithms(self):
        if(all([not not self.day_first, not not self.day_last, not not self.days_tot])):
            return False
        if not(self.ready or self.search_instance.set_graph()):
            return False
        else:
            ready = True
        dates = self.generate_travel_dates()
        for trip in range(1, self.search_instance.city_num - 2):
            for origin in range(1, self.search_instance.city_num):
                for dest in range(1, self.search_instance.city_num):
                    if origin is not dest:
                        data_json = json.load(self.scanner.cheapest_by_route(
                            city1=origin,city2=dest,date1=(dates[trip][self.range_of_search_days]).isoformat()))
                        self.search_instance.weight_edge(self,origin, dest, trip,
                                                         data_json['Quotes'][0]['MinPrice'],
                                                         data_json['Quotes'][0]['DepartureDate'],
                                                         data_json['Carriers'][0]['Name'],
                                                         data_json['Places'][1]['SkyscannerCode'],
                                                         data_json['Places'][0]['SkyscannerCode'])
        # Exit loops. All edges weighted & all calls to skyscanner made
        out_path = self.search_instance.get_path()
