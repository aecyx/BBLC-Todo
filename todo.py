#variables
tasks = []

#functions

def add_task(description):
    tasks.append([{"description" : description, "completed" : False}])

def remove_task(task_index):
    del tasks[task_index]

def complete_task(task_index):
    tasks[task_index]["completed"] = True

def reset_tasks():
    for task in tasks:
        task["completed"] = False

def save_tasks(filename):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(task[:"description"] + "," + str(task["completed"]) + "\n")

def load_tasks(filename):
    tasks.clear()
    try:
        with open(filename, "r") as f:
            for line in f:
                description, completed = line.strip().split(",")
                tasks.append({"description": description, "completed": completed == "True"})
    except FileNotFoundError:
        open(filename, "a").close()

def main():
    filename = "tasks.txt"
    load_tasks(filename)

    while True:
        print("To-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}, [{task['completed']}] {task['description']}")

        choice = input("Enter your choice (add/complete/remove/reset/quit): ").lower()

        