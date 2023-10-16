# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions 


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    counter_constant = 30
    
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self._counter = 0
        self._eaten = set()
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
        return self._eaten
            