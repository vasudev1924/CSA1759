import heapq

def astar(graph, heuristic, start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    
    parent = {start: None}
    g_cost = {start: 0}

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor, cost in graph[current]:
            temp_g = g_cost[current] + cost

            if neighbor not in g_cost or temp_g < g_cost[neighbor]:
                g_cost[neighbor] = temp_g
                f_cost = temp_g + heuristic[neighbor]
                heapq.heappush(pq, (f_cost, neighbor))
                parent[neighbor] = current

    return None


# MAIN PROGRAM
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 1)],
    'E': [('G', 2)],
    'F': [('G', 5)],
    'G': []
}

# Heuristic values (h(n))
heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 2,
    'E': 3,
    'F': 6,
    'G': 0
}

start = 'A'
goal = 'G'

solution = astar(graph, heuristic, start, goal)

print("A* Path:", solution)
