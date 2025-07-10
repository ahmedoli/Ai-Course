# 🔍 Iterative Deepening Search (IDS) in C++

This project implements the **Iterative Deepening Search (IDS)** algorithm using a combination of **Depth-Limited Search (DLS)** with gradually increasing depth limits. IDS combines the space-efficiency of Depth-First Search (DFS) with the completeness of Breadth-First Search (BFS).

---

## 📘 How the Algorithm Works

**Iterative Deepening Search** repeatedly runs **Depth-Limited Search (DLS)** with increasing depth limits, starting from 0 and increasing until the goal is found or a maximum depth is reached.

### 🧠 Algorithm Steps:
1. Set an initial depth limit to 0.
2. Perform Depth-Limited Search up to the current depth limit.
3. If the goal is found → 🎯 return success.
4. Else, increment the depth limit and repeat.
5. Stop when the goal is found or maximum depth is exceeded.

> IDS explores nodes level by level like BFS but uses less memory by performing DFS repeatedly with limited depth.

---
## 🧠 Applications of Iterative Deepening Search

- 🌐 **AI game tree searches** (e.g., chess, checkers)
- 🔄 **State-space search** where depth is unknown
- 🚀 **Memory-limited environments** requiring DFS-like space usage
- 🔎 **Finding shortest paths** in unweighted graphs (like BFS)
- 🧠 **Robotics and puzzle solving**

---

## 📈 Time and Space Complexity

| Metric        | Complexity                   |
|---------------|------------------------------|
| **Time**       | O(b<sup>d</sup>)             |
| **Space**      | O(d)                        |

Where:  
- `b` = branching factor  
- `d` = depth of the shallowest goal node  

> IDS performs some repeated work but is still efficient for many search problems with unknown depth.

---

## 🔢 Input Format

- Number of nodes `n` and edges `e`
- List of directed edges `(u v)`
- Start and goal nodes

---

## 🧪 Sample Input

