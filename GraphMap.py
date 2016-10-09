from igraph import *

class Mapper:
    g = Graph(vertex_attr= ["Destination", "Trip"],
              edge_attr= ["weights", "Carrier", "Departure", "DepStation", "ArriveStation"])
    city_list = set()
    city_first = ''
    city_last = ''
    city_num = 0
    gen = ()

    def __init__(self, city_first=None, city_last=None, city_list=None):
        if city_first is not None:
            self.city_list = city_list
            self.city_first = city_first
            self.city_last = city_last
            self.city_num = len(city_list) + 2

    def set_graph(self):
        if((not not self.city_first)and(not not self.city_last)and(not not self.city_list)and(not not self.city_num)):
            self.g.add_vertices((self.city_num-2)**2 +2) # Assuming a 1-1 ratio of cities to allotted time, only the list
            self.g.vs["Destination"] = [self.city_first, list(self.city_list) * (self.city_num-2), self.city_last]
            self.g.vs["Trip"] = [0, list(x for x in range(1,self.city_num-1)) * (self.city_num-2), self.city_num]
            return True
        return False

    def weight_edge(self, origin, dest, trip, cost, carrier, deptTime, origStation, destStation):
        def get_vertex(city, trip)
            return self.g.vs["Destination": city, "Trip": trip]
        v1 = get_vertex(origin, trip)
        v2 = get_vertex(dest, trip)
        self.g.add_edge(v1,v2,weights= cost, Carrier= carrier, Departure= deptTime,
                        DepStation= origStation, ArriveStation= destStation)

    def get_path(self):
        return self.g.shortest_paths_dijkstra(source= self.g.vs["Trip": 0], target= self.g.vs["Trip": self.city_num], mode= 'OUT')
