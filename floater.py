# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage 


from prey import Prey
import math,random

class Floater(Prey): 
    radius = 5
    
    def __init__(self,x,y):
        Prey.__init__(self,x,y,10,10,2*math.pi*random.random(),5)
    
    def update(self):
        chance = random.randint(1,10)
        if chance <= 3:
            new_speed = random.randint(-5,5) *.1
            self._speed += new_speed
            if self._speed > 7:
                self._speed = 7
            elif self._speed < 3:
                self._speed = 3
            new_angle = random.randint(-5,5) *.1
            self._angle += new_angle
            self._x += self._speed*math.cos(self._angle)
            self._y += self._speed*math.sin(self._angle)
            Prey.wall_bounce(self)
        else:
            self._x += self._speed*math.cos(self._angle)
            self._y += self._speed*math.sin(self._angle)
            Prey.wall_bounce(self)
    
    def display(self,canvas):
       canvas.create_oval(self._x-Floater.radius      , self._y-Floater.radius,
                                self._x+Floater.radius, self._y+Floater.radius,
                                fill="#FF0000")
       