class Task:
    def __init__(self , title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
    
    def mark_done(self):
        self.completed = True

    def __str__(self):
        status = "done" if self.completed else "pending"
        return f"[{self.priority}] {self.title} - {self.description} ({status})"
    
class TaskManager:
    def __init__(self , filename = "tasks.txt"):
        self.filename = filename
        self.tasks = []
        self.load_from_file()

    def add_task(self, title, description, priority):
        task = Task(title , description, priority)
        self.tasks.append(task)
        self.save_to_file()
        print(f"Task {title} added successfully!")

    def view_task(self):
        if not self.tasks:
            print("No tasks available")
            return
        for i, task in enumerate(self.tasks , 1):
            print(f"{i}. {task}")

    def mark_task_done(self,index):
        try:
            self.tasks[index - 1].mark_done()
            self.save_to_file()
            print("Task marked as done")
        except IndexError:
            print("Invalid task number")
    
    def delte_task(self,index):
        try :
            remove = self.tasks.pop(index-1)
            self.save_to_file()
            print(f"Task {remove.title} deleted successfully")
        except IndexError:
            print("Invalid task number")
    
    def save_to_file(self):
        with open(self.filename , "w" ) as f:
            for t in self.tasks:
                f.write(f"{t.title} | {t.description} | {t.priority} | {t.completed}\n")

    def load_from_file(self):
        try:
            with open(self.filename , "r") as f:
                for line in f:
                    title , description, priority , completed = line.strip().split("|")
                    task = Task(title, description, priority)
                    task.completed = completed == "true"
                    self.tasks.append(task)
        except FileNotFoundError:
            pass

def main():
    manager = TaskManager()
    while True:
        print("\n  ===== TaskFlow Pro Personal Task Manager =====")
        print("1. Add task")
        print("2.View task")
        print("3. Mark task as done")
        print("4.Delete task")
        print("5.Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Enter task title: ")
            description = input ("Enter title description: ")
            priority = input("Enter priority(High/Medium/Low): ")
            manager.add_task(title , description, priority)
        elif choice == "2":
            manager.view_task()
        elif choice == "3":
            manager.view_task()
            try: 
                index = int(input("Enter task numbeer as done: "))
                manager.mark_task_done(index)
            except ValueError:
                print("Enter a valid task number as done")
        elif choice == "4":
            manager.view_task()
            try:
                index = int(input("Enter a task number to delete: "))
                manager.delte_task(index)
            except ValueError:
                print("Enter a valid number!")
        elif choice == "5":
            print("EXITING.....")
            break
        else:
            print("Invalid choice! Try again.")
main()