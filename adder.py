import tkinter as tk
from tkinter import messagebox

def add_numbers():
    try:
        num1 = float(first_entry.get())
        num2 = float(second_entry.get())
        result = num1 + num2
        display_result = int(result) if result.is_integer() else result
        messagebox.showinfo("Result", f"Sum: {display_result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

root = tk.Tk()
root.title("Simple Adder")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#2c3e50")

root.eval('tk::PlaceWindow . center')

header_label = tk.Label(root, text="Simple Adder", font=("Arial", 20, "bold"), fg="white", bg="#2c3e50")
header_label.pack(pady=30)

first_frame = tk.Frame(root, bg="#2c3e50")
first_frame.pack(pady=10)
tk.Label(first_frame, text="First Number:", font=("Arial", 12), fg="white", bg="#2c3e50").pack(side="left")
first_entry = tk.Entry(first_frame, font=("Arial", 12), width=25, justify="center")
first_entry.pack(side="right", padx=10)

second_frame = tk.Frame(root, bg="#2c3e50")
second_frame.pack(pady=10)
tk.Label(second_frame, text="Second Number:", font=("Arial", 12), fg="white", bg="#2c3e50").pack(side="left")
second_entry = tk.Entry(second_frame, font=("Arial", 12), width=25, justify="center")
second_entry.pack(side="right", padx=10)

add_frame = tk.Frame(root, bg="#2c3e50")
add_frame.pack(pady=30)
add_btn = tk.Button(add_frame, text="Add", command=add_numbers, font=("Arial", 12, "bold"), bg="#3498db", fg="white", width=25, cursor="hand2")
add_btn.pack(side="right", padx=10)

first_entry.focus()

root.mainloop()
