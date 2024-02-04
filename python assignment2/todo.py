#to-do list
class ToDo:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append([task, False])

    def mark_task_as_completed(self, task):
        for t in self.tasks:
            if t[0] == task:
                t[1] = True

    def display_tasks(self):
        for task, is_completed in self.tasks:
            status = "Completed" if is_completed else "Not Completed"
            print(f"Task: {task}, Status: {status}")

Homework = ToDo()
Homework.add_task("Do math homework")
Homework.mark_task_as_completed("Do math homework")
Homework.display_tasks()


        
    
        
        
