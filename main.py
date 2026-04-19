import tkinter as tk
from tkinter import messagebox

def submit():
    name = name_entry.get()
    email = email_entry.get()
    messagebox.showinfo("Thankyou", f'Thankyou for submitting!\nName: "{name}"\nEmail: "{email}"')

def toggle_red_bg():
    current_bg = root.cget('bg')
    new_bg = 'red' if current_bg == '#2c3e50' else '#2c3e50'
    
    # Update root and propagate to frames/labels/entries
    root.configure(bg=new_bg)
    header_label.configure(bg=new_bg)
    name_frame.configure(bg=new_bg)
    name_frame.winfo_children()[0].configure(bg=new_bg, fg='white')  # Name label
    name_entry.configure(bg=new_bg if new_bg == 'red' else 'white')
    email_frame.configure(bg=new_bg)
    email_frame.winfo_children()[0].configure(bg=new_bg, fg='white')  # Email label
    email_entry.configure(bg=new_bg if new_bg == 'red' else 'white')
    submit_frame.configure(bg=new_bg)
    
    # Buttons stay their fixed colors

root = tk.Tk()
root.title("Simple Login GUI")
root.geometry("400x350")
root.resizable(False, False)
root.configure(bg="#2c3e50")

root.eval('tk::PlaceWindow . center')

header_label = tk.Label(root, text="User Information", font=("Arial", 20, "bold"), fg="white", bg="#2c3e50")
header_label.pack(pady=30)

name_frame = tk.Frame(root, bg="#2c3e50")
name_frame.pack(pady=10)
tk.Label(name_frame, text="Name:", font=("Arial", 12), fg="white", bg="#2c3e50").pack(side="left")
name_entry = tk.Entry(name_frame, font=("Arial", 12), width=25, justify="center", bg='white')
name_entry.pack(side="right", padx=10)

email_frame = tk.Frame(root, bg="#2c3e50")
email_frame.pack(pady=10)
tk.Label(email_frame, text="Email:", font=("Arial", 12), fg="white", bg="#2c3e50").pack(side="left")
email_entry = tk.Entry(email_frame, font=("Arial", 12), width=25, justify="center", bg='white')
email_entry.pack(side="right", padx=10)

submit_frame = tk.Frame(root, bg="#2c3e50")
submit_frame.pack(pady=30)
submit_btn = tk.Button(submit_frame, text="Submit", command=submit, font=("Arial", 9, "bold"), bg="#3498db", fg="white", width=8, cursor="hand2", relief="raised")
submit_btn.pack(side="right", padx=5)
red_btn = tk.Button(submit_frame, text="Red", command=toggle_red_bg, font=("Arial", 9, "bold"), bg="red", fg="white", width=8, cursor="hand2", relief="raised")
red_btn.pack(side="right", padx=5)

name_entry.focus()

root.mainloop()
