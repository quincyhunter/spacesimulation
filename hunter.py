# A Hunter class is derived from a Pulsator and then Mobile_Simulton base.
#   It inherits updating+displaying from Pusator/Mobile_Simulton: it pursues
#   any close prey, or moves in a straight line (see Mobile_Simultion).


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2
import math,random

class Hunter(Pulsator, Mobile_Simulton):  
    distance = 200
    
    def __init__(self,x,y):
        Pulsator.__init__(self,x,y)
        self._speed = 5
        self._angle = 2*math.pi*random.random()
        print(self._counter)
    def update(self, food = None):
        if food == None:
            self._counter +=1
            if self._counter == Pulsator.counter_constant:
                self._counter = 0
                self._width -=1
                self._height -=1
        else:
            self._counter = 1
            self._width += 1
            self._height +=1
            self._eaten.add(food)
        self._x += self._speed*math.cos(self._angle)
        self._y += self._speed*math.sin(self._angle)        
        Mobile_Simulton.wall_bounce(self)
    def close(self,prey):
        if Mobile_Simulton.distance(self, [prey._x,prey._y]) <= Hunter.distance:
            return Mobile_Simulton.distance(self,[prey._x,prey._y])
        else:
            return False
    
    