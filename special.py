# A Special is a prey; it updates by teleporting within 20 pixels in any direction



from prey import Prey
import math,random

class Special(Prey): 
    radius = 5
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,2*math.pi*random.random(),5)
    
    def update(self):
        rand_x = random.randint(-20,20)
        rand_y = random.randint(-20,20)
        self._x += rand_x
        self._y += rand_y
        Prey.wall_bounce(self)
    
    def display(self,canvas):
       canvas.create_oval(self._x-Special.radius      , self._y-Special.radius,
                                self._x+Special.radius, self._y+Special.radius,
                                fill="#FFFFFF")