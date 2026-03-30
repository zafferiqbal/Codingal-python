import tkinter as tk

def convert_length():
    value = float(entry_value.get())
    meters = value
    kilometers = meters / 1000
    centimeters = meters * 100

    result_label.config(
        text=f"{meters} m = {kilometers} km\n{meters} m = {centimeters} cm"
    )

root = tk.Tk()
root.title("Length Converter App")
root.geometry("400x400")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Enter length in meters:").grid(row=0, column=0, padx=10, pady=10)
entry_value = tk.Entry(frame)
entry_value.grid(row=0, column=1, padx=10, pady=10)

tk.Button(root, text="Convert", command=convert_length).pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=20)

root.mainloop()