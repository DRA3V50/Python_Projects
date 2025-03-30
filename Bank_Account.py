import time

# Variables
Account_Option = ["Pay, Withdraw, Deposite"]
Bank_Balance_Option = ("Balance: ")
Login_Credentials = ["ID", "Password", "Pin"]
Fraud = ["Account Lockdown"]

user_info = {
    "name": "",        #User name input.
    "password": "",    #User passwork create/use
    "pin": "",         #User 4-Digit personal identification number create/use   
    "balance": 50.00   #Start with a balance of 50.00
}

# Function to handle login and track failed attempts
def login(failed_attempts, lockdown_time):     #You can move the function definitions around, as long as the functions are defined before they are called. 
    if lockdown_time > time.time():
        print(f"Your account is locked. Please try again after {int(lockdown_time - time.time())} seconds.")
        return failed_attempts, lockdown_time
    print("\n--- Please log in ---")

    # Ask for login credentials
    login_name = input("Enter your name: ")
    login_password = input("Enter your password: ")
    login_pin = input("Enter your PIN: ")

    # Validate credentials
    if login_name != user_info.get("name"):
        print("Invalid name.")
        failed_attempts += 1
    elif login_password != user_info.get("password"):
        print("Invalid password.")
        failed_attempts += 1
    elif login_pin != user_info.get("pin"):
        print("Invalid PIN.")
        failed_attempts += 1
    else:
        print("Login successful! Welcome to your bank account.")
        return failed_attempts, lockdown_time  # Return when login is successful

    # Lock the account if 5 failed attempts
    if failed_attempts >= 5:
        print("Too many failed attempts. Locking account for 10 minutes.")
        lockdown_time = time.time() + 600  # Lock for 10 minutes
        failed_attempts = 0  # Reset failed attempts after lockdown
        return failed_attempts, lockdown_time  # Return the updated values

    return failed_attempts, lockdown_time

# Function to create an account
def create_account():
    print("Welcome To The ATM Machine! Let's Create Your Account!\n")
    
    # Asking for user input during account creation
    first_name = input("What is your first name? ")
    first_initial_with_birthyear = input("Enter First Initial with Birth Year (e.g. J1995): ")
    
    # Validate the initial matches the first letter of the name
    if first_initial_with_birthyear[0].upper() != first_name[0].upper():
        print("Initial doesn't match the first letter of your name! Please try again.")
        return 0, 0  # Return default values if validation fails
    birth_year = first_initial_with_birthyear[1:]  # Extract birth year from input
    
    # Ask for password (birth year + '*')
    password = input("Enter Password, must be birth year followed by '*': ")
    if password != birth_year + "*":
        print("Password doesn't match the required format! Must be 4 digits followed by '*'. Please try again.")
        return 0, 0  # Return default values if validation fails
    
    # Ask for the PIN (reversed birth year)
    pin = input("Enter PIN (reversed birth year): ")
    if pin != birth_year[::-1]:  # Reverses the birth year
        print("PIN doesn't match the reversed birth year! Please try again.")
        return 0, 0  # Return default values if validation fails
    
    #If everything is correct, store the credentials
    user_info["name"] = first_name
    user_info["password"] = password
    user_info["pin"] = pin

    print("Account credentials successfully created!\n")
    return 0, 0  # Return default values after account creation

# Function to display the bank menu
def bank_menu():
    while True:
        print("\n--- Bank Options ---")
        print("1. Pay")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Check Balance")
        print("5. Logout")
        
        choice = input("Please choose an option (1-5): ")

        if choice == '1':
            make_payment()  # Payment function
        elif choice == '2':
            withdraw_money()  # Withdraw function
        elif choice == '3':
            deposit_money()  # Deposit function
        elif choice == '4':
            check_balance()  # Balance check
        elif choice == '5':
            print("Logging out...")
            break  # Exit the loop and logout
        else:
            print("Invalid choice. Please try again.")

# Simplified Payment function
def make_payment():
    amount = input("Enter the amount to pay: $")
    if amount.replace('.', '', 1).isdigit():  # Check if input is a valid number
        amount = float(amount)
        if amount > 0 and amount <= user_info["balance"]:
            user_info["balance"] -= amount
            print(f"Successfully paid ${amount:.2f}. Your new balance is ${user_info['balance']:.2f}")
        else:
            print("Invalid amount. Either the amount is too large or you have insufficient funds.")
    else:
        print("Invalid input! Please enter a valid number.")

# Simplified Withdraw function
def withdraw_money():
    amount = input("Enter the amount to withdraw: $")
    if amount.replace('.', '', 1).isdigit():  # Check if input is a valid number
        amount = float(amount)
        if amount > 0 and amount <= user_info["balance"]:
            user_info["balance"] -= amount
            print(f"Successfully withdrew ${amount:.2f}. Your new balance is ${user_info['balance']:.2f}")
        else:
            print("Invalid amount. Either the amount is too large or you have insufficient funds.")
    else:
        print("Invalid input! Please enter a valid number.")

# Simplified Deposit function
def deposit_money():
    amount = input("Enter the amount to deposit: $")
    if amount.replace('.', '', 1).isdigit():  # Check if input is a valid number
        amount = float(amount)
        if amount > 0:
            user_info["balance"] += amount
            print(f"Successfully deposited ${amount:.2f}. Your new balance is ${user_info['balance']:.2f}")
        else:
            print("Invalid amount. Please enter a positive number.")
    else:
        print("Invalid input! Please enter a valid number.")

# Function to check the balance
def check_balance():
    print(f"{Bank_Balance_Option} ${user_info['balance']:.2f}")

# Main program
def main():
    create_account()  # Create account and get initial failed attempts and lockdown time
    failed_attempts = 0  # Initialize failed attempts
    lockdown_time = 0  # Initialize lockdown time

    # After account creation, loop the login and bank menu until successful login
    while True:
        failed_attempts, lockdown_time = login(failed_attempts, lockdown_time)  # Call login with tracking of failed attempts
        if lockdown_time <= time.time():
            break  # Proceed to bank menu once login is successful

    bank_menu()  # Once logged in, display the bank menu

# Run the program
if __name__ == "__main__": #When you run a Python script directly, Python sets the __name__ variable to "__main__".
    main()        #If the script is being run directly, then __name__ will be "__main__", and the block of code inside the if statement will execute.
