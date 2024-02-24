
#A list variable for storing the tasks from the user.
tasks = []

def add_task(description):
    tasks.append({"description": description, "completed": False})

def complete_task(task_index):
    tasks[task_index]["completed"] = True

def remove_task(task_index):
    del tasks[task_index]

def reset_tasks():
    for task in tasks:
        task["completed"] = False

def save_tasks(filename):
    with open(filename, "w") as f:
        for task in tasks:
            f.write(task["description"] + "," + str(task["completed"]) + "\n")

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

        if choice == "add":
            description = input("Enter task description: ")
            add_task(description)
        
        elif choice == "complete":
            task_index = int(input("Enter task index to complete: ")) - 1
            complete_task(task_index)
        
        elif choice == "reset":
            reset_tasks()
            print("Tasks completion status reset.")
        
        elif choice == "remove":
            task_index = int(input("Enter task index to remove: ")) - 1
            remove_task(task_index)

        elif choice == "quit":
            save_tasks(filename)
            print("Quitting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()