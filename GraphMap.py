from igraph import *
import SkyScannerIO

class mapper:
    g = Graph()
    cityList = []
    cityFirst = []
    cityLast = []
    cityNum = 0

    def __init__(self, cityList, cityFirst, cityLast):
        self.cityList = cityList
        self.cityFirst = cityFirst
        self.cityLast = cityLast
        self.cityNum = len(cityList) + 2
        g.add_vertices( self.cityNum )
        g.vs["Airport"] = [cityFirst, cityList, cityLast]

    def weightEdges(self):
        # Weight the first city to the rest
        for i in self.cityList:
            g.add_edge( (0, i) )
            g.es[ g.get_eid(0, i) ]["weight"] = 0 # Get skyscanner cost
        # Weight the last city to the rest
        for i in self.cityList:
            g.add_edge( ( i, self.cityNum - 1 ) )
            g.es[g.get_eid( i, self.cityNum - 1 )]["weight"] = 0  # Get skyscanner cost
    

