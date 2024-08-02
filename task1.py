def main():
    tasks = []

    while True:
        print("\n<<<<<<<<<<<<\t To-Do List\t>>>>>>>>>>>>")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. remove")
        print("4. Exit")

        choice = input("Enter your choice number:  ")

        if choice == '1':
            print()
            n_tasks = int(input("How may task you want to add ?:  "))
            
            for i in range(n_tasks):
                task = input("Enter the task:  ")
                tasks.append(task)
                print("Task added successfully!")

        elif choice == '2':
            print("The Entered tasks")
            for index, task in enumerate(tasks):
                print(index+1,'.', task)

        elif choice == '3':
            try:
                r_task = int(input("Enter the task number to remove: "))
                if 1 <= r_task < len(tasks):
                    remove_task=tasks.pop(r_task - 1)
                    print("The task",remove_task, "is removed!")
                else:
                    print("\n Invalid task number.","\n Please check")
            except ValueError:
                print("Please enter a valid number.")
                print()               

                    
        elif choice == '4':
            print("Exiting the To-Do List Appliction.")
            print("\n THANK YOU")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
