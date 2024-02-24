
#A list variable for storing the tasks from the user.
tasks = []

#Functions
#adds a task to the task list with the "append" method, by taking the users input for the task description.
def add_task(description):
    tasks.append({"description": description, "completed": False})

#Asks user for index of task they want to set to True for "Completion"
def complete_task(task_index):
    tasks[task_index]["completed"] = True

#This line is asking the index of task that they want to remove.
def remove_task(task_index):
    del tasks[task_index]

#This function sets the completion propertyof all tasks to false.
def reset_tasks():
    for task in tasks:
        task["completed"] = False

#Mr.Sabo wrote this code 
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

        #takes users input and determines which function gets called based on the input
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

        #If user doesn't type add/complete/remove/reset/quit, then they get an error.
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()