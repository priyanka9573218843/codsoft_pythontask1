tasks = []
def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added to the list.")
def complete_task(task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        print(f"Task '{completed_task}' marked as completed.")
    else:
        print("Invalid task index.")
# Main loop
while True:
    print("\nMenu:")
    print("1. Show To-Do List")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter the task: ")
        add_task(task)
    elif choice == '3':
        task_index = int(input("Enter the task number to mark as completed: "))
        complete_task(task_index)
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
