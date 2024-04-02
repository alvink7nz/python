import tkinter as tk
from tkinter import messagebox

# Constants
EMPTY = '.'
PLAYER_X = 'X'
PLAYER_O = 'O'
MAX_DEPTH = 3

class HexapawnGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hexapawn")
        self.board = [
            [PLAYER_X, PLAYER_X, PLAYER_X],
            [EMPTY, EMPTY, EMPTY],
            [PLAYER_O, PLAYER_O, PLAYER_O]
        ]
        self.selected_piece = None
        self.buttons = []
        self.current_player = PLAYER_X  # Start with player X
        self.create_board()

    def create_board(self):
        for i in range(3):
            row_buttons = []
            for j in range(3):
                button = tk.Button(self.master, text=self.board[i][j], font=('Helvetica', 24), width=3, height=1,
                                   command=lambda row=i, col=j: self.handle_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)
    def handle_click(self, row, col):
        if self.selected_piece is None:  # If no piece is selected, select one
            if self.board[row][col] == self.current_player:
                self.selected_piece = (row, col)
        else:  # If a piece is already selected, move it
            move_from = self.selected_piece
            move_to = (row, col)
            if move_from != move_to and self.is_valid_move(self.board, move_from[0], move_from[1], move_to[0], move_to[1], PLAYER_X):
                self.board[move_to[0]][move_to[1]] = self.board[move_from[0]][move_from[1]]
                self.board[move_from[0]][move_from[1]] = EMPTY
                self.selected_piece = None

                # Check for win or draw after player's move
                if self.check_win(self.current_player):
                    messagebox.showinfo("Game Over", "Congratulations! You win!")
                    self.reset_board()
                    return
                if self.check_draw():
                    messagebox.showinfo("Game Over", "It's a draw!")
                    self.reset_board()
                    return

                # Computer's move
                self.computer_move()

                # Check for win or draw after computer's move
                if self.check_win(PLAYER_O):
                    messagebox.showinfo("Game Over", "Sorry, you lose!")
                    self.reset_board()
                    return
                if self.check_draw():
                    messagebox.showinfo("Game Over", "It's a draw!")
                    self.reset_board()

        self.update_buttons()

    def update_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=self.board[i][j])

    def check_win(self, player):
        for row in range(3):
            if self.board[row][0] == player and self.board[row][1] == player and self.board[row][2] == player:
                return True
        return False

    def check_draw(self):
        for row in self.board:
            if EMPTY in row:
                return False
        return True

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = PLAYER_X if (i == 0 or i == 2) else EMPTY
        self.update_buttons()
        self.current_player = PLAYER_X

    def computer_move(self):
        best_move = self.minimax(self.board, MAX_DEPTH, float('-inf'), float('inf'), True, PLAYER_O if self.current_player == PLAYER_X else PLAYER_X)[1]
        if best_move:
            self.board[best_move[1][0]][best_move[1][1]] = self.board[best_move[0][0]][best_move[0][1]]
            self.board[best_move[0][0]][best_move[0][1]] = EMPTY

    def minimax(self, board, depth, alpha, beta, maximizing_player, player):
        if depth == 0 or self.check_win(PLAYER_X) or self.check_win(PLAYER_O) or self.check_draw():
            return self.evaluate(board), None

        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            if self.is_valid_move(board, i, j, k, l, PLAYER_O):
                                board[k][l] = board[i][j]
                                board[i][j] = EMPTY
                                eval = self.minimax(board, depth - 1, alpha, beta, False, player)[0]
                                board[i][j] = board[k][l]
                                board[k][l] = EMPTY
                                if eval > max_eval:
                                    max_eval = eval
                                    best_move = [(i, j), (k, l)]
                                alpha = max(alpha, eval)
                                if beta <= alpha:
                                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        for l in range(3):
                            if self.is_valid_move(board, i, j, k, l, PLAYER_X):
                                board[k][l] = board[i][j]
                                board[i][j] = EMPTY
                                eval = self.minimax(board, depth - 1, alpha, beta, True, player)[0]
                                board[i][j] = board[k][l]
                                board[k][l] = EMPTY
                                if eval < min_eval:
                                    min_eval = eval
                                    best_move = [(i, j), (k, l)]
                                beta = min(beta, eval)
                                if beta <= alpha:
                                    break
            return min_eval, best_move

    def is_valid_move(self, board, from_row, from_col, to_row, to_col, player):
        if board[from_row][from_col] != player:
            return False
        if board[to_row][to_col] != EMPTY:
            return False
        if player == PLAYER_X:
            if from_row != to_row + 1 or abs(from_col - to_col) > 1:
                return False
        elif player == PLAYER_O:
            if from_row != to_row - 1 or abs(from_col - to_col) > 1:
                return False
        return True

    def evaluate(self, board):
        if self.check_win(PLAYER_X):
            return 10
        elif self.check_win(PLAYER_O):
            return -10
        else:
            return 0

def main():
    root = tk.Tk()
    app = HexapawnGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()