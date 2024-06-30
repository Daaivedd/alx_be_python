task = input("Enter your task:")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority :
    case "high" : 
        if time_bound == "yes" :
            print(f"Reminder: {'task'} is a high priority task that requires immediate attention today!")
        else:
            msg =  "is a high priority task."
            print(f"Reminder: {'task'} {msg}")
    case "medium" :
        msg = "is a low priority task. don't forget it."
        print(f"Note: {'task'} {msg}")
    case "low" :
        msg = "is a low priority task. Consider completing it when you have free time."
        print(f"Note: {'task'} {msg}")
