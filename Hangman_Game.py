import random

words = ["python", "hangman", "computer", "pyramid", "artist", "universe", "ocean", "galactic", "graduate", "astonished",
          "role", "superior", "belief", "dramatic", "source", "excruciating", "crust", "bowl", "chicken", "technological", 
          "obliteration", "box", "supply", "chronological", "termination", "defense", "tickle", "gamer", "circus", "panda", "supportive",
          "battery", "challenging", "exterior", "headset", "planets", "unidentified", "classification", "decryption", "cryptography", "seals",
          "age", "geography", "jeopardy", "unnecessary", "hook", "vivid", "philosophy", "destructive", "spectacular", "kilometers", "spartans"]

def play_hangman():
    word = random.choice(words)  # Select a random word
    guessed_word = "_" * len(word)  # Start with blanks
    guessed_letters = []  # Track guessed letters
    attempts = 5  # Number of allowed incorrect guesses
    
    while attempts > 0:
        print(f"Word: {guessed_word}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("Already guessed!")
            continue

        guessed_letters.append(guess)
        
        if guess in word:
            guessed_word = "".join([guess if word[i] == guess else guessed_word[i] for i in range(len(word))])
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong! {attempts} attempts left.")

        if guessed_word == word:
            print("You won!")
            break
    else:
        print(f"You lost! The word was: {word}")

    if input("Play again? (yes/no): ").lower() == "yes":
        play_hangman()
    else:
            print(f"Come Again Soon, Take Care! ")

play_hangman()
