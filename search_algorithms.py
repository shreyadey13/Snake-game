import random
import heapq
from collections import deque
import math

# Directions (Up, Down, Left, Right)
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# Random movement algorithm (limited moves)
def random_move(start, goal, obstacles, rows, cols):
    path = []
    current = start

    for _ in range(1000):  # Limit to 1000 moves
        direction = random.choice(DIRECTIONS)
        new_pos = (current[0] + direction[0], current[1] + direction[1])

        if (
            0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
            new_pos not in obstacles
        ):
            path.append(direction)
            current = new_pos

        if current == goal:
            return path

    return []  # If it takes too long, return empty path


# Write your code below this only

# Breadth First Search (BFS) Algorithm
def bfs(start, goal, obstacles, rows, cols):
    queue = deque([(start, [])])
    visited = set()
    
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        if (x, y) == goal:
            return path
        
        for dx, dy in DIRECTIONS:
            new_pos = (x + dx, y + dy)
            if (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                    new_pos not in obstacles and new_pos not in visited):
                queue.append((new_pos, path + [(dx, dy)]))
    
    return []

# Depth First Search (DFS) Algorithm
def dfs(start, goal, obstacles, rows, cols):
    stack = [(start, [])]
    visited = set()
    
    while stack:
        (x, y), path = stack.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        if (x, y) == goal:
            return path
        
        for dx, dy in DIRECTIONS:
            new_pos = (x + dx, y + dy)
            if (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                    new_pos not in obstacles and new_pos not in visited):
                stack.append((new_pos, path + [(dx, dy)]))
    
    return []

# Iterative Deepening Search (IDS Algorithm
def ids(start, goal, obstacles, rows, cols):
    def dls(node, depth, path):
        if depth == 0 and node == goal:
            return path
        if depth > 0:
            x, y = node
            for dx, dy in DIRECTIONS:
                new_pos = (x + dx, y + dy)
                if (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                        new_pos not in obstacles and new_pos not in path):
                    result = dls(new_pos, depth - 1, path + [(dx, dy)])
                    if result:
                        return result
        return None
    
    depth = 0
    while True:
        result = dls(start, depth, [])
        if result:
            return result
        depth += 1

# Uniform Cost Search (UCS) Algorithm
def ucs(start, goal, obstacles, rows, cols):
    pq = [(0, start, [])]
    visited = set()
    
    while pq:
        cost, (x, y), path = heapq.heappop(pq)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        if (x, y) == goal:
            return path
        
        for dx, dy in DIRECTIONS:
            new_pos = (x + dx, y + dy)
            if (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                    new_pos not in obstacles and new_pos not in visited):
                heapq.heappush(pq, (cost + 1, new_pos, path + [(dx, dy)]))
    
    return []

#Manhattan Distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# #Euclidean Distance- Between (A* & Greedy) greedy algorithm performs better using this heuristic value
# def heuristic(a, b):
#     return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# ##Manhattan + Flood-Fill.....- Between (A* & Greedy) A* algorithm performs better using this heuristic value

# def flood_fill_heuristic(start, goal, obstacles, rows, cols):
#     queue = deque([(start, 0)])  # (position, distance)
#     visited = set(obstacles)  # Treat obstacles as visited
#     visited.add(start)

#     while queue:
#         (x, y), dist = queue.popleft()
#         if (x, y) == goal:
#             return dist  # Return the shortest path distance to goal

#         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Up, Down, Left, Right
#             new_pos = (x + dx, y + dy)
#             if (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and new_pos not in visited):
#                 visited.add(new_pos)
#                 queue.append((new_pos, dist + 1))

#     return float('inf')  # If goal is unreachable, return infinity



# Greedy Best First Search Algorithm
def greedy_bfs(start, goal, obstacles, rows, cols):
    pq = [(heuristic(start, goal), start, [])]
    # pq = [(flood_fill_heuristic(start, goal, obstacles, rows, cols), start, [])]  # Updated Heuristic
    visited = set()
    
    while pq:
        _, (x, y), path = heapq.heappop(pq)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        if (x, y) == goal:
            return path
        
        for dx, dy in DIRECTIONS:
            new_pos = (x + dx, y + dy)
            if (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and new_pos not in obstacles and new_pos not in visited):
                heapq.heappush(pq, (heuristic(new_pos, goal), new_pos, path + [(dx, dy)]))
                # heapq.heappush(pq, (flood_fill_heuristic(new_pos, goal, obstacles, rows, cols), new_pos, path + [(dx, dy)]))

    
    return []

# A* Search Algorithm
def astar(start, goal, obstacles, rows, cols):
    pq = [(heuristic(start, goal), 0, start, [])]
    # pq = [(flood_fill_heuristic(start, goal, obstacles, rows, cols), 0, start, [])]  # Updated Heuristic

    visited = set()
    
    while pq:
        _, cost, (x, y), path = heapq.heappop(pq)
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        if (x, y) == goal:
            return path
        
        for dx, dy in DIRECTIONS:
            new_pos = (x + dx, y + dy)
            if (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                    new_pos not in obstacles and new_pos not in visited):
                g = cost + 1
                f = g + heuristic(new_pos, goal)
                # f = g + flood_fill_heuristic(new_pos, goal, obstacles, rows, cols)
                heapq.heappush(pq, (f, g, new_pos, path + [(dx, dy)]))
    
    return []