import json
import os

# File to store tasks
TASK_FILE = "tasks.json"

# Initialize the tasks file if not present
def initialize_tasks_file():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w') as file:
            json.dump([], file)

# Load tasks from the file
def load_tasks():
    with open(TASK_FILE, 'r') as file:
        return json.load(file)

# Save tasks to the file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a task
def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {"title": title, "description": description, "completed": False}
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

# View all tasks
def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks available.")
        return
    for idx, task in enumerate(tasks, start=1):
        status = "✔️" if task["completed"] else "❌"
        print(f"{idx}. {task['title']} - {task['description']} [{status}]")

# Update a task
def update_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_index = int(input("Enter the task number to update: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks[task_index]["title"] = input("Enter new title: ") or tasks[task_index]["title"]
            tasks[task_index]["description"] = input("Enter new description: ") or tasks[task_index]["description"]
            tasks[task_index]["completed"] = input("Mark as completed? (yes/no): ").strip().lower() == "yes"
            save_tasks(tasks)
            print("Task updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

# Delete a task
def delete_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(tasks):
            tasks.pop(task_index)
            save_tasks(tasks)
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input.")

# Main menu
def main_menu():
    initialize_tasks_file()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
