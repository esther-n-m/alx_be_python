# Objective: Create a simplified Python script that uses conditional statements,
# Match Case, and loops (implicitly, as the script runs once per interaction)
# to remind the user about a single, priority task for the day based on time sensitivity.

# Instructions:
# 1. Prompt for a Single Task:
#    - task description (variable: task)
#    - priority level (variable: priority)
#    - time-bound (variable: time_bound)
# 2. Process the Task Based on Priority and Time Sensitivity:
#    - Use Match Case for priority.
#    - Use an if statement for time-bound.
# 3. Provide a Customized Reminder.

# --- Prompt for User Input ---

# Ask the user for the task description.
task = input("Enter your task: ")

# Ask for the task's priority level. Convert to lowercase for case-insensitive comparison.
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound. Convert to lowercase for case-insensitive comparison.
time_bound = input("Is it time-bound? (yes/no): ").lower()

# --- Process the Task and Construct Reminder ---

# Initialize a base reminder message.
base_reminder = ""
immediate_attention_message = " that requires immediate attention today!"
note_message = "" # For low priority, non-time-bound tasks

# Use a Match Case statement to determine the base reminder based on priority.
# This assumes Python 3.10+ for match-case syntax.
match priority:
    case 'high':
        base_reminder = f"'{task}' is a high priority task"
    case 'medium':
        base_reminder = f"'{task}' is a medium priority task"
    case 'low':
        base_reminder = f"'{task}' is a low priority task"
        # For low priority, we have a specific note if not time-bound
        note_message = " Consider completing it when you have free time."
    case _:
        # Handle invalid priority input
        base_reminder = f"'{task}' has an unrecognized priority level"
        immediate_attention_message = "" # No immediate attention message for invalid priority
        note_message = "" # No special note for invalid priority

# --- Modify Reminder based on Time Sensitivity ---

# Now, use an if statement to modify the reminder if the task is time-bound.
# This logic applies after the base reminder is set by the match-case.
if time_bound == 'yes' and priority in ['high', 'medium']:
    # If it's time-bound and high/medium priority, add the immediate attention message.
    # Note: For low priority, the example output suggests a different message,
    # so we'll handle that separately or ensure this doesn't apply to 'low'.
    final_reminder = base_reminder + immediate_attention_message
elif time_bound == 'no' and priority == 'low':
    # Specific case for low priority, non-time-bound tasks as per example.
    final_reminder = "Note: " + base_reminder + note_message
elif time_bound == 'yes' and priority == 'low':
    # If low priority and time-bound, it's still low priority but with attention.
    # The example doesn't explicitly cover this, so we'll make a reasonable assumption.
    final_reminder = base_reminder + " that might become more urgent soon."
elif base_reminder: # If a valid priority was entered but not time-bound 'yes'
    final_reminder = base_reminder + "." # Just end the sentence.
else: # This covers cases where priority was invalid
    final_reminder = base_reminder + "."


# --- Output the Customized Reminder ---

print("\nReminder:", final_reminder)

