from scheme import Scheme

class Node():
    
    def __init__(self, x, y):
        self.position = x, y
        self.end = Scheme().end
        self.start = Scheme().start
        self.costs = self.calc_costs()

    def calc_costs(self):
        # g(n) cost = from staring node cost
        g = self.calc_distance(*self.position, *self.start)

        # h(n) cost = heuristics estimated cost
        h = self.calc_distance(*self.position, *self.end)

        # f(n) cost = g(n) + h(n) 
        f = g + h

        return (f, h, g)  

    def calc_distance(self, x, y, x2, y2):
        # calculate estimated distance between two points
        return abs((x2-x) + (y2-y))
