# class Graph:
#     def __init__(self):
#         self.adjacency_list={}

#     def add_vertex(self,vertex):
#         if vertex not in self.adjacency_list.keys():
#             self.adjacency_list[vertex]=[]
#             return True
#         return False

#     def add_edge(self,vertex1,vertex2):
#         if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
#             self.adjacency_list[vertex1].append(vertex2)
#             return True
#         return False
    

#     def print_graph(self):
#         for vertex in self.adjacency_list:
#             print(vertex,":",self.adjacency_list[vertex])

# my_graph =Graph()
# my_graph.add_vertex("A")
# my_graph.add_vertex("B")
# my_graph.add_vertex("C")
# my_graph.add_vertex("D")
# my_graph.add_vertex("E")
# my_graph.print_graph()
# my_graph.add_edge("A","B")
# my_graph.add_edge("A","C")
# my_graph.add_edge("A","D")
# my_graph.add_edge("B","A")
# my_graph.add_edge("B","C")
# my_graph.add_edge("B","D")
# my_graph.print_graph()    

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    # Add Vertex
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False

    # Add Edge
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            return True
        return False

    # Remove Edge
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            try:
                self.adjacency_list[vertex1].remove(vertex2)
                return True
            except ValueError:
                pass
        return False

    # Remove Vertex
    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():

            # Remove vertex from other lists
            for other_vertex in self.adjacency_list:
                if vertex in self.adjacency_list[other_vertex]:
                    self.adjacency_list[other_vertex].remove(vertex)

            # Delete the vertex
            del self.adjacency_list[vertex]
            return True

        return False

    # Print Graph
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])


# ---------------- MAIN ----------------

my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")

print("Vertices Added:")
my_graph.print_graph()

# Adding Edges
my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "A")
my_graph.add_edge("B", "C")
my_graph.add_edge("B", "D")

print("\nGraph After Adding Edges:")
my_graph.print_graph()

# Removing Edge
my_graph.remove_edge("A", "D")

print("\nGraph After Removing Edge A-D:")
my_graph.print_graph()

# Removing Vertex
my_graph.remove_vertex("C")

print("\nGraph After Removing Vertex C:")
my_graph.print_graph()