import tkinter as tk
from tkinter import messagebox

tasks = {}

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                line = line.strip()
                if "|" in line:          # ✅ validation
                    task, status = line.split("|", 1)
                    tasks[task] = status
    except FileNotFoundError:
        pass


def save_tasks():
    with open("tasks.txt", "w") as file:
        for task, status in tasks.items():
            file.write(f"{task}|{status}\n")

def add_task():
    task = entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Task cannot be empty!")
    else:
        tasks[task] = "Pending"
        save_tasks()
        entry.delete(0, tk.END)
        update_listbox()

def mark_done():
    try:
        selected = listbox.curselection()[0]
        task = list(tasks.keys())[selected]
        tasks[task] = "Done"
        save_tasks()
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        task = list(tasks.keys())[selected]
        del tasks[task]
        save_tasks()
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a task!")

def update_listbox():
    listbox.delete(0, tk.END)
    for task, status in tasks.items():
        listbox.insert(tk.END, f"{task} [{status}]")

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add_task).pack()

listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

tk.Button(root, text="Mark as Done", command=mark_done).pack(pady=5)
tk.Button(root, text="Delete Task", command=delete_task).pack()

load_tasks()
update_listbox()
root.mainloop()
