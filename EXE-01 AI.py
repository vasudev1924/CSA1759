import heapq
def manhattan_distance(state, goal):
    distance = 0
    for num in range(1, 9):
        x1, y1 = divmod(state.index(num), 3)
        x2, y2 = divmod(goal.index(num), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance
def get_neighbors(state):
    neighbors = []
    zero_pos = state.index(0)   
    row, col = divmod(zero_pos, 3)
    moves = {
        'UP': (row - 1, col),
        'DOWN': (row + 1, col),
        'LEFT': (row, col - 1),
        'RIGHT': (row, col + 1),
    }
    for move, (r, c) in moves.items():
        if 0 <= r < 3 and 0 <= c < 3:
            new_pos = r * 3 + c
            new_state = list(state)
            new_state[zero_pos], new_state[new_pos] = new_state[new_pos], new_state[zero_pos]
            neighbors.append(tuple(new_state))
    return neighbors
# A* Search algorithm
def solve_8_puzzle(start, goal):
    pq = []
    heapq.heappush(pq, (0, start))
    came_from = {start: None}
    g_cost = {start: 0}
    while pq:
        _, current = heapq.heappop(pq)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]
        for neighbor in get_neighbors(current):
            temp_g = g_cost[current] + 1
            if neighbor not in g_cost or temp_g < g_cost[neighbor]:
                g_cost[neighbor] = temp_g
                f_cost = temp_g + manhattan_distance(neighbor, goal)
                heapq.heappush(pq, (f_cost, neighbor))
                came_from[neighbor] = current
    return None
start_state = (1, 2, 3,
               4, 0, 5,
               7, 8, 6)
goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)
solution_path = solve_8_puzzle(start_state, goal_state)
print("\nSolution Steps:")
for step in solution_path:
    print(step[0:3])
    print(step[3:6])
    print(step[6:9])
    print()
