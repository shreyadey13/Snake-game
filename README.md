# 🐍 AI Snake Game with Pathfinding Algorithms

This project is an AI-powered Snake Game where the snake uses classic pathfinding and search algorithms to intelligently find its way to the food. The game visually demonstrates how different search strategies behave in a grid environment.

## 🚀 Features

- Interactive grid-based Snake Game.
- AI-controlled snake using various search algorithms:
  - Breadth-First Search (BFS)
  - Depth-First Search (DFS)
  - Uniform Cost Search (UCS)
  - Greedy Best-First Search
  - A* Search
  - Iterative Deepening Search (IDS)
- Real-time visualization of the snake's pathfinding decisions.
- Algorithm switcher to compare performances live.

## 🧠 Search Algorithms Implemented

| Algorithm               | Description                                                                 |
|------------------------|-----------------------------------------------------------------------------|
| **BFS**                | Explores all nodes level by level, guaranteeing the shortest path.          |
| **DFS**                | Explores as deep as possible before backtracking; may not find shortest.    |
| **UCS**                | Like BFS but uses a priority queue to find lowest-cost paths.               |
| **Greedy BFS**         | Uses a heuristic (e.g., Manhattan distance) to move toward the goal faster. |
| **A\***                | Combines UCS and Greedy BFS for optimal and efficient search.               |
| **IDS**                | Repeated DFS with increasing depth, combining advantages of BFS and DFS.    |

## 🛠️ Tech Stack

- **Language**: Python (or specify your language)
- **Libraries**: 
  - `pygame` (for GUI and game loop)
  - `heapq` or custom priority queues (for UCS and A*)
  - `collections.deque` (for BFS)
  - `math`, `time`, etc.

## 📁 Project Structure

```plaintext
├── snake_ai_game/
│   ├── main.py
│   ├── game.py
│   ├── algorithms/
│   │   ├── bfs.py
│   │   ├── dfs.py
│   │   ├── ucs.py
│   │   ├── greedy_bfs.py
│   │   ├── astar.py
│   │   └── ids.py
│   ├── utils.py
│   └── assets/
│       └── ...
├── README.md
└── requirements.txt
