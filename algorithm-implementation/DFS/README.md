# 🌲 Depth-First Search (DFS) in C++

This C++ program implements the **Depth-First Search (DFS)** algorithm using a **stack-based approach** to find a path between a `start` and a `goal` node in a graph. The implementation supports both **directed** and **undirected** graphs.

---

## 📘 How the Algorithm Works

**Depth-First Search (DFS)** explores a graph by going as **deep as possible** down one path before backtracking. It uses a **stack** (LIFO) to manage which path to explore next.

### 🧠 DFS Algorithm Steps:
1. Initialize a stack with a path containing the `start` node.
2. Pop a path from the stack.
3. If the last node is the goal → ✅ Return the path.
4. If the node hasn't been visited:
   - Mark it as visited.
   - For all its **unvisited neighbors**, create new paths and push them onto the stack.
5. Repeat until:
   - The goal is found
   - Or the stack becomes empty (no path exists)

> This implementation returns **any one valid path**, not necessarily the shortest.

---
## 📚 Applications of DFS

- 🔍 **Pathfinding** in games and puzzles  
- 🧬 **Cycle detection** in graphs  
- 🌐 **Web crawlers**  
- 📊 **Topological sorting**  
- 🧠 **Maze solving**
- ⚙️ **Connectivity checks** in undirected/directed graphs

---

## 📈 Time and Space Complexity

| Metric        | Value        |
|---------------|--------------|
| **Time**       | O(V + E)     |
| **Space**      | O(V)         |

Where:  
- `V` = number of vertices  
- `E` = number of edges  

> DFS is **not guaranteed to find the shortest path** but is **fast and memory-efficient** for many tasks.

---

## 🔢 Input Format

- Number of **nodes** and **edges**
- Indication of whether the graph is **undirected** or **directed**
- List of **edges** in `from → to` format
- **Start** and **Goal** nodes

---

## 🧪 Sample Input

