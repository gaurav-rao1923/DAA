import sys
 2 
 
 3 
 
class Graph:
 4 
 
    def __init__(self, num_vertices):
 5 
 
        self.num_vertices = num_vertices
 6 
 
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]
 7 
 
 8 
 
    def add_edge(self, src, dest, weight):
 9 
 
        self.graph[src][dest] = weight
 10 
 
        self.graph[dest][src] = weight
 11 
 
 12 
 
    def print_mst(self, parent):
 13 
 
        print("Minimum Spanning Tree (MST):")
 14 
 
        total_cost = 0
 15 
 
        for v in range(1, self.num_vertices):
 16 
 
            print(f"Edge: {parent[v]} - {v}, Weight: {self.graph[v][parent[v]]}")
 17 
 
            total_cost += self.graph[v][parent[v]]
 18 
 
        print(f"Total Cost: {total_cost}")
 19 
 
 20 
 
    def find_min_key(self, key, mst_set):
 21 
 
        min_key = sys.maxsize
 22 
 
        min_index = -1
 23 
 
        for v in range(self.num_vertices):
 24 
 
            if key[v] < min_key and not mst_set[v]:
 25 
 
                min_key = key[v]
 26 
 
                min_index = v
 27 
 
        return min_index
 28 
 
 29 
 
    def prim_mst(self):
 30 
 
        key = [sys.maxsize] * self.num_vertices
 31 
 
        parent = [None] * self.num_vertices
 32 
 
        key[0] = 0
 33 
 
        mst_set = [False] * self.num_vertices
 34 
 
        parent[0] = -1
 35 
 
 36 
 
        for _ in range(self.num_vertices):
 37 
 
            u = self.find_min_key(key, mst_set)
 38 
 
            mst_set[u] = True
 39 
 
            for v in range(self.num_vertices):
 40 
 
                if self.graph[u][v] > 0 and not mst_set[v] and self.graph[u][v] < key[v]:
 41 
 
                    key[v] = self.graph[u][v]
 42 
 
                    parent[v] = u
 43 
 
        self.print_mst(parent)
 44 
 
 45 
 
# Example usage
 46 
 
g = Graph(5)  # Create a graph with 5 vertices
 47 
 
# Add edges to the graph (source, destination, weight)
 48 
 
g.add_edge(0, 1, 2)
 49 
 
g.add_edge(0, 3, 6)
 50 
 
g.add_edge(1, 2, 3)
 51 
 
g.add_edge(1, 3, 8)
 52 
 
g.add_edge(1, 4, 5)
 53 
 
g.add_edge(2, 4, 7)
 54 
 
g.add_edge(3, 4, 9)
 55 
 
g.prim_mst()
 56 

