# 🔎 Beam Search Algorithm in C++

A C++ implementation of the **Beam Search** algorithm — a heuristic-based informed search method used in AI and pathfinding tasks. This README provides a comprehensive understanding of how the algorithm works, its applications, complexity analysis, and sample input-output visuals.

---

## 📘 How the Algorithm Works

Beam Search is a **heuristic** search algorithm that explores a graph by expanding the most promising nodes in a **limited-width frontier** (beam). Unlike Breadth-First Search (BFS) that explores all neighbors, Beam Search only considers the **top-k (beam width)** nodes based on a heuristic value.

### 🔁 Steps:
1. Start at the **initial node**.
2. Generate all **successors** (neighbor nodes).
3. Sort successors based on **heuristic values**.
4. **Select only the best `k` nodes** (beam width) and discard the rest.
5. Repeat the process until:
   - Goal is found ✅
   - Frontier is empty ❌

> This technique sacrifices completeness for speed and efficiency.

---

## 📥 Input Format

- **n**: number of nodes  
- **e**: number of edges  
- **Heuristic values** for each node  
- **Edge list** (directed edges `u v`)  
- **Start node, Goal node, Beam Width**

---

## 📤 Output Format

- If goal is found: `Goal found at node X`  
- If not: `Goal not found within beam width.`

---

## 🧠 Applications of Beam Search

- 🤖 **Natural Language Processing** (e.g., Machine Translation, Speech Recognition)
- 🗺️ **Pathfinding Algorithms** in AI
- 🧬 **Protein Folding Simulations**
- 🔎 **Real-time Planning** in Robotics & Gaming
- 📡 **Information Retrieval & Search Engines**

---

## 📊 Time and Space Complexity

| Aspect       | Best Case        | Worst Case       |
|--------------|------------------|------------------|
| **Time**     | O(b × d)         | O(k × d × log k) |
| **Space**    | O(k)             | O(k × d)         |

Where:  
- `b` = branching factor  
- `d` = depth of the goal node  
- `k` = beam width  

> Beam Search is not complete or optimal, but **faster** and more **memory-efficient** than full best-first search when beam width is small.

---

## 🧪 Sample Input & Output

### ▶️ Sample Run:

#### Input:
