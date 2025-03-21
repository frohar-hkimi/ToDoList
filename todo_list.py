class Task:
    def __init__(self, name, due_date, status='Pending'):
        self.name = name 
        self.due_date = due_date
        self.status = status 
        self.tasks =  []

    def mark_complete(self):
        if self.status != "Completed":
            self.status = "Completed"
        return self.status

    def edit_task(self, new_name=None, new_due_date=None, new_status=None):
        self.name = new_name if new_name is not None else self.name
        self.due_date = new_due_date if new_due_date is not None else self.due_date
        self.status = new_status if new_status is not None else self.status

        return f"Updated Task: {self.name} | Due: {self.due_date} | Status: {self.status}"

    def display_task(self):
        return f"Task: {self.name} | Due: {self.due_date} | Status: {self.status}"

class ToDoList:
    def __init__(self, title="My To-Do List"):
        self.title = title
        self.tasks = []  # List of Task objects
    
    def add_task(self, task):
        if isinstance(task, Task):  # Ensure only Task objects are added
            if task not in self.tasks:
                self.tasks.append(task)
                return f"Task '{task.name}' added!"
            else:
                return f"Task '{task.name}' is already in the list."
        else:
            return "Error: Only Task objects can be added."


    def remove_task(self, task):
        if isinstance(task, Task):  # Ensure only Task objects are added
            if task in self.tasks:
                self.tasks.remove(task)
                return f"Task '{task.name}' has been removed from list."
            else:
                return f"Task '{task.name}' does not exist in list, therefore cannot be removed."
        else:
            return "Error: Only Task objects can be added."
    

    def display_tasks(self):
        if len(self.tasks) == 0:
            return 'There are no tasks'
        else:
            tasks_display = ""
            for task in self.tasks:
                tasks_display += task.display_task() + "\n"
            return tasks_display.strip()
    
    def get_tasks(self, status = 'Pending'):
        matched_tasks = []
        for task in self.tasks:
            if task.status == status:
                matched_tasks.append(task.name)
        
        if len(matched_tasks) > 0:
            return f"Task '{matched_tasks}' are all tasks with status {status}"    # Return the tasks in the list
        else:
            return f"No tasks with status '{status}'."

# firstly defining the tasks 
laundry = Task('Laundry', '20/01/2025', 'Completed')  
washing_up = Task('Washing up', '21/01/2024', 'Completed')
homework = Task('homework', '25/01/2024', 'Completed')

# defining to do list class
to_do_list = ToDoList()

# performing actions
print(to_do_list.add_task(laundry))
print(to_do_list.add_task(washing_up))
print(to_do_list.add_task(homework))
print(to_do_list.get_tasks('Completed'))
print(to_do_list.display_tasks())

# this is some change i'd like to make

# NEXT STEP CREATE UI, INPUT ECT TO PUT ALL OF IT TOGETHER


