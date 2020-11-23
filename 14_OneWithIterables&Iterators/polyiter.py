#polyiter.py

from polygons import *
from functools import namedtuple

class PolyIterable:
    '''Converting Polygon sequence into Iterator and Iterator'''
    def __init__(self, vertices, circumradius):
        self.vertices = vertices
        self.circumradius = circumradius

    def __len__(self):
        return self.vertices
    
    def __iter__(self):
        return self.PolyIterator(self.vertices, self.circumradius)
    
    def __getitem__(self, s):
        if s > self.vertices - 3 or s < 0:
            raise IndexError('Index out of scope of this problem')
        else:
            s = s + 3
            return self.PolyIterator(self.vertices, self.circumradius).area_peri_ratio(s)

    class PolyIterator():
        '''This is an iterable that is called via Iterator'''
        def __init__(self, vertices, circumradius):
            self.circumradius = circumradius
            self.vertices = vertices
            self.i = 3

        def __iter__(self):
            return self.__class__()
        
        def __next__(self):
            if self.i > self.vertices:
                raise StopIteration
            else:
                poly_tuple = self.area_peri_ratio(self.i)
                self.i += 1
                return poly_tuple
        
        def area_peri_ratio(self, vertices):
            poly_tuple = namedtuple('poly_tuple', 'Vertices AreaRatio')
            a = PolyGon(vertices, self.circumradius)
            area = a.get_area()
            perimeter = a.get_perimeter()
            return poly_tuple(Vertices= vertices,AreaRatio=(round(area/perimeter,6)))

    def __repr__(self):
        return f'Get max efficient area for Polygon of highest vertices no as {self.vertices} and circumradius {self.circumradius}'
    
    def maxefficiencypoly(self):
        polygons = []
        for i in range(self.vertices-3):
            i = i+3
            polygons.append(self.PolyIterator(self.vertices, self.circumradius).area_peri_ratio(i))
        
        return(max([(i[0],i[1]) for i in polygons]))