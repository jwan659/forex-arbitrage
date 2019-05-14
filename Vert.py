import sys
from Edges import Edge
class Vertex():

    def __init__(self, id):
        self.min_distance = float('inf')
        self.id = id
        self.adjacencies = list()

    def get_min_distance(self):
        return self.min_distance

    def set_min_distance(self, distance):
        self.min_distance = distance

    def get_previous_vertex(self):
        return self.prev_vertex
    
    def add_edge(self, edge):
        self.adjacencies.add(edge)

    def get_adjacencies(self):
        return self.adjacencies
    
    def set_previous_vertex(self, prev_vertex):
        self.prev_vertex = prev_vertex
    
    def is_visited(self):
        return self.visited

    def set_visited(self, visited):
        self.visited = visited

    def __str__(self):
        return self.id