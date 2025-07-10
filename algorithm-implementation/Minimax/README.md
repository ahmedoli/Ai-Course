# 🎮 Minimax Algorithm in C++

This project implements the **Minimax algorithm**, a classic decision rule used for minimizing the possible loss in worst-case scenarios, widely used in two-player zero-sum games such as Chess, Tic-Tac-Toe, and Checkers.

---

## 📘 How the Algorithm Works

The Minimax algorithm simulates all possible moves in a game to determine the optimal move by assuming both players play optimally.

### 🧠 Working principle:
- The game tree is explored from the current position down to the terminal leaf nodes (or a certain depth).
- **Maximizer** tries to maximize the score.
- **Minimizer** tries to minimize the score.
- The algorithm recursively computes the best achievable score assuming both players play optimally.
- At the leaf nodes, the algorithm evaluates the game state (score).
- Using recursion, it backs up these scores through the tree, selecting max or min values depending on whose turn it is.

---

## 📚 Applications of Minimax

- ♟️ **Two-player games:** Chess, Checkers, Tic-Tac-Toe, Othello  
- 🎯 **Game AI:** To choose optimal moves against an opponent  
- 🧠 **Decision making:** Situations involving adversarial conditions  
- 🤖 **Reinforcement learning:** As a baseline for learning optimal policies

---

## 📈 Time and Space Complexity

| Metric        | Complexity                      |
|---------------|--------------------------------|
| **Time**       | O(b<sup>d</sup>)               |
| **Space**      | O(d) (recursion stack depth)   |

Where:  
- `b` = branching factor (number of children per node, here 2)  
- `d` = depth of the tree (height `h` in this implementation)

> The algorithm exhaustively searches the game tree, which grows exponentially with depth.

---


## 🔢 Input Format

- Height of the game tree (number of plies)
- Leaf node values (scores representing the evaluation of terminal states)

---

## 🧪 Sample Input

