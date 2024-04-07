class Tasks:
    def __init__(self, tasks_display):
        self.tasks_display = tasks_display
        self.all_tasks = []
    
    def create_task(self, create):
        self.all_tasks.append(create)
        return self.all_tasks
    
    def remove_task(self, dele):
        self.all_tasks.remove(dele)
        return self.all_tasks
    
    def list_display_tasks(self):
        for task in self.all_tasks:
            return task
    
    def __repr__(self):
        return self.tasks_display
    
if __name__=='__main__':
    Task1 = Tasks("Hello")
    print(Task1.create_task("First task"))
    print(Task1.create_task("Second tasks"))
    print(Task1.create_task("Third tasks"))
    print(Task1.remove_task("First task"))
    print(Task1.list_display_tasks())
        