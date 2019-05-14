from BellmanFord import BellmanFord
from Edges import Edge
from Vert import Vertex
from forex_python.converter import CurrencyRates
import numpy as np

if __name__ == "__main__":
    c = CurrencyRates()
    input_string = raw_input('Enter a list of currencies: ')
    l = input_string.split()

    vertex_list = []
    for item in l:
        vertex_list.append(Vertex(item))
    
    edge_list = []
    for i in vertex_list:
        for j in vertex_list:
            if i != j:
                edge_list.append(Edge(i, j, (-1*np.log((c.get_rate(str(i), str(j)))))))
    
    algo = BellmanFord(vertex_list, edge_list)
    algo.bellman_ford(vertex_list[0])
    algo.print_cycle()
