import random

# Tool 1: To-Do List Manager
# Manages a dynamic list of tasks with options to add, view, and remove items.
def todo_manager():
    tasks = []
    print("\n--- To-Do List Manager ---")
    while True:
        print("\n1. View Tasks\n2. Add Task\n3. Remove Task\n4. Back to Main Menu")
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == "1":
            if not tasks:
                print("\nYour to-do list is currently empty.")
            else:
                print("\nYour Current Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == "2":
            new_task = input("Enter the task description: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"'{new_task}' added successfully.")
            else:
                print("Task cannot be empty.")
        elif choice == "3":
            if not tasks:
                print("\nNo tasks to remove.")
            else:
                print("\nCurrent Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    remove_idx = int(input("Enter the number of the task to remove: ")) - 1
                    if 0 <= remove_idx < len(tasks):
                        removed = tasks.pop(remove_idx)
                        print(f"'{removed}' has been removed.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")
        elif choice == "4":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")

# Tool 2: Number Guessing Game
# Challenges the user to guess a randomly generated number between 1 and 20.
def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    print("I have picked a number between 1 and 20. Try to guess it!")
    secret_number = random.randint(1, 20)
    attempts = 0
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid integer.")

# Tool 3: Tip Calculator
# Calculates tip amounts and splits the total bill cleanly.
def tip_calculator():
    print("\n--- Tip Calculator ---")
    try:
        bill = float(input("Enter the total bill amount ($): "))
        tip_percentage = float(input("Enter the tip percentage (e.g., 15, 18, 20): "))
        people = int(input("Enter the number of people splitting the bill: "))
        
        if bill < 0 or tip_percentage < 0 or people <= 0:
            print("Values must be greater than zero.")
            return
            
        tip_amount = bill * (tip_percentage / 100)
        total_bill = bill + tip_amount
        per_person = total_bill / people
        
        print(f"\n--- Bill Summary ---")
        print(f"Tip Amount: ${tip_amount:.2f}")
        print(f"Total Bill: ${total_bill:.2f}")
        print(f"Amount Per Person: ${per_person:.2f}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Main Program Loop
def main():
    print("Welcome to your Personal Mini-Toolkit!")
    
    while True:
        print("\n==============================")
        print("      PERSONAL MINI-TOOLKIT")
        print("==============================")
        print("1. To-Do List Manager")
        print("2. Number Guessing Game")
        print("3. Tip Calculator")
        print("4. Quit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            todo_manager()
        elif choice == "2":
            number_guessing_game()
        elif choice == "3":
            tip_calculator()
        elif choice == "4":
            print("\nThank you for using Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print("\n[Error] Invalid choice. Please select an option between 1 and 4.")

if __name__ == "__main__":
    main()
    