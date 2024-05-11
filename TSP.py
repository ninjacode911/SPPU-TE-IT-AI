def solve(graph, start_city):
    num_cities = len(graph)
    visited = [False] * num_cities
    path = [start_city]
    
    curr_city = start_city
    visited[start_city] = True
    total_distance = 0
    
    min_distance = float('inf')
    
    for _ in range(num_cities - 1):
        min_distance = float('inf')
        near_city = None
        
        for city in range(num_cities):
            if not visited[city] and graph[curr_city][city] < min_distance:
                min_distance = graph[curr_city][city]
                near_city = city
        
        path.append(near_city)
        visited[near_city] = True
        total_distance += min_distance
        curr_city = near_city
        
    total_distance += graph[path[-1]][start_city]
    path.append(start_city)
    return path, total_distance    
    

if __name__ == "__main__":
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    start_city = 0
    
    shortest_path, min_distance = solve(graph, start_city)
    print("Shortest Path : ", shortest_path)
    print("Min Distance : ", min_distance)