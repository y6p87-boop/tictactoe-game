# I acknowledge the use of Claude (Anthropic, https://claude.ai/) to create the code in this file.

import tkinter as tk
from tkinter import messagebox
from score_tracker import ScoreTracker

# --- Constants ---
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = ""

class TicTacToe:
    """Main Tic-Tac-Toe game class with score tracking."""

    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe | Two Player Game")
        self.root.configure(bg="#f0f0f0")
        self.current_player = PLAYER_X
        self.board = [EMPTY] * 9
        self.buttons = []
        self.tracker = ScoreTracker()
        self.build_gui()

    def build_gui(self):
        """Build the game board UI."""
        title = tk.Label(self.root, text="Tic-Tac-Toe", font=("Arial", 20, "bold"), bg="#f0f0f0")
        title.grid(row=0, column=0, columnspan=3, pady=10)

        self.status_label = tk.Label(self.root, text=f"Player {self.current_player}'s turn", font=("Arial", 13), bg="#f0f0f0", fg="green")
        self.status_label.grid(row=1, column=0, columnspan=3)

        # Score display
        self.score_label = tk.Label(self.root, text=self.tracker.get_scores(), font=("Arial", 11), fg="blue", bg="#f0f0f0")
        self.score_label.grid(row=2, column=0, columnspan=3)

        for i in range(9):
            btn = tk.Button(
                self.root, text="", font=("Arial", 24, "bold"),
                width=5, height=2,
                command=lambda i=i: self.on_click(i)
            )
            btn.grid(row=(i // 3) + 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)

        # Restart and Reset Score buttons
        restart_btn = tk.Button(self.root, text="Restart Game", font=("Arial", 12), command=self.restart)
        restart_btn.grid(row=6, column=0, columnspan=2, pady=10)

        reset_score_btn = tk.Button(self.root, text="Reset Scores", font=("Arial", 12), command=self.reset_scores)
        reset_score_btn.grid(row=6, column=2, pady=10)

    def on_click(self, index):
        """Handle a cell click."""
        if self.board[index] != EMPTY:
            return

        self.board[index] = self.current_player
        self.buttons[index].config(text=self.current_player)

        if self.check_winner():
            self.tracker.record_win(self.current_player)
            self.score_label.config(text=self.tracker.get_scores())
            messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
            self.restart()
        elif EMPTY not in self.board:
            self.tracker.record_draw()
            self.score_label.config(text=self.tracker.get_scores())
            messagebox.showinfo("Game Over", "It's a draw!")
            self.restart()
        else:
            self.current_player = PLAYER_O if self.current_player == PLAYER_X else PLAYER_X
            self.status_label.config(text=f"Player {self.current_player}'s turn")

    def check_winner(self):
        """Check if the current player has won."""
        winning_combos = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        for combo in winning_combos:
            if all(self.board[i] == self.current_player for i in combo):
                return True
        return False

    def restart(self):
        """Reset the board for a new game."""
        self.board = [EMPTY] * 9
        self.current_player = PLAYER_X
        self.status_label.config(text=f"Player {self.current_player}'s turn")
        for btn in self.buttons:
            btn.config(text="")

    def reset_scores(self):
        """Reset all scores to zero."""
        self.tracker.reset()
        self.score_label.config(text=self.tracker.get_scores())


if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()