import tkinter as tk

def check_strength():
    password = entry.get()
    length = len(password)

    if length <= 5:
        result_label.config(text="Weak", fg="red")
    elif 6 <= length <= 8:
        result_label.config(text="Medium", fg="yellow")
    elif 9 <= length <= 12:
        result_label.config(text="Strong", fg="light green")
    else:
        result_label.config(text="Very Strong", fg="dark green")

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=30)

tk.Label(frame, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(frame, show="*")
entry.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Check Strength", command=check_strength).pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()