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
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False

    def isInGraph(self, vertex):
        if vertex in self.adj_list.keys():
            return True
        else:
            return False

    def printAllConnected(self, vertex):
        if vertex in self.adj_list.keys():
            print(vertex, ':', self.adj_list[vertex])
        else:
            print('Vertex tidak ditemukan atau tidak ada')


my_graph = Graph()
my_graph.add_vertex(82)
my_graph.add_vertex(27)
my_graph.add_vertex(52)
my_graph.add_vertex(18)
my_graph.add_vertex(21)
my_graph.add_vertex(76)
my_graph.add_vertex(44)

my_graph.add_edge(82, 27)
my_graph.add_edge(27, 52)
my_graph.add_edge(52, 18)
my_graph.add_edge(18, 21)
my_graph.add_edge(18, 44)
my_graph.add_edge(21, 44)
my_graph.add_edge(21, 76)
my_graph.add_edge(76, 44)

my_graph.print_graph()

# Uji coba saat def isInGraph dijalankan


# ketika vertex yang dicari ada didalam graph
print("Vertex yang dicari : ", my_graph.isInGraph(18))

# ketika vertex yuang dicari tidak ada didalam graph
print("\nVertex yang dicari : ", my_graph.isInGraph(1))

# Uji Coba saat def printAllConeected() dijalankan


# ketika vertex yang dicari ada didalam graph
print("Koneksi dari vertex: ")
my_graph.printAllConnected(44)

# ketika vertex yang dicari tidak ada didalam graph
print("\nkoneksi dari vertex : ")
my_graph.printAllConnected(99)
