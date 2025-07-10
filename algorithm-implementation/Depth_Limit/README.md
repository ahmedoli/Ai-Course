# 🌲 Depth-Limited Search (DLS) Algorithm in C++

This project implements the **Depth-Limited Search (DLS)** algorithm — a variant of Depth-First Search that limits the depth of exploration in a graph or tree. It is commonly used to avoid infinite descent in graphs with cycles or very deep branches.

---

## 📘 How the Algorithm Works

Depth-Limited Search explores nodes in a depth-first manner but restricts the search to a **predefined depth limit**. If the goal node is not found within that depth, the search stops.

### 🧠 Algorithm Steps:
1. Start at the root (start node).
2. Recursively explore child nodes, decreasing the depth limit by 1 at each step.
3. If the current node is the goal → 🎯 return success.
4. If depth limit is reached → backtrack without exploring further.
5. Continue until goal is found or all nodes within depth limit are explored.

This approach prevents infinite loops in infinite or cyclic graphs.

---


---

## 🧠 Applications of Depth-Limited Search

- 🧩 Useful in **iterative deepening search** algorithms  
- 🚧 Avoids infinite loops in graphs with cycles  
- 🤖 Used in **game tree search** where depth needs restriction  
- 🔍 Problems with large or infinite search spaces where complete DFS is infeasible  
- 🔄 **Resource-bounded search** in AI applications

---

## 📈 Time and Space Complexity

| Metric        | Complexity              |
|---------------|------------------------|
| **Time**      | O(b^l)                 |
| **Space**     | O(l)                   |

Where:  
- `b` = branching factor (average number of children per node)  
- `l` = depth limit  

> Time grows exponentially with depth limit, but space complexity remains linear due to recursion depth.

---


## 🔢 Input Format

- Number of nodes `n` and edges `e`
- List of edges (`u v`) representing directed connections
- Start node, goal node, and depth limit

---

## 📥 Sample Input

