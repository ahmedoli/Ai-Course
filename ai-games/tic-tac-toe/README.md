

# 🕹️ Tic-Tac-Toe (with Minimax AI)

This is a classic **Tic-Tac-Toe game** where you play as **Player X** against an unbeatable **AI opponent (Player O)**. The game is built using **Python's Tkinter** library for the GUI and implements the **Minimax algorithm** to simulate smart computer moves.

---

## 🔧 How to Run the File

1. Make sure **Python 3.x** is installed on your computer.
2. Save the Python file as: `tic_tac_toe.py`
3. Open a terminal or command prompt and navigate to the directory containing the file.
4. Run the file using:

```bash
python tic_tac_toe.py
```

---

## 📦 Requirements

✅ You only need **Python 3.x** installed — no external libraries required.

### Built-in Libraries Used:

* `tkinter`: For creating the graphical user interface (GUI)
* `math`: For using mathematical constants like `inf` (infinity)

> No need to install anything separately — everything is built into standard Python.

---

## 🎮 How to Play the Game

* **You play as X**, the computer plays as **O**.
* Click on an **empty box** in the 3x3 grid to place your move.
* The computer will automatically respond with its optimal move.
* **Goal**: Get three of your symbols in a row (horizontal, vertical, or diagonal) before the computer does.
* If all cells are filled and no one wins, it’s declared a **draw**.
* After a game ends (win or draw), the board will **automatically reset** for a new game.

---

## 🧠 Algorithm Used

The game uses the **Minimax Algorithm** for AI:

* It explores **all possible future game states** recursively.
* The computer always plays **optimally**, trying to **maximize its chances of winning**.
* The player is assumed to also play optimally, and the AI will counter all possible human strategies.
* Ensures that the AI is **unbeatable** — at best, the human can get a draw.

---

## 📸 Screenshots

You can include the following screenshots in a `screenshots/` folder:

### 🖼️ Game Interface:

> Screenshot showing the initial game grid

![Game Window](screenshots/game_window.png)

---

### ✅ Player Wins:

> Screenshot after player (X) wins

![Player Win](screenshots/player_win.png)

---

### ❌ Computer Wins:

> Screenshot after computer (O) wins

![Computer Win](screenshots/computer_win.png)

---

### 😐 Draw Game:

> Screenshot showing a full board with no winner

![Draw](screenshots/draw.png)

---

## 💡 Bonus Tip

Want to customize the look or symbols? You can easily modify the:

* Button colors and fonts
* Symbols used (e.g., emojis like ❌ and ⭕)
* Add a scoreboard for tracking wins/draws

---

> ✅ This project is perfect for learning **basic AI**, **game logic**, and **Python GUI programming** using `Tkinter`.