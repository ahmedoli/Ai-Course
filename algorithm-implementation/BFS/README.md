# 🔄 Breadth-First Search (BFS) in C++

This project implements the **Breadth-First Search (BFS)** algorithm in C++. BFS is one of the most fundamental and widely used **graph traversal** algorithms. This implementation finds the **shortest path** (in terms of number of edges) between a given start and goal node in a graph.

---

## 🚀 How the Algorithm Works

**Breadth-First Search (BFS)** explores a graph layer by layer (or level by level), starting from the source node and visiting all its neighbors before moving on to their neighbors.

### 🧠 Algorithm Steps:
1. Initialize a **queue** with the path containing the `start` node.
2. Use a **set** to track `visited` nodes.
3. Repeat while the queue is not empty:
   - Dequeue the front path.
   - Get the last node of that path.
   - If it's the goal node → 🎯 return the path.
   - Otherwise, add all unvisited neighbors to the queue with updated paths.
4. If queue is exhausted and no goal is found → return empty path.

> It guarantees the **shortest path** in unweighted graphs.

---

## 🧠 Applications of BFS

- 🌐 **Shortest path** in unweighted graphs
- 🧩 Solving puzzles (e.g., 8-puzzle, Rubik's cube)
- 🧭 GPS & Map Navigation systems
- 🧠 AI and Robotics for state exploration
- 🌳 Tree/graph structure level-order traversal
- 🔄 Network broadcast simulation

---

## 📈 Time and Space Complexity

| Metric        | Value                      |
|---------------|----------------------------|
| **Time**       | O(V + E)                   |
| **Space**      | O(V)                       |

Where:  
- `V` = number of vertices  
- `E` = number of edges  

> BFS is both **complete** and **optimal** for unweighted graphs.


---

## 🔢 Input Format

1. Number of **nodes** and **edges**
2. Whether the graph is **undirected or directed**
3. List of **edges** (as `from → to`)
4. The **start** and **goal** nodes

---

## 📥 Sample Input

