import os

user_database = {}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def register():
    clear_screen()
    print("REGISTER MENU\n")
    print("PLEASE INPUT INFORMATION")
    username = input("\nUSERNAME (Leave Blank to go BACK): ").strip()
    if not username:
        return
    if username in user_database:
        print("Username already taken")
        input("Press Enter to continue...")
        return

    while True:
        password = input("PASSWORD (Must be 8 characters Long): ").strip()
        if len(password) >= 8:
            print("Password saved")
            break
        else:
            print("Password must be 8 characters long")
    
    user_database[username] = {
        "username": username,
        "password": password,
    }

    print(f"\n\nHello {username}! You have successfully registered!")
    input("Press Enter to continue...")

def userlog():
    clear_screen()
    print("USER LOG IN MENU")
    print("Please Input Your Account Information")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in user_database and user_database[username]["password"] == password:
        print(f"Hello {username}! You Have Successfully Logged In!")
        input("Press Enter to Continue...")
        user_menu(username)
    elif username not in user_database:
        print("No Account Found")
        input("Press Enter to Continue...")
    else:
        print("Incorrect Password")
        input("Press Enter to Continue...")

def calc(username):
    while True:
        try:
            clear_screen()
            print("CALCULATOR\n\n")
            num1 = float(input("1st Number: ")) 
            op = input("Select Operation (+, -, /, *, ^): ")
            num2 = float(input("2nd Number: ")) 
            
            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                if num2 != 0:  
                    result = num1 / num2
                else:
                    print("Error: Division by zero")
                    continue  
            elif op == '^':
                result = num1 ** num2
            else:
                print("Invalid operation selected.")
                continue  
            
            print("Result:", result)
            
            choice = input("Do you want to continue? (yes/no): ")
            if choice.lower() != 'yes':
                print("Goodbye,", username + "!")
                break  
        except ValueError:
            print("Please enter valid numeric inputs.")
        except Exception as e:
            print("An error occurred:", str(e))


def taskM(username, tasks):
    while True:
        clear_screen()  # Clear the screen at the beginning of the loop
        try:
            print("\nTASK MANAGER")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Go Back")

            choice = input("Please enter your choice: ")

            if choice == "1":
                task = input("Enter the task: ")
                tasks.append(task)
                print("Task added successfully.")
                input("Press Enter to continue...")  # Add a pause before clearing
            elif choice == "2":
                clear_screen()  # Clear the screen before displaying tasks
                if tasks:
                    print("Your tasks:")
                    for index, task in enumerate(tasks, start=1):
                        print(f"{index}. {task}")
                else:
                    print("No tasks available.")
                input("Press Enter to continue...")  # Add a pause
            elif choice == "3":
                if tasks:
                    print("Your tasks:")
                    for index, task in enumerate(tasks, start=1):
                        print(f"{index}. {task}")
                    task_index = int(input("Enter the task number you want to delete: ")) - 1
                    if 0 <= task_index < len(tasks):
                        del tasks[task_index]
                        print("Task deleted successfully.")
                    else:
                        print("Invalid task number.")
                else:
                    print("No tasks available to delete.")
                input("Press Enter to continue...")  # Add a pause
            elif choice == "4":
                print("Going back to the main menu...")
                break
            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to continue...")
        except ValueError:
            print("Invalid input. Please enter a number.")

