# Tic-Tac-Toe Game (Human vs Computer)

This is a classic Tic-Tac-Toe game implemented in Python using the `tkinter` GUI framework. You play as **X**, and the computer plays as **O**, powered by the **Minimax algorithm** for an unbeatable AI experience.

---

## 📦 Requirements

Before running the game, make sure you have Python installed on your system.

### ✅ Pre-installed Libraries:

* `tkinter` (comes bundled with standard Python installations)
* `math` (standard Python module)

No external packages are required.

---

## ▶️ How to Run the Game

1. Save the code into a Python file, e.g., `tic_tac_toe.py`
2. Open your terminal or command prompt.
3. Navigate to the folder containing the file.
4. Run the following command:

```bash
python tic_tac_toe.py
```

A GUI window will open for the game.

---

## 🎮 How to Play

* The player is **X** and always plays first.
* Click any square in the 3x3 grid to make your move.
* The computer will respond immediately using the Minimax strategy.
* The game announces the result via a popup message:

  * You win!
  * Computer wins!
  * It's a draw!
* The board automatically resets for a new game after each round.

---

## 🧠 AI Algorithm Used

### Minimax Algorithm

The computer's decisions are powered by the **Minimax algorithm**, a recursive strategy used in decision-making and game theory. It assumes that your opponent (the human) will always play optimally and tries to minimize the possible loss.

Key properties:

* Optimal play (unbeatable AI)
* Depth-based scoring system:

  * +1 if AI wins
  * -1 if player wins
  * 0 for a draw

---

## 🖼️ Screenshots

> 🧩 Here are some visuals of the game:

### **Game Board**
![Image](https://github.com/user-attachments/assets/74c3126c-cd69-4a65-be06-9a722919c0b1)

### **Player's Turn**
![Image](https://github.com/user-attachments/assets/f3559259-c3f8-4179-8337-eca9df881b9e)
### **Computer's Turn**
![Image](https://github.com/user-attachments/assets/aed4246e-9206-4b1f-9a99-70881cc23e50)
### **after compelete game with multiple moves**
![Image](https://github.com/user-attachments/assets/eefa65e4-2816-4f12-a3ad-0b7fac1e98d6)
### **Draw Screen**
![Image](https://github.com/user-attachments/assets/d92f71cd-a685-4b5e-8ad4-2e0e016434ba)
### **New game with multiple moves**
![Image](https://github.com/user-attachments/assets/4e8d4690-dece-4f52-96d2-70430165a2ba)
### **Winning Screen (Player/Computer Wins)**
![Image](https://github.com/user-attachments/assets/0aef7239-dba7-492f-b9cc-0c5b8c20d16c)

---

**Suggested file structure:**

```
/your-project-folder
|-- tic_tac_toe.py
|-- README.md
|-- screenshots/
    |-- gameplay1.png
    |-- gameplay2.png
```

To add screenshots in your `README.md`:

```markdown
![Gameplay 1](screenshots/gameplay1.png)
![Gameplay 2](screenshots/gameplay2.png)
```

---

## 💡 Tips

* You cannot beat the AI if it plays first or second correctly.
* Try to create forks and block opponent's forks to play smart.

---

## 📜 License

This project is open-source and free to use for learning or modification purposes.
