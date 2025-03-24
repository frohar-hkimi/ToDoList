import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter.font import Font
from datetime import datetime, date


class Task:
    def __init__(self, name, due_date, status='Pending'):
        self.name = name
        self.due_date = due_date
        self.status = status

    def mark_complete(self):
        self.status = "Completed"

    def edit_task(self, new_name=None, new_due_date=None, new_status=None):
        self.name = new_name if new_name else self.name
        self.due_date = new_due_date if new_due_date else self.due_date
        self.status = new_status if new_status else self.status

    def display_task(self):
        return f"{self.name} | Due: {self.due_date} | Status: {self.status}"


class ToDoList:
    def __init__(self):
        self.tasks = []  # List of Task objects

    def add_task(self, task):
        if isinstance(task, Task):
            self.tasks.append(task)

    def remove_task(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                self.tasks.remove(task)
                return True
        return False

    def mark_task_complete(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.mark_complete()
                return True
        return False

    def display_tasks(self):
        return [task.display_task() for task in self.tasks]


# ----------------- Tkinter GUI -----------------

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo List App")
        self.root.geometry("500x500")

        self.todo_list = ToDoList()

        # Font
        self.my_font = Font(family="Arial", size=12, weight="bold")

        # Frame for Listbox
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        # Listbox
        self.listbox = tk.Listbox(
            self.frame, font=self.my_font, width=50, height=10, bg="white"
        )
        self.listbox.pack()

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.refresh_button = tk.Button(self.root, text="Refresh List", command=self.refresh_list)
        self.refresh_button.pack(pady=5)

    def add_task(self):
        task_name = simpledialog.askstring("Task Name", "Enter Task Name:")
        if not task_name:
            return
        due_date = simpledialog.askstring("Due Date", "Enter Due Date (dd/mm/yyyy):")
        due_date = datetime.strptime(due_date, "%d/%m/%Y").date()
        if due_date < date.today():
            return messagebox.showinfo("Failed", f"'{due_date}' is in the past!")
        if not due_date:
            return

        new_task = Task(task_name, due_date)
        self.todo_list.add_task(new_task)
        self.refresh_list()

    def remove_task(self):
        try:
            selected_task = self.listbox.get(self.listbox.curselection())
            task_name = selected_task.split(" | ")[0]

            if self.todo_list.remove_task(task_name):
                messagebox.showinfo("Success", f"Task '{task_name}' removed!")
            else:
                messagebox.showerror("Error", f"Task '{task_name}' not found!")
        except:
            messagebox.showerror("Error", "No task selected!")

        self.refresh_list()

    def mark_completed(self):
        try:
            selected_task = self.listbox.get(self.listbox.curselection())
            task_name = selected_task.split(" | ")[0]

            if self.todo_list.mark_task_complete(task_name):
                messagebox.showinfo("Success", f"Task '{task_name}' marked as Completed!")
            else:
                messagebox.showerror("Error", f"Task '{task_name}' not found!")
        except:
            messagebox.showerror("Error", "No task selected!")

        self.refresh_list()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for task in self.todo_list.display_tasks():
            self.listbox.insert(tk.END, task)


# Run the Tkinter App
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
