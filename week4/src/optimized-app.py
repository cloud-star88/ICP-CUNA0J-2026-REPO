#!/usr/bin/env python

def show_menu():
    """Displays the main menu options to the user."""
    print("\nTo-Do App")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

def add_task(tasks):
    """
    Prompts the user to enter a task and adds it to the task list.
    Input is validated to prevent empty tasks.
    """
    task = input("Enter task: ").strip()

    if not task:
        print("Task cannot be empty.")
        return

    tasks.append(task)
    print("Task added successfully.")

def view_tasks(tasks):
    """
    Displays all tasks in the list.
    If no tasks exist, notifies the user.
    """
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def remove_task(tasks):
    """
    Removes a task selected by the user.
    Validates input to ensure a valid task number is provided.
    """
    if not tasks:
        print("No tasks to remove.")
        return

    view_tasks(tasks)

    try:
        task_number = int(input("Enter task number to remove: "))

        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Removed task: {removed_task}")
        else:
            print("Task number out of range.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """
    Main application loop.
    Initializes task storage and handles user menu selection.
    """
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")

if __name__ == "__main__":
    main()
