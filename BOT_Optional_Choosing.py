from termcolor import colored 

Battery = "Low Charge "
LED = "Dim/Low LED"
Battery_Range = ["A:10-35%, B:36-65%, C:66-95%"]
A = colored("Charge For Just About 35 Minutes! ","light_yellow")
B = colored("Charge For Approximately 25 Minutes! ","light_magenta")
C = colored("Charge No More Than 15 Minutes! ","light_cyan","on_light_cyan")
Color = ["Red", "Orange", "Yellow", "Green", "Blue"]
R = "Restart"
E = "Exit"
# Variables

while True:
    print(colored(Battery + LED, "light_cyan"))  # Display battery and LED status in cyan color
    name = input(colored(f"May I Know Who This Is? ", "green"))  # Ask for user name in green
    print(colored(f"Hello {name}, Would You Like To Recharge LED Battery? ", "red"))  # Greet user in red
    user_input = input("Please Answer By Typing: 'Yes' OR 'No' ")  # Get user response
    if user_input == "Yes":
        print(f"What Is The Current Battery Percentage Range In? A: 10-35% ", "B: 36-65% ", "C: 66-90% ")  # Ask for battery range
        user_input = input("Choice (Type As Options Given 'A'...): ")  # Get choice for battery range
        if user_input == "A":
            print(A)  # Print charge recommendation for range A
        elif user_input == "B":
            print(B)  # Print charge recommendation for range B
        elif user_input == "C":
            print(C)  # Print charge recommendation for range C
            print(colored(f"Have A Nice Day {name}!", "light_yellow"))  # Greet in yellow
        else:
            print(colored(f"Invalid Input!", "light_red"))  # Handle invalid input in red
            print(f"Try Typing Exactly As Displayed {name}!")  # Prompt user to try again
    elif user_input == "No":
        user_input = input(colored(f"Would You Like To Change Color Instead? Please Answer By Typing: 'Yes' OR 'No' ", "light_magenta"))  # Ask about color change
        if user_input == "Yes":
            print(f"Choose Which Color Below: ")  # Prompt for color selection
            for color in Color:
                print(color)  # Display color options
            user_input = input("Choice: ")  # Get color choice
            if user_input in Color:
                print(colored(f"LED Switched Into {user_input}!", "grey"))  # Change LED color
                print(colored(f"Have A Nice Day {name}!", "light_green"))  # Greet in light green
            else:  
                print("Invalid Input!")  # Handle invalid color input
                print(colored(f"Try typing Exactly As Displayed {name}!", "light_yellow"))  # Prompt for correct input
        else:
            user_input = input(colored(f"Would You Like To Alternately Change Brightness For LED? Please Answer By Typing: 'Yes' OR 'No' ", "light_red"))  # Ask about brightness change
            if user_input == "Yes":
                print(colored(f"Pick Between '10 ~ 100' ", "light_blue"))  # Prompt for brightness level
                user_input = int(input(" "))  # Get brightness input
                if 10 <= user_input <= 100:
                    print(colored(f"Brightness Adjusted to {user_input}%: ", "light_magenta"))  # Confirm brightness change
                    print(colored(f"Have A Nice Day {name}!", "light_blue"))  # Greet in blue
                else:
                    print(colored(f"Invalid Brightness Input! Choose Between 10 Which Is Lowest Dim or 100 Which is Max Brightness!", "light_red"))  # Handle invalid brightness input
                    print(f"Try Typing Exactly As Displayed {name}!")  # Prompt user to try again
            elif user_input == "No":
                print(colored(f"If You'd Like To Exit, Type 'E', Otherwise Type 'R' To Restart.", "yellow"))  # Ask for exit or restart
                user_input = input("")  # Get exit or restart input
                if user_input.upper() == "E":
                    print(colored(f"Take Care {name}!","light_cyan"))  # Exit greeting
                    break  # Exit the program
                elif user_input.upper() == "R":
                    continue  # Restart the loop
                else:
                    print(colored(f"Invalid Input!, Restarting...", "red"))  # Handle invalid input
                    print(colored(f"Try Typing Exactly As Displayed {name}!", "yellow"))  # Prompt user to try again
