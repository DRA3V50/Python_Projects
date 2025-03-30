from tkinter import *  # Import everything from tkinter to build the GUI
import random  # Import random module to generate a random number
from PIL import Image, ImageTk  # Import image handling from Pillow

# Set up the main window (root window) for the game
root = Tk()  # Create the main window object
root.title('Number Guess Game!')  # Set the window title
root.geometry('750x750')  # Set the size of the window (500x500 pixels)

# Generate a random number between 1 and 50
BOTnumber = random.randint(1, 50)  # The computer picks a random number

# Display instructions at the top of the window
Label(root, text="Guess a number between 1 and 50!", font=("Arial", 14)).pack(pady=10)  # Label for instructions

# Label to display feedback based on the user's guess
feedback_label = Label(root, text="", font=("Arial", 12))  # Label for feedback (initially empty)
feedback_label.pack(pady=10)  # Add the label to the window

# Create an Entry widget for the user to type in their guess
guess_entry = Entry(root, font=("Arial", 12))  # Entry widget for user input
guess_entry.pack(pady=5)  # Add the input field to the window

# Label for displaying the cookie image (initially empty)
cookie_label = Label(root)  # This label will hold the cookie image
cookie_label.pack(pady=20)  # Add the label to the window

# Declare the cookie_image variable outside the function to keep a reference
cookie_photo = None

# Function that will be called when the "Guess" button is clicked
def check_guess():
    global cookie_photo  # Use global to ensure the cookie_photo variable retains the image reference
    user_guess = int(guess_entry.get())  # Get the user's guess and convert it to an integer
    
    # Check if the guess is correct
    if user_guess == BOTnumber:  # If the guess is equal to the random number
        feedback_label.config(text="Correct! You win a cookie!")  # Update feedback to say "Correct!"
        try:
            # Correct path to the image (make sure to use the full path)
            cookie_image = Image.open("C:/Users/arabo/OneDrive/Desktop/Python_Practice/Cookie.png")  # Correct path to the image Ex: "C:/Users/YOUR_NAME/YOUR_FOLDER/Cookie.png"
            cookie_image = cookie_image.resize((300, 300))  # Resize the image to fit the window
            cookie_photo = ImageTk.PhotoImage(cookie_image)  # Convert the image to a format Tkinter can display
            cookie_label.config(image=cookie_photo)  # Set the cookie image to the label
            cookie_label.image = cookie_photo  # Keep a reference to the image to prevent it from disappearing
        except Exception as e:
            feedback_label.config(text=f"Error loading image: {e}")  # In case of any error loading the image
    # Check if the guess is too low
    elif user_guess < BOTnumber:  # If the guess is smaller than the random number
        feedback_label.config(text="Too low! Try again.")  # Update feedback to say "Too low!"

    # Check if the guess is too high
    else:  # If the guess is larger than the random number
        feedback_label.config(text="Too high! Try again.")  # Update feedback to say "Too high!"

# Button that calls the check_guess function when clicked
Button(root, text="Guess", command=check_guess, font=("Roman", 12)).pack(pady=20)  # Create and add the button

# Run the Tkinter main loop to display the window and wait for user input
root.mainloop()  # This keeps the window open and running
