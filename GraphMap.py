from igraph import *


class Mapper:
    g = Graph()
    city_list = set()
    city_first = ''
    city_last = ''
    city_num = 0

    def __init__(self, city_first=None, city_last=None, city_list=None):
        if city_first is not None:
            self.city_list = city_list
            self.city_first = city_first
            self.city_last = city_last
            self.city_num = len(city_list) + 2

    def set_graph(self):
        if((not not self.city_first)and(not not self.city_last)and(not not self.city_list)and(not not self.city_num)):
            self.g.add_vertices(self.city_num)
            self.g.vs["Airport"] = [self.city_first, self.city_list, self.city_last]
            return True
        return False

    def weight_edges(self):
        # Weight the first city to the rest
        for i in self.city_list:
            self.g.add_edge((0, i))
            self.g.es[self.g.get_eid(0, i)]["weight"] = 0 # Get skyscanner cost
        # Weight the last city to the rest
        for i in self.city_list:
            self.g.add_edge((i, self.city_num - 1))
            self.g.es[self.g.get_eid(i, self.city_num - 1)]["weight"] = 0  # Get skyscanner cost
