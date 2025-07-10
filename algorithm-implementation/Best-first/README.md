# 🚀 Best-First Search Algorithm in C++

This is a C++ implementation of the **Best-First Search (Greedy Search)** algorithm. Best-First Search is a **graph traversal and pathfinding algorithm** that uses **heuristics** to prioritize which nodes to explore.

---

## 📘 How the Algorithm Works

Best-First Search explores the most promising node first, as judged by a **heuristic function**. It uses a **priority queue (min-heap)** to always expand the node with the lowest heuristic value.

### 🧠 Algorithm Steps:
1. Start at the **initial node**.
2. Use a **priority queue** to store nodes sorted by heuristic cost.
3. Expand the node with the **lowest heuristic value**.
4. Mark it as visited.
5. If the goal is found → ✅ Exit.
6. Otherwise, add all unvisited neighbors to the queue.
7. Repeat until:
   - Goal is found
   - Or no more nodes to explore

> It is **greedy** in nature — it chooses the next node that appears best at that moment.


---

## 🧠 Applications of Best-First Search

- 🔍 **AI Search Problems**  
- 🧭 **Pathfinding in maps and games**  
- 🧠 **Decision making in game trees**  
- 🧬 **Robot navigation**  
- 📚 **Solving puzzles** like 8-puzzle, Sudoku

---

## 📊 Time & Space Complexity

| Metric        | Complexity              |
|---------------|--------------------------|
| **Time**       | O(E * log V) (with heap) |
| **Space**      | O(V)                     |

Where:
- `V` = number of vertices (nodes)
- `E` = number of edges

---

## 🔢 Input Format

1. **Number of nodes `n`** and **edges `e`**
2. **Heuristic values** for each node
3. **Edges** (from `u` to `v`)
4. **Start** and **Goal** nodes


## 🖥️ Sample Run

### ▶️ Input:
