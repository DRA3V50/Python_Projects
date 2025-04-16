import itertools  #Create all combinations of characters/numbers
password = "pas$"  # The password to crack!
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:',.<>?/`~"  #Full character set - lowercase, uppercase, numbers, special characters
for length in range(1, len(password) + 1):  #Try all lengths from 1 up to the password's length
    for attempt in itertools.product(chars, repeat=length):  #Generate all possible combinations of this length
        guess = ''.join(attempt)  #Turns tuple of characters into a single string guess
        print("Trying:", guess)  #Print-guess to show progress 
        if guess == password:  #Check if the guess 'matches' the real password
            print("Password found:", guess)  #If it matches, print the *correct* password
            exit()  #Exit the program once the password is found
