import tkinter as tk
from datetime import date

def calculate_age():
    name = entry_name.get()
    d = int(entry_day.get())
    m = int(entry_month.get())
    y = int(entry_year.get())

    today = date.today()
    age = today.year - y - ((today.month, today.day) < (m, d))

    result_label.config(text=f"Hello {name}, you are {age} years old.")

root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Name").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(frame)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Day").grid(row=1, column=0, padx=10, pady=5)
entry_day = tk.Entry(frame)
entry_day.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame, text="Month").grid(row=2, column=0, padx=10, pady=5)
entry_month = tk.Entry(frame)
entry_month.grid(row=2, column=1, padx=10, pady=5)

tk.Label(frame, text="Year").grid(row=3, column=0, padx=10, pady=5)
entry_year = tk.Entry(frame)
entry_year.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Calculate Age", command=calculate_age).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()