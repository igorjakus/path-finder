from scheme import Scheme
from node import Node

start = Scheme().start
end = Scheme().end


class A_Star:

    def __init__(self):
        self.nodes = []

    def find_path(self):
        # Find correct shortest path by A* algorithm

        # If there's any node in nodes list set point
        # as position of node that has smallest costs
        # if there's no -> set point as start poisition
        for __ in range(2):
            point = self.nodes[0].position if self.nodes else start

            for position in self.nearest_moves(point):
                self.nodes.append(Node(*position))

            self.delete_duplicates()
            self.sort_nodes()

    def delete_duplicates(self):
        # Delete nodes duplicates
        while value := self.is_there_duplicate():
            self.nodes.remove(value)

    def is_there_duplicate(self):
        # when there's no duplicate in nodes list
        # return False, when there is return it
        seen = []
        for x in self.nodes:
            if x.position in seen:
                return x
            else:
                seen.append(x.position)
        return False

    def sort_nodes(self):
        # Sort nodes by costs so first in list
        # will be that node that has smallest cost:)
        self.nodes.sort(key=lambda node: node.costs)

    def nearest_moves(self, position):
        # Return nearest possible list of moves for pointed node
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        return [self.moved_position(position, move) for move in moves]

    @staticmethod
    def moved_position(pos, move):
        # Return moved position (sum of two tuples)
        return tuple(pos + move for pos, move in zip(pos, move))

    def printme(self):
        # Just for test in developing:)
        for n in self.nodes:
            print(n.position, n.costs)


x = A_Star()
x.find_path()
x.printme()
