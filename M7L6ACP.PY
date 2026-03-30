import tkinter as tk
import random

def play(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    result_label.config(
        text=f"Your Choice: {user_choice}\nComputer: {computer_choice}\nResult: {result}"
    )

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

tk.Label(root, text="Choose Rock, Paper or Scissors", font=("Arial", 12)).pack(pady=20)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Rock", width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Paper", width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Scissors", width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=30)

root.mainloop()