import os

print("This is yor to do list application. What would you like to do?")

todo = {"task1": False}


def menu():
    os.system("clear")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Exit")
    print()

    def take_input():
        i = input("Please select an option (1-5): ")
        os.system("clear")
        if i == "1":
            add_task()
        elif i == "2":
            view_tasks()
        elif i == "3":
            mark_task_complete()
        elif i == "4":
            delete_task()
        elif i == "5":
            print("Goodbye!")
            exit()
        else:
            print("Invalid option. Please try again.")
            take_input()

    take_input()


def add_task():
    print("Please enter the task you want to add:")
    task = input()
    todo[task] = False
    print(f"Task '{task}' added.")
    print()
    input("Press Enter to continue...")
    menu()


def view_tasks():
    print("Here are your tasks:")
    print()
    for task, done in todo.items():
        status = "Done" if done else "Not done"
        print(f"{task}: {status}")
    print()
    input("Press Enter to continue...")
    menu()
    # This should display the list of tasks


def mark_task_complete():
    print("Please enter the task you want to mark as complete:")
    task = input()
    try:
        if todo[task]:
            print("task is done")
        else:
            todo[task] = True
    except KeyError:
        print("Task not found.")
        print()
        input("Press Enter to continue...")
        menu()
        return
    todo[task] = True
    print(f"Task '{task}' marked as complete.")

    print()
    input("Press Enter to continue...")
    menu()
    # This should mark the task as complete


def delete_task():
    print("Please enter the task you want to delete:")
    task = input()
    try:
        del todo[task]
        print(f"Task: {task} has been deleted")
        input("\nPress enter to continue...")
        menu()
    except KeyError:
        print("Could not find task.")
        input("\nPress enter to continue...")
        menu()
        return

    print()
    input("Press Enter to continue...")
    menu()
    # This should delete the task


menu()
