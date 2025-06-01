# Objective: Create a simplified Python script that uses conditional statements,
def main():
    """
    This script prompts the user for a single task, its priority level,
    and if it is time-sensitive. It then provides a customized reminder
    for that task based on the inputs.
    """
    print("Welcome to your Daily Task Reminder!")

    # Prompt for a single task description
    task = input("Enter your task: ")

    # Prompt for the task's priority level
    # Convert input to lowercase for consistent matching
    priority = input("Priority (high/medium/low): ").lower()

    # Prompt if the task is time-bound
    # Convert input to lowercase for consistent matching
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Initialize the reminder message variable
    reminder_message = ""

    # Process the task based on priority using a Match Case statement
    match priority:
        case 'high':
            # Base message for high priority tasks
            reminder_message = f"Reminder: '{task}' is a high priority task"
            # Use an if statement to modify the reminder if the task is time-bound
            if time_bound == 'yes':
                reminder_message += " that requires immediate attention today!"
            else:
                reminder_message += "." # Add a period if not time-bound
        case 'medium':
            # Base message for medium priority tasks
            reminder_message = f"Reminder: '{task}' is a medium priority task"
            # Use an if statement to modify the reminder if the task is time-bound
            if time_bound == 'yes':
                reminder_message += " that requires immediate attention today!"
            else:
                reminder_message += "." # Add a period if not time-bound
        case 'low':
            # For low priority tasks, the message changes significantly based on time-bound status
            if time_bound == 'yes':
                reminder_message = f"Reminder: '{task}' is a low priority task that requires immediate attention today!"
            else:
                # Specific message for non-time-bound low priority tasks as per example
                reminder_message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            # Handle cases where an invalid priority is entered
            reminder_message = "Error: Invalid priority entered. Please choose 'high', 'medium', or 'low'."

    # Print the customized reminder
    print(reminder_message)

if __name__ == "__main__":
    main()

