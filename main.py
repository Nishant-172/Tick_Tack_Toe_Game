import tkinter as tk  # Tkinter ko import kar rahe hain GUI banane ke liye
from tkinter import messagebox  # Messagebox ko import kar rahe hain winner ya tie ka message dikhane ke liye
import random  # Random module ko import kar rahe hain AI ka move random choose karne ke liye

# Initialize global variables
player_score = 0  # Player ka score initialize kar rahe hain
ai_score = 0  # AI ka score initialize kar rahe hain
board = [" " for _ in range(9)]  # Board ka 9 empty spaces wala list bana rahe hain
current_player = "X"  # Player ka symbol "X" set kar rahe hain, AI ka "O" hoga

# Reset the board for a new game
def reset_board():
    global board, current_player  # Global variables ko use kar rahe hain
    board = [" " for _ in range(9)]  # Board ko phir se empty kar rahe hain
    current_player = "X"  # Player ko first turn de rahe hain (X)
    for button in buttons:  # Saare buttons ko reset kar rahe hain
        button.config(text=" ", state="normal")  # Button ke text ko empty kar rahe hain aur state ko normal (clickable) kar rahe hain

# Display the winner or tie message
def display_winner(winner):
    global player_score, ai_score  # Global score variables ko use kar rahe hain
    if winner == "X":  # Agar player jeeta hai (X)
        player_score += 1  # Player ka score badha rahe hain
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations! You win!")  # Winner ka message show kar rahe hain
    elif winner == "O":  # Agar AI jeeta hai (O)
        ai_score += 1  # AI ka score badha rahe hain
        messagebox.showinfo("Tic-Tac-Toe", "AI wins! Better luck next time.")  # AI jeet gaya toh message show kar rahe hain
    else:  # Agar tie hua ho
        messagebox.showinfo("Tic-Tac-Toe", "The game is a tie!")  # Tie ka message show kar rahe hain
    update_scoreboard()  # Scoreboard update kar rahe hain
    reset_board()  # Board ko reset kar rahe hain nayi game ke liye

# Update the scoreboard after each game
def update_scoreboard():
    player_label.config(text=f"Player: {player_score}")  # Player ke score ko update kar rahe hain
    ai_label.config(text=f"AI: {ai_score}")  # AI ke score ko update kar rahe hain

# Check if there's a winner or if the board is full
def check_winner():
    win_combinations = [  # Winning combinations ke indices define kar rahe hain
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for combo in win_combinations:  # Saare winning combinations ko check kar rahe hain
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != " ":  # Agar 3 cells same player ke hain
            return board[combo[0]]  # Toh winner return kar rahe hain
    if " " not in board:  # Agar board full ho gaya ho aur koi winner nahi hai
        return "Tie"  # Toh game tie ho gaya
    return None  # Agar winner ya tie nahi hua ho toh None return karte hain

# AI's move logic
def ai_move():
    for i in range(9):  # AI pehle check karega agar wo jeet sakta hai
        if board[i] == " ":
            board[i] = "O"  # AI apna move karega (O)
            if check_winner() == "O":  # Agar AI jeet gaya ho
                update_button(i, "O")  # Button ko update karenge aur AI ka move show karenge
                return
            board[i] = " "  # Agar AI jeet nahi raha, toh move undo karenge
    for i in range(9):  # Player ke winning moves ko block karna
        if board[i] == " ":
            board[i] = "X"  # Player ka move (X) temporarily dal rahe hain
            if check_winner() == "X":  # Agar player jeet raha ho
                board[i] = "O"  # AI ko block karenge
                update_button(i, "O")
                return
            board[i] = " "  # Agar player ko block nahi karna tha toh undo karenge
    while True:  # Agar AI ko kuch nahi karna hai, toh random move karega
        move = random.randint(0, 8)  # Random index choose kar rahe hain
        if board[move] == " ":  # Agar wo space khaali ho
            update_button(move, "O")  # Move ko board par place karenge
            return

# Update the button text for a specific move
def update_button(index, player):
    board[index] = player  # Board par player ka move update kar rahe hain
    buttons[index].config(text=player, state="disabled")  # Button par move show kar rahe hain aur usse disable kar rahe hain
    winner = check_winner()  # Winner check kar rahe hain
    if winner:  # Agar koi winner hai
        display_winner(winner)  # Winner ka message display karenge
    else:
        toggle_player()  # Player ka turn change karenge

# Toggle between the player and the AI
def toggle_player():
    global current_player  # Current player ko change kar rahe hain
    current_player = "O" if current_player == "X" else "X"  # Agar current player X hai toh O ho jayega aur vice versa
    if current_player == "O":  # Agar AI ka turn hai
        ai_move()  # AI ka move call karenge

# Handle player's button click
def button_click(index):
    if board[index] == " " and current_player == "X":  # Agar button khaali hai aur player ka turn hai
        update_button(index, "X")  # Player ka move update karenge

# Set up the main game window
root = tk.Tk()  # Tkinter ka root window bana rahe hain
root.title("Tic-Tac-Toe")  # Title set kar rahe hain window ka

# Create a scoreboard
score_frame = tk.Frame(root)  # Ek frame bana rahe hain scoreboard ke liye
score_frame.grid(row=0, column=0, columnspan=3)  # Scoreboard ko grid mein set kar rahe hain (pehle row mein)

player_label = tk.Label(score_frame, text=f"Player: {player_score}", font=("Arial", 14))  # Player ka label bana rahe hain
player_label.grid(row=0, column=0)  # Player label ko grid mein place kar rahe hain
ai_label = tk.Label(score_frame, text=f"AI: {ai_score}", font=("Arial", 14))  # AI ka label bana rahe hain
ai_label.grid(row=0, column=1)  # AI label ko grid mein place kar rahe hain

# Create the Tic-Tac-Toe board with buttons
buttons = []  # Buttons ka list bana rahe hain
for i in range(9):  # 9 buttons banayenge
    button = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2,  # Button ka text, size aur font set kar rahe hain
                       command=lambda i=i: button_click(i))  # Button click hone par button_click function call hoga
    button.grid(row=(i // 3) + 1, column=i % 3)  # Buttons ko 3x3 grid mein arrange kar rahe hain
    buttons.append(button)  # Button ko list mein add kar rahe hain

# Add a restart button
restart_button = tk.Button(root, text="Restart", font=("Arial", 12), command=reset_board)  # Restart button bana rahe hain
restart_button.grid(row=4, column=1)  # Restart button ko grid mein place kar rahe hain

# Start the game loop
root.mainloop()  # Tkinter event loop ko start kar rahe hain, jo window ko open rakhta hai
