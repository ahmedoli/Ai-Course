# 🔴🟡 Connect Four (AI vs Player) using Minimax with Alpha-Beta Pruning

This is a classic **Connect Four** game where a human player competes against an **AI opponent** built using the **Minimax algorithm** with **Alpha-Beta Pruning**. The game features a user-friendly **GUI built with Pygame**.

---

## 🔧 How to Run the Game

1. Make sure **Python 3.x** is installed on your system.
2. Install the required libraries by running the following commands:

```bash
pip install pygame
pip install numpy
```

3. Save the game file as:

```bash
connect_four.py
```

4. Open your terminal or command prompt and run:

```bash
python connect_four.py
```

---

## 📦 Requirements

* **Python 3.x**
* **Pygame** – for creating the graphical user interface
  Install via: `pip install pygame`
* **NumPy** – for efficient array handling
  Install via: `pip install numpy`

> 💡 *Tip: If you're using an IDE like VS Code or PyCharm, make sure your virtual environment has these packages installed.*

---

## 🎮 How to Play

### Menu Options:

* Press **1**: You play first (as 🔴 **Red**).
* Press **2**: AI plays first (as 🟡 **Yellow**).
* Press **Q**: Quit the game.

### Gameplay Instructions:

* The game board is a **6x7 grid**.
* Move your mouse horizontally to select a column.
* Click to **drop your disk** into that column.
* The first player to **connect 4 disks** (horizontally, vertically, or diagonally) **wins**.
* If the board is full and no player has won, the game ends in a **draw**.

### After the Game:

* Press **Y** to play again.
* Press **N** to quit.

---

## 🧠 Algorithm Used

### ✅ **Minimax with Alpha-Beta Pruning**

The AI is powered by a **Minimax algorithm** that:

* Explores all possible moves to determine the best outcome.
* Uses **Alpha-Beta pruning** to skip over unnecessary branches, increasing efficiency.

### 🔍 Scoring System:

* Prioritizes controlling the **center column**.
* Evaluates and scores:

  * 2 in a row
  * 3 in a row
  * 4 in a row
* Penalizes moves that give the opponent an advantage.

> 🤖 The result is a highly strategic and **unbeatable AI opponent** when played optimally.

---

## 📸 Screenshots

* 🧩 Here are some visuals of the game:

### **Menu Screen**
![Image](./screenshots/menu_screen.jpg)

### **Gameplay - Player's Turn**
![Image](./screenshots/Gameplay_player's%20turn.jpg)

### **Gameplay - AI's Turn**
![Image](./screenshots/Gameplay_AI's%20turn.jpg)

### **Winning Screen - Player / AI Wins**
![Image](./screenshots/Winning%20Screen%20-%20AI%20Wins.jpg)
### **Gameplay - After wining**
![Image](./screenshots/Gameplay%20-%20After%20wining.jpg)

 
---
