import tkinter as tk

def submit_task():
    task = entry.get()
    if task:
        label.config(text="Task: " + task)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(
    frame,
    text="Add Item:",
    font=("Courier New", 12)
)
label.pack(side=tk.LEFT)

entry = tk.Entry(
    frame,
    font=("Courier New", 12)
)
entry.pack(side=tk.LEFT)

submit_button = tk.Button(
    root,
    text="Submit",
    command=submit_task,
    font=("Courier New", 12)
)
submit_button.pack(pady=10)

root.mainloop()
