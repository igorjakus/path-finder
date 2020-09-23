from scheme import Scheme


start = Scheme().start
end = Scheme().end


class Node:

    def __init__(self, x, y):
        self.position = x, y
        self.costs = self.calc_costs()

    def calc_costs(self):
        # g(n) cost = from staring node cost
        g = self.calc_distance(*self.position, *start)

        # h(n) cost = heuristics estimated cost
        h = self.calc_distance(*self.position, *end)

        # f(n) cost = g(n) + h(n)
        f = g + h

        return (f, h, g)

    def calc_distance(self, x, y, x2, y2):
        # calculate estimated distance between two points
        return abs((x2-x) + (y2-y))
