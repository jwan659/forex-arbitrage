from Vert import Vertex
from Edges import Edge
class BellmanFord():

    def __init__(self, vertex_list, edge_list):
        self.vertex_list = vertex_list
        self.edge_list = edge_list
        self.cycle_list = list()

    def bellman_ford(self, src):
        
        src.set_min_distance(0)

        for i in range(len(self.vertex_list) - 1):
            for edge in self.edge_list:
                if (edge.get_start().get_min_distance() == float('inf')):
                    continue

                dist = edge.get_start().get_min_distance() + edge.get_weight()

                if (dist < edge.get_target().get_min_distance()):
                    edge.get_target().set_min_distance(dist)
                    edge.get_target().set_previous_vertex(edge.get_start())

        for edge in self.edge_list:
            if(edge.get_start().get_min_distance() != float('inf')):
                if(self.has_cycle(edge)):
                    vertex = edge.get_start()

                    while (vertex != edge.get_target()):
                        self.cycle_list.append(vertex)
                        vertex = vertex.get_previous_vertex()
                    
                    self.cycle_list.append(edge.get_target())

                    return
    
    def has_cycle(self, edge):
        return edge.get_target().get_min_distance() > edge.get_start().get_min_distance() + edge.get_weight()

    def print_cycle(self):
        if (self.cycle_list):
            print("An arbitrage opportunity has been detected: ")
            for vertex in self.cycle_list:
                print(vertex)
        else:
            print("No arbitrage opportunity! ")