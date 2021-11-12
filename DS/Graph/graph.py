class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        keys = self.adj_list.keys()
        if v1 in keys and v2 in keys:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_vertex(self, vertex):
        keys = self.adj_list.keys()
        if vertex in keys:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


     
    def remove_edge(self, v1, v2):
        keys = self.adj_list.keys()
        if v1 in keys and v2 in keys:
            self.adj_list[v1].remove(v2)
            self.adj_list[v2].remove(v1)
            return True
        return False

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B') 
graph.add_vertex('C') 
graph.add_vertex('D')

graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('A', 'D')
graph.add_edge('B', 'D')
graph.add_edge('C', 'D')

graph.print_graph()

print('\n')

graph.remove_vertex('D')

graph.print_graph()
