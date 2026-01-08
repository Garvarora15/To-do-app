tasks = []

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # File will be created later

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

tasks = []
def show_menu():
    print("\n        TO-DO LIST      ")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choise: ")
    
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        save_tasks()
        print("Task added")

    elif choice == "2":
        if not tasks:
            print("No tasks present")
        else:
         print("\n Your Tasks: ")
         for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        
    elif choice == "3":
        if not tasks:
            print("No tasks to delete")
        else:
            num = int(input("Enter the task number to be deleted: "))
            if 1 <= num <= len(tasks):
             tasks.pop(num - 1)
             print("Task deleted")
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("Exiting")
        break

else:
    print("Invalid choice")