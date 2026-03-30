import tkinter as tk

def calculate_product():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    output.delete("1.0", tk.END)
    output.insert(tk.END, str(result))

root = tk.Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")

label_desc = tk.Label(root, text="Enter two numbers to calculate their product")
label_desc.pack()

label1 = tk.Label(root, text="Enter first number:")
label1.pack()

entry1 = tk.Entry(root)
entry1.pack()

label2 = tk.Label(root, text="Enter second number:")
label2.pack()

entry2 = tk.Entry(root)
entry2.pack()

button = tk.Button(root, text="Calculate Product", command=calculate_product)
button.pack()

output = tk.Text(root, height=2, width=20)
output.pack()

root.mainloop()