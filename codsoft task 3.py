import random
import string
import tkinter as tk
from tkinter import messagebox


def generate_password():
    try:
        length = int(length_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid password length.")
        return

    pool = string.ascii_letters + string.digits
    password = ''.join(random.choices(pool, k=length))
    generated_password_label.config(text="Generated password: " + password)


def accept_password():
    username = username_entry.get()
    password = generated_password_label.cget("text").replace("Generated password: ", "")
    messagebox.showinfo("Accepted", f"Username: {username}\nPassword: {password}")


def reset():
    username_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    generated_password_label.config(text="Generated password: ")

window = tk.Tk()

window.title("Password Generator")

title_label = tk.Label(window, text="Password Generator", font=("Helvetica", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=10)

username_label = tk.Label(window, text="Username:")
username_label.grid(row=1, column=0, padx=10, pady=10, sticky="E")
username_entry = tk.Entry(window)
username_entry.grid(row=1, column=1, padx=10, pady=10, sticky="W")

length_label = tk.Label(window, text="Password Length:")
length_label.grid(row=2, column=0, padx=10, pady=10, sticky="E")
length_entry = tk.Entry(window)
length_entry.grid(row=2, column=1, padx=10, pady=10, sticky="W")

generated_password_label = tk.Label(window, text="Generated password:")
generated_password_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="W")

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, padx=10, pady=10, sticky="W")

accept_button = tk.Button(window, text="Accept", command=accept_password)
accept_button.grid(row=4, column=1, padx=10, pady=10, sticky="E")

reset_button = tk.Button(window, text="Reset", command=reset)
reset_button.grid(row=4, column=2, padx=10, pady=10)

window.mainloop()

