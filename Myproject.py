# Initialize an empty list to store tasks
to_do_list = []

# Function to add tasks to the list
def add_task(task):
    to_do_list.append(task)
    print(f'Task "{task}" added to the list.')

# Function to display all tasks
def display_tasks():
    if not to_do_list:
        print("No tasks in the to-do list.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(to_do_list, start=1):
            print(f"{index}. {task}")

# Function to remove a task by index
def remove_task(index):
    try:
        removed_task = to_do_list.pop(index - 1)
        print(f'Task "{removed_task}" removed from the list.')
    except IndexError:
        print("Invalid task number!")

# Main function to run the program in a loop
def to_do_app():
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. Display all tasks")
        print("3. Remove a task")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '2':
            display_tasks()
        elif choice == '3':
            display_tasks()
            if to_do_list:
                try:
                    task_number = int(input("Enter the task number to remove: "))
                    remove_task(task_number)
                except ValueError:
                    print("Please enter a valid number!")
        elif choice == '4':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the To-Do List Application
to_do_app()