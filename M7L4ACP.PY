import tkinter as tk

def calculate_interest():
    p = float(entry_principal.get())
    t = float(entry_time.get())
    r = float(entry_rate.get())

    simple_interest = (p * t * r) / 100
    compound_interest = p * ((1 + r/100) ** t) - p

    result_label.config(
        text=f"Simple Interest: {simple_interest}\nCompound Interest: {compound_interest}"
    )

root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Principal").grid(row=0, column=0, padx=10, pady=10)
entry_principal = tk.Entry(frame)
entry_principal.grid(row=0, column=1, padx=10, pady=10)

tk.Label(frame, text="Time (years)").grid(row=1, column=0, padx=10, pady=10)
entry_time = tk.Entry(frame)
entry_time.grid(row=1, column=1, padx=10, pady=10)

tk.Label(frame, text="Rate (%)").grid(row=2, column=0, padx=10, pady=10)
entry_rate = tk.Entry(frame)
entry_rate.grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Calculate", command=calculate_interest).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

root.mainloop()