# Objective: Create a simplified Python script that uses conditional statements,
def daily_reminder():
    # Step 1: Prompt the user for task details
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Step 2: Process the task based on priority and time sensitivity
    match priority:
        case "high":
            priority_message = "high priority task"
        case "medium":
            priority_message = "medium priority task"
        case "low":
            priority_message = "low priority task"
        case _:
            priority_message = "undefined priority task"

    # Step 3: Check if the task is time-bound and adjust the reminder
    if time_bound == "yes":
        time_sensitive_message = "requires immediate attention today!"
    else:
        time_sensitive_message = "Consider completing it when you have free time."

    # Step 4: Generate the reminder
    print(f"Reminder: '{task}' is a {priority_message} that {time_sensitive_message}")

# Run the function to remind the user
daily_reminder()