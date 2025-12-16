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
        Choice = input(colored("Options: [1] Edit Info [2] Delete User [3] Show Login History [4] Log-out: ", "white")).strip()  # Provide options to the user
        if Choice == "1":                                                                                                        # If edit is chosen
            logged_in_user[1] = input(colored(f"Objective [{logged_in_user[1]}]: ", "yellow")) or logged_in_user[1]              # Edit objective
            logged_in_user[2] = input(colored(f"Job Info [{logged_in_user[2]}]: ", "yellow")) or logged_in_user[2]               # Job info
            logged_in_user[4] = input(colored(f"Password [{logged_in_user[4]}]: ", "yellow")) or logged_in_user[4]               # Change password
            print(colored("Information record confirmed and updated successfully.", "light_red"))                                # Log update confirmation
        elif Choice == "2":                                                                                                      # Option to delete user
            confirm = input(colored(f"Verify deletion of user {logged_in_user[0]} (yes/no): ", "white")).lower()                 # Confirm deletion
            if confirm == "yes":                                                                                                 # If yes --> deleted
                data.remove(logged_in_user)                                                                                      # Data removal
                print(colored(f"{logged_in_user[0]} deleted successfully.\n", "red"))                                            # Deletion confirmation
        elif Choice == "3":                                                                                                      # Show recent login history
            print(colored("\n--- Recent Logins ---", "light_red"))
            for entry in login_history[-5:]:                                                                                     # Show last 5 logins
                print(colored(f"{entry[0]} logged in at {entry[1]}", "yellow"))
        elif Choice == "4":                                                                                                      # If log out is chosen
            print(colored("Logging out...\n","red"))                                                                             # Notify user of log out
        else:
            print(colored("Option invalid.  -== DENIED ==-", "yellow"))                                                          # Invalid login attempt
    else:
        print(colored("Access Denied! Invalid credentials. Please try again.","yellow"))                                         # Indicate failed login
    User_Credentials_Log = input(colored("\nWould you like to manage another log (yes/no): ", "white")).lower()                  # Yes or no to continue
    if User_Credentials_Log != 'yes':                                                                                            # If no, exit loop
        print(colored("Thank you!", "light_red"))                                                                                # Exit message
        break                                                                                                                    # Exit the program