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
![Image](https://github.com/user-attachments/assets/709bcde2-0c8f-4edf-9fe0-d3ab9ebde5af)

### **Gameplay - Player's Turn**
![Image](https://github.com/user-attachments/assets/135adcdb-7959-480d-b872-0941472eee47)

### **Gameplay - AI's Turn**
![Image](https://github.com/user-attachments/assets/5fc9d852-7689-48c9-bdd4-89b4f8ae57f4)

### **Winning Screen - Player / AI Wins**
![Image](https://github.com/user-attachments/assets/04a8bf6c-9ffa-48ca-a6d2-5e6f6a5af2ab)
### **Gameplay - After wining**
![Image](https://github.com/user-attachments/assets/b22c5756-1ded-485a-afa2-1bc5f7116903)

 
---