def notepad(username):
    notes = []

    while True:
        try:
            clear_screen()
            print("NOTEPAD\n")
            print("1. Add Note")
            print("2. View Notes")
            print("3. Delete Note")
            print("4. Go Back")

            choice = input("Please enter your choice: ")

            if choice == "1":
                clear_screen()
                print("NOTEPAD - Add Note\n")
                note = input("Enter your note: ")
                notes.append(note)
                print("Note added successfully.")
                input("Press Enter to continue...")
            elif choice == "2":
                clear_screen()
                print("NOTEPAD - View Notes\n")
                if notes:
                    for i, note in enumerate(notes, start=1):
                        print(f"{i}. {note}")
                else:
                    print("No notes available.")
                input("\nPress Enter to continue...")
            elif choice == "3":
                clear_screen()
                print("NOTEPAD - Delete Note\n")
                if notes:
                    for i, note in enumerate(notes, start=1):
                        print(f"{i}. {note}")
                    try:
                        note_index = int(input("Enter the note number you want to delete: ")) - 1
                        if 0 <= note_index < len(notes):
                            del notes[note_index]
                            print("Note deleted successfully.")
                        else:
                            print("Invalid note number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                else:
                    print("No notes available to delete.")
                input("\nPress Enter to continue...")
            elif choice == "4":
                print("Going back to the main menu...")
                break
            else:
                print("Invalid choice. Please try again.")
                input("Press Enter to continue...")
        except ValueError:
            print("Invalid Input")
            print("Enter to continue")
            input()

def flashcards(username):
    topics = {}

    while True:
        try:
            clear_screen()
            print("FLASHCARDS\n")
            print("1. Create Flashcards")
            print("2. View Topics")
            print("3. Answer Flashcards")
            print("4. Go Back")

            choice = input("Please enter your choice: ")

            if choice == "1":
                clear_screen()
                print("FLASHCARDS - Create Flashcards\n")
                topic_name = input("Enter the topic name: ")
                if topic_name in topics:
                    print("Topic already exists. Adding cards to existing topic.")
                else:
                    topics[topic_name] = []
                while True:
                    question = input("Enter the question (type 'exit' to stop adding cards): ")
                    if question.lower() == 'exit':
                        break
                    answer = input("Enter the answer: ")
                    topics[topic_name].append((question, answer))
                    print("Card added successfully.")
                    input("\nPress Enter to continue...")
            elif choice == "2":
                clear_screen()
                print("FLASHCARDS - View Topics\n")
                if topics:
                    print("Available Topics:")
                    for topic in topics:
                        print("-", topic)
                        input("\nPress Enter to continue...")
                else:
                    print("No topics available.")
                    input("\nPress Enter to continue...")
            elif choice == "3":
                clear_screen()
                print("FLASHCARDS - Answer Flashcards\n")
                if topics:
                    print("Available Topics:")
                    for topic in topics:
                        print("-", topic)
                    selected_topic = input("\nEnter the topic name to answer flashcards (type 'exit' to go back): ")
                    if selected_topic.lower() == 'exit':
                        continue
                    elif selected_topic in topics:
                        clear_screen()
                        print(f"FLASHCARDS - {selected_topic}\n")
                        if topics[selected_topic]:
                            for i, (question, answer) in enumerate(topics[selected_topic], start=1):
                                print(f"Question {i}: {question}")
                                while True:
                                    user_answer = input("Your Answer (type 'next' to go to the next question): ").strip()
                                    if user_answer.lower() == answer.lower():
                                        print("Correct!")
                                        break
                                    elif user_answer.lower() == 'next':
                                        print("Skipping to the next question.")
                                        break
                                    else:
                                        retry_choice = input("Incorrect answer. Do you want to retry? (yes/no): ")
                                        if retry_choice.lower() != 'yes':
                                            break
                                input("Press Enter to continue...")
                        else:
                            print("No flashcards available for this topic.")
                            input("\nPress Enter to continue...")
                    else:
                        print("Invalid topic name.")
                        input("\nPress Enter to continue...")
                else:
                    print("No topics available.")
                    input("\nPress Enter to continue...")
            elif choice == "4":
                print("Going back to the main menu...")
                break
            else:
                print("Invalid choice. Please try again.")
                input("\nPress Enter to continue...")
        except ValueError:
            print("Invalid Input")
            print("Enter to continue")
            input()

def menu():
    while True:
        try:
            clear_screen()
            print(f"Welcome to Main Menu\n")
            print("Please choose an option")
            print("1. Register")
            print("2. Login")
            print("3. Exit\n")
            choice = input("Please input choice: ")
            
            if choice == "1":
                register()
            elif choice == "2":
                userlog()
            elif choice == "3":
                print("Exiting the program...")
                break 
            else:
                print("Invalid input. Please choose a valid option.")
                input("Press Enter to continue...")
        except ValueError:
            print("Invalid Input")
            print("Press Enter to continue")
            input()

def user_menu(username):
    tasks = [] 

    while True:
        try:
            clear_screen()
            print(f"Welcome {username}! Please Select.")
            print("1. Calculator")
            print("2. Task Manager")
            print("3. Notepad")
            print("4. Flash Cards")
            print("5. Logout")
            print("6. Exit")

            choice = input("Please enter choice: ")
            if choice == "1":
                calc(username)
            elif choice == "2":
                taskM(username, tasks)  # Pass tasks list to taskM
            elif choice == "3":
                notepad(username)
            elif choice == "4":
                flashcards(username)
            elif choice == "5":
                print("Logging out...")
                input("Press Enter to continue...")
                menu()
            elif choice == "6":
                confirm = input("Are you sure you want to exit? YES OR NO: ")
                if confirm.upper() == "YES":
                    print("Exiting Menu....")
                    break
                elif confirm.upper() == "NO":
                    continue
            else:
                print("Please select an option.")
                input()
        except ValueError:
            print("Invalid Input")
            input()

menu()
