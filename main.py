import json
import os

def view_tasks():
    with open("tasks.json", "r") as file:
        data = json.load(file)

    print(f"{'ID':<6}{'Task Name':<30}{'Status':<15}")
    print("-" * 51)

    for task in data:
        print(f"{task['id']:<6}{task['Taskname']:<30}{task['status']:<15}")


def add_task():
  
    with open("tasks.json", "r") as file:
        data = json.load(file)

    task_name = input("Enter task name: ").strip()

    if not task_name:
        print("Task name cannot be empty.")
        return

    next_id = max((task["id"] for task in data), default=0) + 1

    new_task = {
        "id": next_id,
        "Taskname": task_name,
        "status": "Pending"
    }

    data.append(new_task)

    with open("tasks.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Task added successfully!")

def complete_task():
    with open("tasks.json", "r") as file:
            data = json.load(file)

    selected_task = int(input("Select the id of task you wish to mark complete: "))
    for task in data:
        if task["id"] == selected_task:

            if (task["status"] == "complete"):
                print("Task already marked as completed")
            else:
                task["status"] = "complete"
   
    with open('tasks.json', 'w') as f:
        json.dump(data, f)

def delete_task():
    with open("tasks.json", "r") as file:
        data = json.load(file)

    selected_task = int(input("Select the id of task you wish to delete: "))
    for task in data:
            if task["id"] == selected_task:
                data.remove(task)

    with open('tasks.json', 'w') as f:
            json.dump(data, f)
               

    

    






def display_menu():
    
    
    print("\n===== TASK MANAGER =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    print("========================")



while True:
    display_menu()
    choice = (int(input("Select an option: ")))

    match choice:
        case 1:
            print("viewing tasks...")
            os.system("cls")
            view_tasks()
        case 2: 
            print("Adding tasks...")
            os.system("cls")
            add_task()
        case 3:
            print("Completing tasks...")
            os.system("cls")
            complete_task()
        case 4:
            print("Deleting tasks...")
            os.system("cls")
            delete_task()
        case 5:
            print("exiting")
            break

        
