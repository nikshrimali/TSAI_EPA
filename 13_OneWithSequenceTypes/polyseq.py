#polyseq.py

# custom polygon sequence types

from polygons import PolyGon

class PolySeq:
    def __init__(self, vertices, circumradius):
        self.vertices = vertices
        self.circumradius = circumradius

    def __len__(self):
        return self.vertices

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 4 or s >=self.vertices:
                raise IndexError
            else:
                area_dict =  PolySeq._area_peri_ratio(s, self.circumradius)
                max_efficient_area = sorted(area_dict, key= lambda k: area_dict[k], reverse=True)[0]
                print(f'area/perimeter ratios {area_dict}')
                print(f'Maximum efficient polygon is of side {max_efficient_area}')
                return max_efficient_area

    def __repr__(self):
        return f'Get max efficient area for Polygon of highest vertices no as {self.vertices} and circumradius {self.circumradius}'

    @staticmethod
    def _area_peri_ratio(n, circumradius):
        i = 3
        efficiency_dict = dict()
        while (i <= n):
            a = PolyGon(i, circumradius)
            area = a.get_area()
            perimeter = a.get_perimeter()
            efficiency_dict[i] = (round(area/perimeter,6))
            i += 1
        return (efficiency_dict)