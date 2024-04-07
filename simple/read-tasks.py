class Tasks:
    def __init__(self, tasks_display):
        self.tasks_display = tasks_display 
    
    # def create_task(self, create):
    #     self.display.append("First Task")
    #     return self.display

    def view_tasks(self):
        self.view = self.display
        return self.view
    
    def __repr__(self):
        return self.tasks_display
    
if __name__=='__main__':
    Task1 = Tasks("First Task")
    print(Task1)
        