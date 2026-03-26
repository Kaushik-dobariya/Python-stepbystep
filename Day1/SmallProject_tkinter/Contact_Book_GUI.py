import tkinter as tk
from tkinter import messagebox

# File to store contacts
FILE_NAME = "contacts.txt"

contacts = []

# ---------------- FILE HANDLING ----------------
def load_contacts():
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts.append((name, phone))
    except FileNotFoundError:
        pass


def save_contacts():
    with open(FILE_NAME, "w") as file:
        for contact in contacts:
            file.write(contact[0] + "," + contact[1] + "\n")

# ---------------- FUNCTIONS ----------------
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Error", "Please fill all fields!")
        return

    contacts.append((name, phone))
    save_contacts()
    display_contacts()

    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Contact added!")
    
def display_contacts():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact[0]}   📞 {contact[1]}")


def search_contact():
    search = search_entry.get().lower()
    listbox.delete(0, tk.END)

    for contact in contacts:
        if search in contact[0].lower():
            listbox.insert(tk.END, f"{contact[0]}   📞 {contact[1]}")


def delete_contact():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Error", "Select a contact!")
        return

    index = selected[0]
    del contacts[index]

    save_contacts()
    display_contacts()

    messagebox.showinfo("Deleted", "Contact removed!")   
    
# ---------------- GUI DESIGN ----------------
root = tk.Tk()
root.title("📒 Smart Contact Book")
root.geometry("420x500")
root.config(bg="#1e1e2f")

# Title
tk.Label(root, text="📒 Contact Book", font=("Arial", 18, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=10)

# Frame for inputs
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

# Name
tk.Label(frame, text="Name", bg="#1e1e2f", fg="white").grid(row=0, column=0)
name_entry = tk.Entry(frame, width=20)
name_entry.grid(row=0, column=1, padx=10)

# Phone
tk.Label(frame, text="Phone", bg="#1e1e2f", fg="white").grid(row=1, column=0)
phone_entry = tk.Entry(frame, width=20)
phone_entry.grid(row=1, column=1, padx=10)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=10, bg="#4CAF50", fg="white",
          command=add_contact).grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="View", width=10, bg="#2196F3", fg="white",
          command=display_contacts).grid(row=0, column=1, padx=5)

tk.Button(btn_frame, text="Delete", width=10, bg="#f44336", fg="white",
          command=delete_contact).grid(row=0, column=2, padx=5)

# Search Bar
search_entry = tk.Entry(root, width=30)
search_entry.pack(pady=10)

tk.Button(root, text="Search", bg="#9C27B0", fg="white",
          command=search_contact).pack()

# Listbox
listbox = tk.Listbox(root, width=45, height=15, bg="#2e2e3e", fg="white")
listbox.pack(pady=15)

# Load contacts at start
load_contacts()
display_contacts()

# Run app
root.mainloop()