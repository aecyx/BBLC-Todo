#variables
tasks = []

#functions

def add_task(description):
    tasks.append([{"description" : description, "completed" : False}])

def remove_task(task_index):
    del tasks[task_index]
#write code here
    