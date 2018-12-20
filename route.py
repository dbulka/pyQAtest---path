from point import Point
import math
from interface import Interface

class Route:
    """
    calculate route
    """

    def __init__(self):
        """initialize route"""

    def make_sheet(self, coordinates):
        """get x,y value of point"""
        self.x = point.x
        self.y = point.y

    def calcutate_formula(self):
        """formula for calculating"""
        route = 0
        # cycle for making
        for i in range(0,len(self.x)):
            if i == 0:
                point_a = Point(0,0)
                point_b = Point(self.x[i],self.y[i])
                route_formula(point_a, point_b)
            else:
                point_a = Point(self.x[i-1],self.y[i-1])
                point_b = Point(self.x[i],self.y[i])
                route_formula(point_a, point_b)
        print(interface.route)

    def route_formula(self,point_a, point_b):
        self.lenth = math.sqrt((point_a.x-point_b.x)**2+(point_a.y-point_b.y)**2)
        self.route += self.lenth
        print(interface.lenth)
        print(interface.route)
        return route

interface = Interface()
point = Point()
calc_route = Route()
calc_route.make_sheet(point.main())
calc_route.calcutate_formula()


