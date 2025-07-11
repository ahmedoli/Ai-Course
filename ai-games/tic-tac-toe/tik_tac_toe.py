import tkinter as tk
from tkinter import messagebox
import math

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe (You: X | Computer: O)")
        
        # Initialize game board as a list of 9 spaces
        self.board = [' ' for _ in range(9)]
        
        # List to store button references
        self.buttons = []

        # Create the GUI board
        self.create_board()

        # Set player and computer symbols
        self.player = 'X'
        self.computer = 'O'

    def create_board(self):
        # Create 3x3 grid of buttons
        for i in range(9):
            button = tk.Button(self.root, text=' ', font='Helvetica 20 bold', height=3, width=6,
                               command=lambda i=i: self.on_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

    def on_click(self, index):
        # Handle button click by human player
        if self.board[index] == ' ':
            self.make_move(index, self.player)
            if self.check_winner(self.player):
                messagebox.showinfo("Game Over", "You win!")
                self.reset_board()
                return
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_board()
                return

            # Delay computer move slightly for realism
            self.root.after(500, self.computer_move)

    def make_move(self, index, player):
        # Make move and disable the button
        self.board[index] = player
        self.buttons[index]['text'] = player
        self.buttons[index]['state'] = 'disabled'

    def is_draw(self):
        # Check if board is full without a winner
        return ' ' not in self.board

    def check_winner(self, player):
        # Winning combinations for 3x3 grid
        win_combinations = [
            [0,1,2], [3,4,5], [6,7,8],  # Rows
            [0,3,6], [1,4,7], [2,5,8],  # Columns
            [0,4,8], [2,4,6]            # Diagonals
        ]
        return any(all(self.board[i] == player for i in combo) for combo in win_combinations)

    def computer_move(self):
        # Computer determines best move using Minimax algorithm
        best_score = -math.inf
        best_move = None
        for move in self.available_moves():
            self.board[move] = self.computer
            score = self.minimax(0, False)
            self.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move

        # Make the best move
        self.make_move(best_move, self.computer)

        if self.check_winner(self.computer):
            messagebox.showinfo("Game Over", "Computer wins!")
            self.reset_board()
        elif self.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_board()

    def minimax(self, depth, is_maximizing):
        # Minimax algorithm for finding best move
        if self.check_winner(self.computer):
            return 1
        elif self.check_winner(self.player):
            return -1
        elif self.is_draw():
            return 0

        if is_maximizing:
            best_score = -math.inf
            for move in self.available_moves():
                self.board[move] = self.computer
                score = self.minimax(depth + 1, False)
                self.board[move] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for move in self.available_moves():
                self.board[move] = self.player
                score = self.minimax(depth + 1, True)
                self.board[move] = ' '
                best_score = min(score, best_score)
            return best_score

    def available_moves(self):
        # Return list of available move indices
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def reset_board(self):
        # Reset game for a new round
        self.board = [' ' for _ in range(9)]
        for btn in self.buttons:
            btn.config(text=' ', state='normal')

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
