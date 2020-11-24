#polygon.py

import math

class PolyGon:
    def __init__(self, edges=None, circumradius=None):
        self.edges = edges
        self.circumradius = circumradius
    def get_interior_angle(self):
        self.interior_angle = (self.edges - 2)*(180/self.edges)
        return self.interior_angle
    def get_edgelength(self):
        self.edge_length = 2*self.circumradius*(math.sin(math.pi/self.edges))
        return self.edge_length
    def get_apothem(self):
        self.apothem = self.circumradius*(math.cos(math.pi/self.edges))
        return self.apothem
    def get_area(self):
        '''Calcuates the area of a regular polygon for\
            no of sides of side_length'''
        edge_length = self.get_edgelength()
        apothem = self.get_apothem()
        self.area =  1/2*(edge_length*self.edges*apothem)
        return round(self.area,2)
    def get_perimeter(self):
        self.perimeter = self.edge_length*self.area
        return self.perimeter

    def __eq__(self, other):
        if isinstance(other,PolyGon):
            if self.edges == other.edges and self.circumradius == other.circumradius:
                return True
            else:
                return False
        else:
            raise ValueError('Only Polygon objects can be compared')

    def __gt__(self, other):
        if isinstance(other,PolyGon):
            if self.edges > other.edges:
                return True
            else:
                return False
        else:
            raise ValueError('Only Polygon objects can be compared')
    
    def __repr__(self):
        return f'A polygon of side {self.edges} and circumradius {self.circumradius}'