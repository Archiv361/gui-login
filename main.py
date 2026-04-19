import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_entry.get()
    email = email_entry.get()
    messagebox.showinfo("Thankyou", f'Thankyou for submitting!\nName: "{name}"\nEmail: "{email}"')


root = tk.Tk()
root.title("Simple Login GUI")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="#2c3e50")

root.eval('tk::PlaceWindow . center')


header_label = tk.Label(root, text="User Information", font=("Arial", 20, "bold"), fg="white", bg="#2c3e50")
header_label.pack(pady=30)


name_frame = tk.Frame(root, bg="#2c3e50")
name_frame.pack(pady=10)
tk.Label(name_frame, text="Name:", font=("Arial", 12), fg="white", bg="#2c3e50").pack(side="left")
name_entry = tk.Entry(name_frame, font=("Arial", 12), width=25, justify="center")
name_entry.pack(side="right", padx=10)


email_frame = tk.Frame(root, bg="#2c3e50")
email_frame.pack(pady=10)
tk.Label(email_frame, text="Email:", font=("Arial", 12), fg="white", bg="#2c3e50").pack(side="left")
email_entry = tk.Entry(email_frame, font=("Arial", 12), width=25, justify="center")
email_entry.pack(side="right", padx=10)



submit_frame = tk.Frame(root, bg="#2c3e50")
submit_frame.pack(pady=30)
submit_btn = tk.Button(submit_frame, text="Submit", command=submit, font=("Arial", 12, "bold"), bg="#3498db", fg="white", width=25, cursor="hand2")
submit_btn.pack(side="right", padx=10)


name_entry.focus()


root.mainloop()

