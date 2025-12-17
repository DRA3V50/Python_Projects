from termcolor import colored
from tabulate import tabulate
from datetime import datetime                                                                                                    # For login timestamps

#--- Character Access Data Log ---
headers = ["Name", "Objective", "Job Info", "Username", "Password", "Last Login"]

data = [
    ["Leon S. Kennedy", "Uncover the truth behind the outbreak.", "Rookie police officer", "leon.kennedy", "RPDLeon1998", ""],
    ["Claire Redfield", "Find her brother Chris and protect Sherry.", "Civilian survivor", "ClaireR", "CCR789", ""],
    ["Ada Wong", "Retrieve the G-Virus sample.", "Covert mercenary posing as FBI agent", "AdaW", "MercenaryAda456", ""],
    ["Sherry Birkin", "Escape Umbrella and survive.", "Civilian child infected with G-Virus", "SherryB", "TeddyBear305", ""],
    ["Annette Birkin", "Stop Umbrella and save Sherry.", "Umbrella researcher", "AnnetteB", "Scientist242", ""],
    ["William Birkin", "Spread the G-Virus after mutation.", "Umbrella scientist (mutated)", "WilliamB", "Mutant303", ""],
    ["Marvin Branagh", "Help survivors and hold the RPD.", "RPD lieutenant", "MarvinB", "HelpSurvive650", ""],
    ["Brian Irons", "Cover up Umbrella crimes.", "Corrupt RPD chief", "BrianI", "CoverUmbrella505", ""],
]

failed_attempts = 0                                                                                                              # Track failed access attempts
login_history = []                                                                                                               # Keep track of recent logins

while True:
    print(colored("\n--- Character Access Data Log ---\n", "white"))
    print(tabulate(data, headers=headers, tablefmt="grid"))
    Username = input(colored("Enter Username: ", "light_red"))                                                                   # Type one of the usernames from the data log
    Password = input(colored("Enter Password: ", "light_red"))                                                                   # Type the original password that corresponds to the username
    logged_in = False                                                                                                            # Variable to track login status/check
    logged_in_user = None                                                                                                        # User found
    for row in data:                                                                                                             # Loop through each character/log
        if row[3].lower() == Username.lower() and row[4] == Password:                                                            # Compare input with username and password from the data log
            logged_in = True                                                                                                     # Keep track of successful login
            logged_in_user = row                                                                                                 # User found
            row[5] = datetime.now().strftime("%Y-%m-%d %H:%M")                                                                   # Update last login timestamp
            login_history.append((row[0], row[5]))                                                                               # Add to recent login history
            break                                                                                                                # If match found, break the loop
    if logged_in:                                                                                                                # If login is successful
        print(colored(f"Access Granted! Welcome, {logged_in_user[0]}!", "red"))                                                  # Indicate successful login
        print(colored(f"[AUDIT] {Username} performed Logged in at {datetime.now()}", "light_blue"))                              # Audit log entry
        action = "Logged in"                                                                                                     # Log action
        with open("audit_log.txt", "a") as f:                                                                                    # Audit log file
            f.write(f"{datetime.now()} - {logged_in_user[0]} performed {action}\n")                                              # Keep track of user actions
        print(colored(f"Inactive users: {[row[0] for row in data if not row[5]]}", "grey"))                                      # Show inactive users
        critical_count = sum (1 for row in data if "G-Virus" in row[1])                                                          # Count critical cases
        print(colored(f"Critical Cases (G-Virus linked): {critical_count}", "yellow"))                                           # Show count of critical cases
        Choice = input(colored("Options: [1] Edit Info [2] Delete User [3] Show Login History [4] Log-out: ", "white")).strip()  # Provide options to the user
        if Choice == "1":                                                                                                        # If edit is chosen
            logged_in_user[1] = input(colored(f"Objective [{logged_in_user[1]}]: ", "yellow")) or logged_in_user[1]              # Edit objective
            logged_in_user[2] = input(colored(f"Job Info [{logged_in_user[2]}]: ", "yellow")) or logged_in_user[2]               # Job info
            logged_in_user[4] = input(colored(f"Password [{logged_in_user[4]}]: ", "yellow")) or logged_in_user[4]               # Change password
            print(colored("Information record confirmed and updated successfully.", "light_red"))                                # Log update confirmation
            action = "Edited User Info"                                                                                          # If action is edited
            print(colored(f"[AUDIT] {logged_in_user[0]} performed {action} at {datetime.now()}", "light_blue"))                   # Audit log entry
            with open("audit_log.txt", "a") as f:                                                                                # Audit log file
                f.write(f"{datetime.now()} - {logged_in_user[0]} performed {action}\n")                                          # Keep track of user actions
        elif Choice == "2":                                                                                                      # Option to delete user
            confirm = input(colored(f"Verify deletion of user {logged_in_user[0]} (yes/no): ", "white")).lower()                 # Confirm deletion
            if confirm == "yes":                                                                                                 # If yes --> deleted
                data.remove(logged_in_user)                                                                                      # Data removal
                print(colored(f"{logged_in_user[0]} deleted successfully.\n", "red"))                                            # Deletion confirmation
                action = "Deleted User"                                                                                          # Action logged
                print(colored(f"[AUDIT] {logged_in_user[0]} performed {action} at {datetime.now()}", "light_blue"))              # Audit log entry
                with open("audit_log.txt", "a") as f:                                                                            # Audit log file
                    f.write(f"{datetime.now()} - {logged_in_user[0]} performed {action}\n")                                      # Keep track of user actions
            if not data:                                                                                                         # Check if data list is empty
                print(colored("Data list is empty. No users left.", "yellow"))                                                   # Notify no users left
                break                                                                                                            # Exit if no users left
            else:
                print(colored(f"Remaining users in record: {len(data)}", "light_red"))                                           # Show remaining users
        elif Choice == "3":                                                                                                      # Show recent login history
            print(colored("\n--- Recent Logins --- ", "light_red"))                                                              # Header for recent logins
            for entry in login_history[-5:]:                                                                                     # Show last 5 logins
                print(colored(f"{entry[0]} logged in at {entry[1]}", "yellow"))                                                  # Print recent login entries
        elif Choice == "4":                                                                                                      # If log out is chosen
            print(colored("Logging out...\n","red"))                                                                             # Notify user of log out
        else:
            print(colored("Option invalid.  -== DENIED ==- ", "yellow"))                                                         # Invalid login attempt
    else:
        print(colored("Access Denied! Invalid credentials. Please try again.","yellow"))                                         # Indicate failed login
        failed_attempts += 1                                                                                                     # Increment failed attempts
        action = "Failed login attempts"                                                                                         # Action logged
        print(colored(f"[AUDIT] {Username} performed {action} at {datetime.now()}", "light_blue"))                               # Audit log entry
        with open("audit_log.txt", "a") as f:                                                                                    # Audit log file
            f.write(f"{datetime.now()} - {Username} performed {action}\n")                                                       # Keep track of user actions
        if failed_attempts >= 3:                                                                                                 # After 3 failed attempts
            print(colored("ALERT: Multiple failed login attempts detected. Session terminated.","red"))                          # Notify user of exit
            print(colored("Control Triggered: Excessive failed authentication attempts (GRC enforcement).", "yellow"))           # GRC enforcement message
            break                                                                                                                # Exit the program
    User_Credentials_Log = input(colored("\nWould you like to manage another log (yes/no): ", "white")).lower()                  # Yes or no to continue
    if User_Credentials_Log != 'yes':                                                                                            # If no, exit loop
        print(colored("Thank you!", "light_red"))                                                                                # Exit message
        break
