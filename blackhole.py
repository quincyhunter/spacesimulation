# A Black_Hole is derived from a Simulton base; it updates by finding+removing
#   any objects (derived from a Prey base) whose center is crosses inside its
#   radius (and returns a set of all eaten simultons); it displays as a black
#   circle with a radius of 10 (e.g., a width/height 20).
# Calling get_dimension for the width/height (for containment and displaying)'
#   will facilitate inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):  
    radius = 10
    
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,20,20)
        self._eaten = set()
    def update(self, food = None):
        if food == None:
            pass
        else:
            self._eaten.add(food)
        return self._eaten
    
    def display(self,canvas):
       canvas.create_oval(float(self._x)-float(self._height/2)      , float(self._y)-float(self._width/2),
                                float(self._x)+float(self._height/2), float(self._y)+float(self._width/2),
                                fill="#000000")
    
    def contains(self, xy):
        if ((self._x -xy[0])**2  + (self._y -xy[1])**2)**.5 <= float(self._height/2):
            return True
        else:
            return False
