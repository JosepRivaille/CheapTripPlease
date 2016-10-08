import SkyScannerIO as ss
import GraphMap as gm

class ArrangementHandler:
    # Initiate instance specific usages
    search_instance = gm.Mapper

    # Define parameters assumed, used for limitations, and given by user
    min_days_between_flights = 2
    

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

