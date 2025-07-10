# 🎯 Alpha-Beta Pruning Algorithm

An efficient implementation of the **Alpha-Beta Pruning** algorithm using C++. This optimization is applied to the **Minimax algorithm** used in decision-making and game theory, most notably in **two-player turn-based games** like Tic-Tac-Toe, Chess, etc.

---

## 📌 How the Algorithm Works

Alpha-Beta Pruning is an enhancement of the **Minimax algorithm** that eliminates branches in the game tree which cannot possibly influence the final decision.

### 🧠 Concept:
- Two players: **Maximizer** and **Minimizer**
- The algorithm explores a game tree of certain height `h`, where:
  - Each **Max** level tries to maximize the value.
  - Each **Min** level tries to minimize the value.

### 🔁 Alpha & Beta:
- **Alpha**: Best value that the maximizer can guarantee so far.
- **Beta**: Best value that the minimizer can guarantee so far.
- If `beta ≤ alpha`, further exploration is **pruned** as it won't affect the result.

### 👣 Steps:
1. Start from root node (depth 0).
2. Traverse to leaves (depth = height `h`).
3. Return scores at leaf level.
4. Apply **alpha-beta bounds** while traversing up to avoid unnecessary branches.

---

## 🧮 Time & Space Complexity

| Factor            | Complexity  |
|------------------|-------------|
| **Best Case**     | O(b<sup>d/2</sup>) |
| **Worst Case**    | O(b<sup>d</sup>)   |
| **Space**         | O(d) — due to recursion stack |

Where:
- `b` = branching factor (2 in this case)
- `d` = depth of the tree

---

## 🛠 Sample Input & Output

### 🔢 Sample Run:

**User Input:**
