#cylinder
from operator import truediv


class cylinder:
    def __init__(self,radius,height,color):
        self.r=radius
        self.h=height
        self.rangi=color
    def calc_area(self,is_closed=True):
        if is_closed:
            area=2*22/7*self.r**2 + 2 * 22/7* self.r *22/7 * self.h
            print(f'area of open cylinder is: {area}')
        else:
            area = 22/7*self.r**2+2*3.14* self.r **2*22/7* self.h
            print(f'area of open cylinder is: {area}')
    def calc_volume(self):
        v=22/7*self.r**2*self.h
        print(f'volume of the cylinder is:{v}')

c1=cylinder(10,15,'blue')
c2=cylinder(12,20,'green')
c1.calc_volume()
c1.calc_area(is_closed=False)
c1.calc_area(is_closed=True)
