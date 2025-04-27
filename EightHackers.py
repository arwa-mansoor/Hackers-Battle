import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class EightQueensGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hacking")
        self.root.configure(bg="black")
        self.root.geometry("600x600")

        self.board_size = 8
        self.cell_size = 60
        self.queen_positions = set()  # Initialize queen positions set

        # Load queen image
        self.queen_image = ImageTk.PhotoImage(Image.open("icon.jpg").resize((50, 50)))

        # Instruction label
        self.instruction_label = tk.Label(
            self.root, text="P14c3 th3 31gh7 h4ck3r 1n such 4 m4nn3r th4t th3y 4v01d 0ccupy1ng th3 s4m3 v3rt1c4l, h0r1z0nt4l, 0r d14g0n4l l1n3s. Cl1ck 0n 4 b04rd c3ll t0 pl4c3 0r r3m0v3 4 h4ck3r.",
            fg="white", bg="black", font=("Arial", 12), wraplength=500
        )
        self.instruction_label.pack(pady=10)

        # Create a canvas for the chessboard
        self.canvas = tk.Canvas(self.root, width=self.board_size * self.cell_size, 
                                height=self.board_size * self.cell_size, bg="white")
        self.canvas.pack(pady=20)

        # Draw chessboard
        self.draw_chessboard()

        # Store queen items
        self.queen_items = {}

        # Check button
        self.check_button = tk.Button(self.root, text="Check Solution", 
                                      command=self.check_solution, bg="green", fg="white")
        self.check_button.pack(pady=10)

        # Reset button
        self.reset_button = tk.Button(self.root, text="Reset Board", 
                                      command=self.reset_board, bg="green", fg="white")
        self.reset_button.pack(pady=5)

        # Bind click event to place/remove queens
        self.canvas.bind("<Button-1>", self.toggle_queen)

    def draw_chessboard(self):
        self.canvas.delete("all")  # Clear previous board
        for row in range(self.board_size):
            for col in range(self.board_size):
                color = "white" if (row + col) % 2 == 0 else "green"
                x1, y1 = col * self.cell_size, row * self.cell_size
                x2, y2 = x1 + self.cell_size, y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

        # Redraw queens
        for row, col in self.queen_positions:
            self.place_queen(row, col)

    def toggle_queen(self, event):
        row, col = event.y // self.cell_size, event.x // self.cell_size

        if (row, col) in self.queen_positions:
            # Remove the queen
            self.queen_positions.remove((row, col))
            self.draw_chessboard()
        elif len(self.queen_positions) < 8:
            # Place a queen
            self.queen_positions.add((row, col))
            self.place_queen(row, col)

    def place_queen(self, row, col):
        x, y = col * self.cell_size + self.cell_size // 2, row * self.cell_size + self.cell_size // 2
        queen_item = self.canvas.create_image(x, y, image=self.queen_image)
        self.queen_items[(row, col)] = queen_item

    def check_solution(self):
        if len(self.queen_positions) != 8:
            messagebox.showerror("Error", "You must place exactly 8 hackers!")
            return

        # Extract queen coordinates
        queens = list(self.queen_positions)

        # Check if the solution is valid
        if self.is_valid_solution(queens):
            messagebox.showinfo("Success", "Congratulations! Solution is correct.")
        else:
            messagebox.showerror("Error", "Invalid solution. Try again.")

    def reset_board(self):
        self.queen_positions.clear()
        self.draw_chessboard()

    def is_valid_solution(self, queens):
        rows, cols, diag1, diag2 = set(), set(), set(), set()

        for row, col in queens:
            if row in rows or col in cols or (row - col) in diag1 or (row + col) in diag2:
                return False
            rows.add(row)
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = EightQueensGame(root)
    root.mainloop()
