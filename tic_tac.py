import tkinter as tk
from tkinter import messagebox

# Initialize window
root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg="#f0f0f0")

# Global variables
current_player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

# Colors and styles
colors = {
    "X": "#ff4d4d",   # red
    "O": "#4d79ff",   # blue
    "bg": "#ffffff",
    "highlight": "#90ee90"
}

def check_winner():
    for i in range(3):
        # Check rows
        if buttons[i][0]["text"] != "" and all(buttons[i][j]["text"] == buttons[i][0]["text"] for j in range(3)):
            highlight_winner([(i, j) for j in range(3)])
            return buttons[i][0]["text"]

        # Check columns
        if buttons[0][i]["text"] != "" and all(buttons[j][i]["text"] == buttons[0][i]["text"] for j in range(3)):
            highlight_winner([(j, i) for j in range(3)])
            return buttons[0][i]["text"]

    # Check diagonals
    if buttons[0][0]["text"] != "" and all(buttons[i][i]["text"] == buttons[0][0]["text"] for i in range(3)):
        highlight_winner([(i, i) for i in range(3)])
        return buttons[0][0]["text"]
    if buttons[0][2]["text"] != "" and all(buttons[i][2-i]["text"] == buttons[0][2]["text"] for i in range(3)):
        highlight_winner([(i, 2-i) for i in range(3)])
        return buttons[0][2]["text"]

    # Check for draw
    if all(buttons[i][j]["text"] != "" for i in range(3) for j in range(3)):
        return "Draw"
    
    return None

def highlight_winner(coords):
    for i, j in coords:
        buttons[i][j].configure(bg=colors["highlight"])

def on_click(row, col):
    global current_player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        buttons[row][col]["fg"] = colors[current_player]
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Result", "It's a Draw!")
            else:
                messagebox.showinfo("Winner", f"{winner} wins!")
            disable_all_buttons()
        else:
            current_player = "O" if current_player == "X" else "X"

def disable_all_buttons():
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")

def reset_game():
    global current_player
    current_player = "X"
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", bg=colors["bg"], state="normal", fg="black")

# Create the grid buttons
frame = tk.Frame(root, bg="#f0f0f0", pady=20)
frame.pack()

for i in range(3):
    for j in range(3):
        btn = tk.Button(frame, text="", font=('Arial', 32), width=5, height=2,
                        bg=colors["bg"], command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j, padx=10, pady=10)
        buttons[i][j] = btn

# Reset Button
reset_btn = tk.Button(root, text="Reset Game", font=('Arial', 14), bg="#ffd966", fg="black",
                      command=reset_game, padx=10, pady=5)
reset_btn.pack(pady=10)

root.mainloop()
