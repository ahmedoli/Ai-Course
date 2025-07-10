# 🔁 Bidirectional Search in C++

This C++ program implements the **Bidirectional Search** algorithm — an advanced and efficient graph search technique used to find the shortest path between a start and goal node by **searching from both directions simultaneously**.

---

## 📘 How the Algorithm Works

Bidirectional Search works by **running two simultaneous Breadth-First Searches** — one from the `start` node and the other from the `goal` node. The idea is that the two searches will meet somewhere in the middle, which significantly reduces the number of nodes explored.

### 🧠 Steps:
1. Initialize two queues:  
   - `q_f` for forward BFS from the **start** node  
   - `q_b` for backward BFS from the **goal** node

2. Initialize two visited sets: `visited_f` and `visited_b`

3. Loop until either queue is empty:
   - Pop one node from each queue
   - If there's any node common to both visited sets → ✅ **Path Found**
   - Otherwise, expand neighbors of each node and update the respective queues and visited sets

4. If queues are exhausted without intersection → ❌ **No Path Found**

---


## 📚 Applications of Bidirectional Search

- 🔍 **Finding shortest path** in undirected graphs
- 🧭 **Navigation systems** (e.g., Google Maps)
- 🤖 **AI in games and robotics**
- 🧠 **Pathfinding in large unweighted graphs**
- 🌐 **Social network analysis** (finding connection paths between users)

---

## 📈 Time and Space Complexity

| Metric        | Value                              |
|---------------|--------------------------------------|
| **Time**       | O(b^(d/2)) + O(b^(d/2)) = O(b^(d/2)) |
| **Space**      | O(b^(d/2))                          |

Where:  
- `b` = branching factor  
- `d` = distance between start and goal  

> This is exponentially faster than normal BFS for large graphs.

---

## 🔢 Input Format

- Number of **nodes `n`** and **edges `e`**
- The `e` edges of the graph (undirected)
- The **start** and **goal** nodes

---

## 📥 Sample Input

