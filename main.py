# Define an empyt list to hold our tasks
tasks = []

# Define a function to add tasks to our lists
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.")
    

# Define a function to remove tasks from list
def remove_task():
    try:
        if len(tasks) == 0:
            print("There are no more tasks to remove")
            return

        index = input("Enter the index of the list you want to remove: ")
        if index < 0 or index >= len(tasks):
            print("The tasks index you entered is invalid.")
            return

        task = tasks.pop(index)
        print(f"Task '{task}' removed successfully.")
    except:
        print("Invalid task index entered!")

# Define a function to list all tasks
def list_tasks():
    if len(tasks) == 0:
        print("There are no tasks.")
        return

    print("Tasks")
    for i, task in enumerate(tasks):
        print(f"{i}. {task}")


# Define a function to list all tasks
def show_menu():
    print("\n=============Todo List=============\n")
    print("1. Add task")
    print("2. Remove task")
    print("3. List tasks")
    print("4. Quit")
    
    
# Loop to show the menu and executes options
while True:
    show_menu()
    
    chioce = input("\nEnter your choice: ")
    if chioce == '1':
        add_task()
    elif chioce == '2':
        remove_task()
    elif chioce == '3':
        list_tasks()
    elif chioce == '4':
        break
    else:
        print("Invalid choice.")