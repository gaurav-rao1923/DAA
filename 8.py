from collections import defaultdict
 2 
 
 3 
 
class Graph:
 4 
 
    def __init__(self):
 5 
 
        self.graph = defaultdict(list)
 6 
 
    
 7 
 
    def add_edge(self, u, v):
 8 
 
        self.graph[u].append(v)
 9 
 
        self.graph[v].append(u)
 10 
 
    
 11 
 
    def is_safe(self, v, color, c):
 12 
 
        for neighbor in self.graph[v]:
 13 
 
            if color[neighbor] == c:
 14 
 
                return False
 15 
 
        return True
 16 
 
    
 17 
 
    def graph_coloring(self):
 18 
 
        num_vertices = len(self.graph)
 19 
 
        color = [-1] * num_vertices
 20 
 
        
 21 
 
        # Function to assign colors recursively
 22 
 
        def assign_colors(v):
 23 
 
            if v == num_vertices:
 24 
 
                return True
 25 
 
            for c in range(1, num_vertices + 1):
 26 
 
                if self.is_safe(v, color, c):
 27 
 
                    color[v] = c
 28 
 
                    if assign_colors(v + 1):
 29 
 
                        return True
 30 
 
                    color[v] = -1
 31 
 
        assign_colors(0)
 32 
 
        return max(color)
 33 
 
 34 
 
def calculate_min_time_slots(subjects):
 35 
 
    graph = Graph()
 36 
 
    
 37 
 
    # Create a graph with subjects as vertices and common students as edges
 38 
 
    for i in range(len(subjects)):
 39 
 
        for j in range(i + 1, len(subjects)):
 40 
 
            if len(set(subjects[i]) & set(subjects[j])) > 0:
 41 
 
                graph.add_edge(i, j)
 42 
 
    
 43 
 
    min_time_slots = graph.graph_coloring()
 44 
 
    return min_time_slots
 45 
 
 46 
 
def main():
 47 
 
    # Example usage
 48 
 
    subjects = [
 49 
 
        ["Alice", "Bob", "Charlie"],
 50 
 
        ["Bob", "David"],
 51 
 
        ["Charlie", "Eve", "Frank"],
 52 
 
        ["David", "Frank"]
 53 
 
    ]
 54 
 
    min_time_slots = calculate_min_time_slots(subjects)
 55 
 
    print("Minimum Time Slots:", min_time_slots)
 56 
 
 57 
 
if __name__ == "__main__":
 58 
 
    main()
 59 

