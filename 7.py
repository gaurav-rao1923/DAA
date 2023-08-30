import itertools
 2 
 
 3 
 
def calculate_distance(x1, y1, x2, y2):
 4 
 
    # Calculate Euclidean distance between two points
 5 
 
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
 6 
 
 7 
 
def calculate_total_distance(points_order, distances):
 8 
 
    # Calculate the total distance for a given order of points
 9 
 
    total_distance = 0
 10 
 
    num_points = len(points_order)
 11 
 
    for i in range(num_points - 1):
 12 
 
        point1 = points_order[i]
 13 
 
        point2 = points_order[i + 1]
 14 
 
        total_distance += distances[point1][point2]
 15 
 
    return total_distance
 16 
 
 17 
 
def find_optimal_drilling_time(points, toolbox_time):
 18 
 
    num_points = len(points)
 19 
 
    distances = [[0] * num_points for _ in range(num_points)]
 20 
 
 21 
 
    # Calculate distances between all pairs of points
 22 
 
    for i in range(num_points):
 23 
 
        x1, y1, d1 = points[i]
 24 
 
        for j in range(num_points):
 25 
 
            x2, y2, d2 = points[j]
 26 
 
            distances[i][j] = calculate_distance(x1, y1, x2, y2)
 27 
 
 28 
 
    # Generate all possible permutations of points
 29 
 
    point_permutations = list(itertools.permutations(range(num_points)))
 30 
 
 31 
 
    # Initialize optimal drilling time to a large value
 32 
 
    optimal_drilling_time = float('inf')
 33 
 
 34 
 
    # Find the optimal drilling time
 35 
 
    for permutation in point_permutations:
 36 
 
        total_distance = calculate_total_distance(permutation, distances)
 37 
 
        drilling_time = total_distance + (num_points - 1) * toolbox_time
 38 
 
        if drilling_time < optimal_drilling_time:
 39 
 
            optimal_drilling_time = drilling_time
 40 
 
 41 
 
    return optimal_drilling_time
 42 
 
 43 
 
def main():
 44 
 
    # Example usage
 45 
 
    points = [(0, 0, 1), (3, 0, 2), (0, 4, 1), (3, 4, 2)]  # (x, y, diameter) of each hole
 46 
 
    toolbox_time = 5  # Time required to change the drill at the toolbox
 47 
 
    optimal_time = find_optimal_drilling_time(points, toolbox_time)
 48 
 
    print("Optimal Drilling Time:", optimal_time)
 49 
 
 50 
 
if __name__ == "__main__":
 51 
 
    main()
