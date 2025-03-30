import random  # Importing the random module to shuffle the questions

# List of "Would You Rather" questions with sophisticated choices and corresponding outcomes
questions = [
    # Each tuple contains: (question, list of choices, resulting category)
    ("Would you rather have the power to read minds or control the weather?", ["Read minds", "Control the weather"], "Psychic"),
    ("Would you rather explore outer space or the deepest parts of the ocean?", ["Outer space", "Deep ocean"], "Explorer"),
    ("Would you rather be able to time travel or teleport?", ["Time travel", "Teleport"], "Time Traveler"),
    ("Would you rather have unlimited wealth or unlimited knowledge?", ["Unlimited wealth", "Unlimited knowledge"], "Philanthropist"),
    ("Would you rather live a peaceful life in the mountains or a busy life in the city?", ["Mountains", "City"], "Adventurer"),
    ("Would you rather be a renowned scientist or a famous artist?", ["Scientist", "Artist"], "Innovator"),
    ("Would you rather have the ability to talk to animals or communicate with extraterrestrial life?", ["Talk to animals", "Talk to aliens"], "Communicator"),
    ("Would you rather never need sleep or never need food?", ["Never need sleep", "Never need food"], "Energizer"),
    ("Would you rather explore unknown lands or solve the mysteries of the universe?", ["Unknown lands", "Mysteries of the universe"], "Philosopher"),
    ("Would you rather have the ability to heal others or the ability to create anything you imagine?", ["Heal others", "Create anything"], "Creator")
]

def play_game():  # Defining the function to start the game
    # Dictionary to store the scores for each result category
    scores = {
        "Psychic": 0, "Explorer": 0, "Time Traveler": 0, "Philanthropist": 0, "Adventurer": 0,
        "Innovator": 0, "Communicator": 0, "Energizer": 0, "Philosopher": 0, "Creator": 0
    }
    
    # Loop through 5 randomly selected questions from the list of questions
    for question, choices, result in random.sample(questions, 5):  # Randomize the order of questions
        print(f"\n{question}")  # Display the question
        print(f"1: {choices[0]}")  # Display the first choice
        print(f"2: {choices[1]}")  # Display the second choice
        
        choice = input("Choose 1 or 2: ")  # Ask the player to choose 1 or 2
        
        # If the input is valid (either "1" or "2"), increase the score for the resulting category
        if choice == "1" or choice == "2":
            scores[result] += 1
    
    # After all questions, determine which result (category) the player most aligns with
    result = max(scores, key=scores.get)  # Find the category with the highest score
    
    # Display the final result
    print(f"\nYou are a {result}!")

# Call the function to start the game
play_game()
