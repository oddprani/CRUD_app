import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

DATA_FILE = "todo.json"

# Load tasks from JSON
def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

# Save tasks to JSON
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as file:
        json.dump(tasks, file)

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App (CRUD)")

        self.tasks = load_tasks()

        # UI Components
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_btn = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_btn.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)
        self.refresh_task_list()

        self.update_btn = tk.Button(root, text="Update Task", command=self.update_task)
        self.update_btn.pack(pady=5)

        self.delete_btn = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_btn.pack(pady=5)

    def refresh_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            save_tasks(self.tasks)
            self.task_entry.delete(0, tk.END)
            self.refresh_task_list()
        else:
            messagebox.showwarning("Empty Task", "Task cannot be empty.")

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            current_task = self.tasks[selected_index[0]]
            new_task = simpledialog.askstring("Update Task", "Edit task:", initialvalue=current_task)
            if new_task:
                self.tasks[selected_index[0]] = new_task.strip()
                save_tasks(self.tasks)
                self.refresh_task_list()
        else:
            messagebox.showinfo("Select Task", "Please select a task to update.")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            task = self.tasks.pop(selected_index[0])
            save_tasks(self.tasks)
            self.refresh_task_list()
        else:
            messagebox.showinfo("Select Task", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
