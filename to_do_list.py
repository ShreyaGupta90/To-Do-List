# Simple To-Do List Python Application

todo_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")

def add_task():
    task = input("Enter the task you want to add: ")
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def delete_task():
    view_tasks()
    if todo_list:
        try:
            task_num = int(input("\nEnter the number of the task to delete: "))
            if 1 <= task_num <= len(todo_list):
                deleted_task = todo_list.pop(task_num - 1)
                print(f"Task '{deleted_task}' has been deleted.")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("Goodbye! Have a great day!\n")
            break
        else:
            print("Invalid choice. Please choose a valid option (1-4).")

if __name__ == "__main__": #if condition is not necessary you can simply call main function too...
    main()