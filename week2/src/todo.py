#!/usr/bin/env python

tasks = []

def show_menu():
    print("\nTo-Do App")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def remove_task():
    view_tasks()
    try:
        task_number = int(input("Enter task number to remove: "))
        tasks.pop(task_number - 1)
        print("Task removed.")
    except (ValueError, IndexError):
        print("Invalid selection.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
