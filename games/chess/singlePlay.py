import tkinter as tk

class Chess:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Chess")
        
        # Chessboard and pieces
        self.board = self.initialize_board()
        self.selected_square = None
        self.buttons = [[None for _ in range(8)] for _ in range(8)]
        self.whiteTurn = True

        # Draw the board
        self.create_board()

    def initialize_board(self):
        """Initializes the chessboard with pieces."""
        return [
            ["r", "n", "b", "q", "k", "b", "n", "r"],  # Black major pieces
            ["p"] * 8,                                # Black pawns
            [None] * 8,                               # Empty rows
            [None] * 8,
            [None] * 8,
            [None] * 8,
            ["P"] * 8,                                # White pawns
            ["R", "N", "B", "Q", "K", "B", "N", "R"], # White major pieces
        ]

    def create_board(self):
        """Creates the chessboard with buttons."""
        for row in range(8):
            for col in range(8):
                # Determine color of the square
                color = "white" if (row + col) % 2 == 0 else "green"
                
                # Create a button for each square
                btn = tk.Button(
                    self.root,
                    text=self.board[row][col] if self.board[row][col] else "",
                    font=("Helvetica", 24),
                    width=3,
                    height=1,
                    bg=color,
                    command=lambda r=row, c=col: self.on_square_click(r, c)
                )
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

    def on_square_click(self, row, col):
        """Handles click events on a square."""
        if self.selected_square:
            # Move piece to new square
            if self.board[row][col] == ".":
                start_row, start_col = self.selected_square
                self.board[row][col] = self.board[start_row][start_col]
                self.board[start_row][start_col] = None
                self.selected_square = None  # Deselect
                for x in range(8):
                    for y in range(8):
                        if self.board[x][y] == ".":
                            self.board[x][y] = None
            
            # Update board display
            self.update_board()
        else:
            piece = self.board[row][col]
            if not piece:
                return  # No piece in the selected square, exit.

            # Define movement logic for each piece
            def move_pawn(row, col):
                direction = -1 if piece.isupper() else 1
                start_row = 6 if piece == "P" else 1
                if self.board[row + direction][col] is None:
                    self.board[row + direction][col] = "."
                    if row == start_row and self.board[row + 2 * direction][col] is None:
                        self.board[row + 2 * direction][col] = "."
                    update_turn(row, col)

            def move_rook(row, col):
                directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                move_linear(row, col, directions)

            def move_bishop(row, col):
                directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
                move_linear(row, col, directions)

            def move_queen(row, col):
                directions = [
                    (-1, -1), (-1, 1), (1, 1), (1, -1),  # Bishop-like moves
                    (0, -1), (0, 1), (-1, 0), (1, 0)     # Rook-like moves
                ]
                move_linear(row, col, directions)

            def move_knight(row, col):
                # Possible relative moves for a knight
                knight_moves = [
                    (-2, -1), (-2, 1),  # Two steps up, one step left/right
                    (2, -1), (2, 1),    # Two steps down, one step left/right
                    (-1, -2), (1, -2),  # One step up/down, two steps left
                    (-1, 2), (1, 2)     # One step up/down, two steps right
                ]

                for dr, dc in knight_moves:
                    new_row, new_col = row + dr, col + dc

                    # Check if the move is within board boundaries
                    if 0 <= new_row < 8 and 0 <= new_col < 8:
                        target = self.board[new_row][new_col]

                        # Check if the square is empty or has an opponent's piece
                        if target is None or (target.islower() if piece.isupper() else target.isupper()):
                            self.board[new_row][new_col] = "."  # Mark as a possible move

                # Update the board and turn
                update_turn(row, col)

            def move_king(row, col):
                # Possible relative moves for the king
                king_moves = [
                    (-1, -1), (-1, 0), (-1, 1),  # Diagonals and vertical moves upwards
                    (0, -1),         (0, 1),     # Horizontal moves
                    (1, -1), (1, 0), (1, 1)      # Diagonals and vertical moves downwards
                ]

                for dr, dc in king_moves:
                    new_row, new_col = row + dr, col + dc

                    # Check if the move is within board boundaries
                    if 0 <= new_row < 8 and 0 <= new_col < 8:
                        target = self.board[new_row][new_col]

                        # Check if the square is empty or has an opponent's piece
                        if target is None or (target.islower() if piece.isupper() else target.isupper()):
                            self.board[new_row][new_col] = "."  # Mark as a possible move

                # Update the board and turn
                update_turn(row, col)

            def move_linear(row, col, directions):
                for dr, dc in directions:
                    for i in range(1, 8):
                        new_row, new_col = row + dr * i, col + dc * i
                        if 0 <= new_row < 8 and 0 <= new_col < 8 and self.board[new_row][new_col] is None:
                            self.board[new_row][new_col] = "."
                        else:
                            break
                update_turn(row, col)

            def update_turn(row, col):
                self.update_board()
                self.selected_square = (row, col)
                self.whiteTurn = not self.whiteTurn

            # Map piece to corresponding movement logic
            piece_moves = {
                "R": move_rook,
                "r": move_rook,
                "B": move_bishop,
                "b": move_bishop,
                "Q": move_queen,
                "q": move_queen,
                "N": move_knight,  
                "n": move_knight, 
                "K": move_king,
                "k": move_king
            }

            # Execute movement if it’s the correct turn for the piece
            if piece in piece_moves and ((piece.isupper() and self.whiteTurn) or (piece.islower() and not self.whiteTurn)):
                piece_moves[piece](row, col)
            elif piece in ["P", "p"]:  # Handle pawns separately
                if (piece == "P" and self.whiteTurn) or (piece == "p" and not self.whiteTurn):
                    move_pawn(row, col)


    def update_board(self):
        """Updates the button text to reflect the board state."""
        for row in range(8):
            for col in range(8):
                text = self.board[row][col] if self.board[row][col] else ""
                self.buttons[row][col].config(text=text)