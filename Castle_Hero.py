import random
from termcolor import colored  # Import termcolor for colored text
# Begin Game
# Data for names by letter
names = {
    'A': ["Alan", "Anoe", "Anderson", "Abol", "Elon", "Arin"],
    'B': ["Biggy", "Bolak", "Brian", "Brosy", "Boen"],
    'C': ["Carl", "Coky", "Camron", "Chadd", "Crak"],
    'D': ["Divon", "Dooke", "Deruk", "Dariy", "Donaky"],
    'E': ["Evak", "Eld", "Eden", "Elom", "Etohy"],
    'F': ["Fiko", "Frank", "Fanod", "Fred", "Felix"],
    'G': ["George", "Gino", "Gapo", "Gerry", "Gail"],
    'H': ["Hepto", "Harry", "Hank", "Hilon", "Hroth"],
    'I': ["Ithoc", "Ion", "Isaac", "Irone", "Igoo"],
    'J': ["John", "Jono", "Jackary", "Jololo", "Jason"],
    'K': ["Korth", "Kevin", "Kyle", "Koal", "Kiloth"],
    'L': ["Lion", "Lote", "Loye", "Luke", "Laith"],
    'M': ["Max", "Maloo", "Mason", "Meo", "Mark"],
    'N': ["Nathan", "Nelo", "Noah", "Neo", "Narco"],
    'O': ["Oath", "Oscar", "Owen", "Opal", "Omar"],
    'P': ["Paul", "Pam", "Peter", "Ponko", "Priscot"],
    'Q': ["Quakal", "Qoko", "Qaleo", "Qontoy", "Qalon"],
    'R': ["Rote", "Ray", "Ramy", "Rick", "Roe"],
    'S': ["Sam", "Sote", "Steve", "Strode", "Sippy"],
    'T': ["Tom", "Teon", "Tramo", "Twake", "Tole"],
    'U': ["Ummo", "Urgo", "Umar", "Usman", "Ukilo"],
    'V': ["Varo", "Victor", "Vince", "Vivon", "Volem"],
    'W': ["Wekol", "Woody", "Walter", "Willow", "Wilon"],
    'X': ["Xander", "Xino", "Xeron", "Xelo", "Xakon"],
    'Y': ["Yoron", "Yussy", "Yoniko", "Yusmo", "Yekon"],
    'Z': ["Zane", "Zoral", "Zoe", "Zeke", "Zack"]
}

# List of colors for text display
colors = [
    "red", "blue", "green", "yellow", "magenta", "cyan", 
    "white", "grey", "light_red", "light_green", 
    "light_magenta", "light_cyan", "light_blue", 
    "light_grey", "light_yellow"
]

# List of job classes
jobs = [
    "Knight", "Wizard", "Merchant", "Thief", "Healer", 
    "Assassin", "Alchemist", "Priest", "Barbarian", "Warrior"
]

# List of princess names
princess_names = [
    "Rosita", "Selena", "Elara", "Ariana", "Zara", 
    "Lira", "Elysia", "Fiora", "Isolde", "Cassandra", 
    "Alisa", "Lina", "Dalya", "Mera", "Taily",
    "Balina", "Rily", "Wenola", "Kurla", "Tiona",
    "Gibbal", "Jaila", "Iohna", "Fikila", "Vabilee"
]

# Inventory for different job classes
specified_inventory = {
    'Knight': ["Sword", "Shield"],
    'Wizard': ["Wand", "Potion"],
    'Merchant': ["Knife", "Bandage"],
    'Thief': ["Dagger", "Lockpick"],
    'Healer': ["Healing Herb", "Life Shield"],
    'Assassin': ["Stealth Cloak", "Poison"],
    'Alchemist': ["Potion", "Sanctional Ruby"],
    'Priest': ["Holy Book", "Blessing Oil"],
    'Barbarian': ["Battle Axe", "Health Fruit"],
    'Warrior': ["Sword", "Helmet"]
}
# Function to create character based on input letter


def create_character():
    princess_name = random.choice(princess_names)  # Randomly select a princess name

    # Welcome messages
    print(colored(f"***EVERY END OF GAME, KILL TERMINAL BEFORE STARTING A NEW ONE FOR BETTER DIALOGUE AND NO CONFUSION.***","light_green"))
    print(colored(f"WARNING:TYPE AS OPTIONS ARE GIVEN OR GAME WILL MESS UP!", "light_red"))
    print(colored("\nWelcome to the Medieval Adventure Game!", "magenta"))
    print(colored("In this game, you'll embark on a quest to save a princess and fight mighty entities!", "red"))
    print(colored("Let's begin by creating your character...\n", "yellow"))
    # Prompt user for a letter to choose a name
    letter = input(colored("Choose a letter (A-Z) to start your character creation: ", "blue")).upper()
    
    # Check if the letter is valid
    if letter in names:
        name = random.choice(names[letter])  # Randomly select a name from the chosen letter
        color = random.choice(colors)  # Random color (for display purposes)
        job = random.choice(jobs)  # Randomly assign a job
        hp = 100  # Character starts with 100 HP, can if you needed to!
        inventory = specified_inventory[job]  # Assign inventory based on job

        # Display the character's initial stats
        display_intro(name, hp, inventory, job)

        # Ask if the player wants to start the journey
        choice_option = input(colored("\nNarrator: Would you like to begin your journey across the medieval era, and save the day? (Start/No): ", "blue")).lower()
        # If player chooses to start
        if choice_option == "start":
            print(colored(f"Narrator: The journey begins, {name}!", "blue"))  # Description
            print(colored(f"Narrator: You awoke early morning, wondering where life will get you into...", "blue"))  # Description
            # Ask if the player wants to leave their dorm
            leave_choice = input(colored(f"Narrator: Would you like to leave your dorm, {name}? (Leave/No): ", "blue")).lower()
            # If player chooses to leave
            if leave_choice == "leave":
                print(colored(f"Narrator: You head outside, but something doesn't feel right. You look up at the castle tower and see a dragon - dark gray and smokey with jaw teeth the length of a human....laying on top of the tower.", "blue"))  # Storyline
                print(colored(f"Narrator: Unable to let princess {princess_name} escape, yelling, or resting.", "blue"))  # Storyline
                print(colored(f"Narrator: You slowly make your way up to the dorm to check if princess {princess_name} is hurt while the dragon is still asleep. \nYou squeak as you try to go into the dorm, however, the dragon awoke and found you.", "blue"))  # Storyline
                print(colored(f"Dragon: 'You must do as I tell you or else everyone will perish miserably....Yes?'", "red"))  # Storyline
                # Ask if the player agrees to the dragon's request
                player_input = input(colored("Do you choose to agree? (Yes/No): ", "yellow")).lower()  # Storyline/Question
                # If player agrees
                if player_input == "yes":
                    print(colored("Dragon: 'Good choice... \nI need you to obtain the PHILOSOPHER'S STONE from the place known as 'Dimware Valley.' You with me so far? \n'Yes'?", "red"))  # Storyline
                    player_input = input(colored("Do you want to continue? (Yes/No): ", "yellow")).lower()  # Player input
                    # If player wants to continue
                    if player_input == "yes":
                        print(colored("Dragon: 'Good! \nYou have thought wisely, but your request shall begin now. \nI will be needing you to start the search. After you've found it, come back and we shall proceed thoroughly from there.'", "red"))  # Storyline
                        player_input = input(colored("Understood.....? (Yes)|(No): ", "yellow")).lower()  # Storyline
                        # If player confirms understanding
                        if player_input == "yes":
                            print(colored("Dragon: 'Your journey begins!'", "red"))
                            path_choice(name, hp, inventory)  # Proceed with the path choice
                        else:
                            print(colored("Dragon: 'You dare deny me?! If you wish to live, you must obey!' He roars angrily and agressively", "red"))
                            # Penalty or consequence here
                    else:
                        print(colored("Dragon: 'You will regret this! Everyone will perish!' The dragon huffs in frustration.", "red"))
                        # Penalty or consequence here if the player chooses 'no'
                elif player_input == "no":
                    print(colored("Dragon: 'You will pay for your cowardice!' The dragon growls menacingly, detroying the village!", "red"))
                    # Add a penalty or consequence here if the player chooses 'no'
                else:
                    print(colored("Invalid choice! Please type 'Yes' or 'No'.", "red"))
            elif leave_choice == "no":
                print(colored("Narrator: You decide to stay inside and not face the dragon.", "green"))
                # You can add more consequences or continuation for choosing 'No' here.
            else:
                print(colored("Invalid input! Please type 'Leave' or 'No'.", "red"))
        elif choice_option == "no":
            print(colored(f"Dragon: You like to give up that easily?! \n UNBELIEVABLE!!!", "light_red"))
        else:
            print(colored("Invalid choice! Please type 'Start' or 'No'.", "red"))
    else:
        print("Invalid letter. Please try again.")
# Function to display character's initial stats
def display_intro(name, hp, inventory, job):
    print(colored(f"Character: {name}", "blue"))  # Display character name
    print(colored(f"Job: {job}", "green"))  # Display character job
    health_bar = f"❤️ {hp}% HP"  # Health bar representation
    print(colored(health_bar, "red"))  # Display health bar
    print(colored("Inventory:", "light_blue"))  # Inventory header
    for item in inventory:  # Loop through inventory items
        print(colored(f"- {item}", "cyan"))  # Display each item
    # Function to choose the path for the journey
    # Ask player to choose a path
def path_choice(name, health, inventory):
    # Ask player to choose a path
    direction_option = input(colored(f"Narrator: Choose a path to begin your journey: Long Dangerous Path or Short Mysterious Path? (LDP/SMP): ", "blue")).lower()
    # If player chooses the long dangerous path
    if direction_option == "ldp":
        print(colored(f"Narrator: You have chosen the long dangerous path, {name}!", "blue"))
        print(colored(f"Narrator: After about half an hour, you began your journey in the late evening as the sun was setting. It was already dark. \nYou had to find a place to rest safely before proceeding.", "blue"))
        sleep_choice = input(colored("Would you sleep in the tree or field? ('Tree' or 'Field'): ", "blue")).lower()
        # If player chooses to sleep in the field
        if sleep_choice == "field":
            print(colored(f"Narrator: You were almost devoured by a pack of hyenas, luckily, you managed to escape, though you sustained some injuries.", "blue"))
            health -= random.randint(18, 24)  # Health damage
            print(colored(f"Narrator: Your current HP is ❤️  {health} HP.", "blue"))
            print(colored(f"Narrator: You can heal up if you have any of the following items: 'Bandage', 'Potion', 'Healing Herb', or 'Health Fruit'. If you do, say 'Heal'.", "blue"))
            # Healing choice
            player_input = input(colored("Say 'Heal' to proceed and check your healing items or 'No': ", "blue")).lower()
            if player_input == "heal":
                healing_items = ['Potion', 'Healing Herb', 'Health Fruit', 'Bandage']
                available_items = [item for item in healing_items if item in inventory]  # Healing items list
                if available_items:
                    health += random.randint(10, 15)  # Heal the player
                    item_used = available_items[0]
                    inventory.remove(item_used)  # Remove one item from the inventory
                    print(colored(f"Narrator: {item_used} has been removed from your inventory.","blue"))
                    print(colored(f"Narrator: Your new inventory is only {inventory} since you have used your healing.", "blue"))
                    print(colored(f"Narrator: Your health has been healed. Your new health is: ❤️  {health} HP.", "blue"))
                else:
                    print(colored(f"Narrator: You don't have any healing items. Your HP is still at: ❤️  {health} HP.", "blue"))
            else:
                print(colored(f"Narrator: You decide not to heal. Your HP is still at: ❤️  {health} HP.", "blue"))
            # Continue story or go to next part
            Wraith_Encounter(health, inventory)  # Continue the journey after healing (or not healing)
        # If player chooses to sleep in the tree
        elif sleep_choice == "tree":
            print(colored(f"Narrator: You sleep safely in the tree, but you get scratched by branches resulting in minor injuries.", "blue"))
            health -= random.randint(12, 18)  # Health damage
            print(colored(f"Narrator: Your current HP is ❤️  {health} HP.", "blue"))
            player_input = input(colored(f"Narrator: Say 'Heal' to proceed and check for healing items or 'No': ", "blue")).lower()
            if player_input == "heal":
                healing_items = ['Potion', 'Healing Herb', 'Health Fruit', 'Bandage']
                available_items = [item for item in healing_items if item in inventory]  # Healing items list
                if available_items:
                    health += random.randint(10, 12)  # Heal the player
                    item_used = available_items[0]
                    inventory.remove(item_used)  # Remove one item from the inventory
                    print(f"{item_used} has been removed from your inventory.")
                    print(colored(f"Narrator: Your new inventory is only {inventory} since you have used your healing.", "blue"))
                    print(colored(f"Narrator: Your health has been healed. Your new health is: ❤️  {health} HP.", "blue"))
                else:
                    print(colored(f"Narrator: You don't have any healing items. Your HP is still at: ❤️  {health} HP.", "blue"))
            else:
                print(colored(f"Narrator: You decide not to heal. Your HP is still at: ❤️  {health} HP.", "blue"))
            # Continue story or go to next part
            Wraith_Encounter(health, inventory)  # Continue the journey after healing (or not healing)
        else:
            print(colored(f"Narrator: Invalid choice. Please choose either 'Tree' or 'Field'.", "red"))
            path_choice(name, health, inventory)  # Recurse to make the player choose again.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    elif direction_option == "smp":
                                                 print(colored(f"Narrator: You have chosen the short mysterious path, {name}!", "blue"))
                                                 print(colored(f"Narrator: You've walked down the steep path, by the river, and found a dark crystal randomly left...\nYou go to pick it up and see what it was...", "blue"))
                                                 item = "Glowing Dark Blue Crystal"  # Item found
                                                 inventory.append(item)  # Add item to inventory
                                                 print(colored(f"New item found: {item}! Current inventory: {inventory}", "blue"))
                                                 print(colored(f"Narrator: You proceeded onward for a couple of hours. \nThe sun was setting and you needed to camp for the night.", "blue"))
                                                 direction_option2 = input(colored("Pick a path: Near River (1) or Cave (2) ", "blue")).lower()
                                                 if direction_option2 == "1":
                                                     print(colored(f"Narrator: You slept near the river. The sound of water calms you.", "blue"))
                                                 elif direction_option2 == "2":
                                                         print(colored(f"Narrator: The cave was very chilly as you went in, a moose gotten scared and shoved you to the floor while it ran out. You still yesdecided to rest in it.", "blue"))
                                                         health -= random.randint(12, 18)
                                                         print(colored(f"Narrator: Your new HP is at: ❤️  {health} HP.","blue"))
                                                 else:
                                                     print(colored(f"Narrator: Invalid choice. Game Over!", "red"))
                                                     return
                                                 print(colored(f"Narrator: You wake up feeling hungry. Your health drops due to hunger.", "blue"))
                                                 health -= random.randint(10, 15)
                                                 print(colored(f"Narrator: Your new HP is at: ❤️  {health} HP.","blue"))
                                                 heal_choice = input(colored("Do you want to heal? [heal] or [no]: ", "blue")).lower()
                                                 if heal_choice == "heal".lower():
                                                         healing_items = ['Healing Herb', 'Potion', 'Health Fruit', 'Bandage']
                                                         if any(healing_item in inventory for healing_item in healing_items):
                                                             heal_amount = random.randint(4, 7)  # Random healing amount
                                                             health += heal_amount  # Heal the player
                                                             # Remove one healing item from inventory after use
                                                             for healing_item in healing_items:
                                                                 if healing_item in inventory:
                                                                     inventory.remove(healing_item)
                                                                     print(colored(f"You've used {healing_item} and felt better! You regained {heal_amount} health. Current HP: ❤️  {health}", "blue"))
                                                                     print(colored(f"Current Inventory - {inventory}", "grey"))
                                                                     break  # Only remove one item at a time
                                                         else:
                                                             print(colored("You don’t have any healing items! You need one of the following: 'Health Fruit', 'Potion', 'Healing Herb', 'Bandage'.", "red"))
                                                             print(colored(f"Your health remains at: ❤️ {health}", "red"))
                                                 else:
                                                     health -= random.randint(22, 30)
                                                     print(colored(f"Narrator: Your health dropped further due to no healing items or not wanting to heal: ❤️ {health}", "blue"))
                                                 print(colored("Narrator: As you move forward, you hear the rustle of leaves in the bushes.", "blue"))
                                                 print(colored("Narrator: Suddenly, a wolf emerges from the shadows, the eyes glowing with hunger.", "blue"))
                                                 print(colored("                   /\\ /|", "blue"))
                                                 print(colored("                  (    <@\\____", "blue"))
                                                 print(colored("                  /        o /", "blue"))
                                                 print(colored("                 /   (___ VV", "blue"))
                                                 choice = input(colored("Do you fight the wolf or try to escape? (Fight/Escape): ", "blue")).lower()
                                                 if choice == "fight".lower():
                                                     print(colored(f"*Fighting...Dodging...Falling...*","yellow"))
                                                     print(colored(f"**Wolf Pouncing...Teeth Baring...Ground Quaking...**","yellow"))
                                                     print(colored(f"***Claws Scratching...Dodging and Rolling...Heart Racing...***","yellow"))
                                                     fight_result = random.choice([True, False])
                                                     if fight_result:
                                                         print(colored(f"Narrator: After a tough battle, you manage to drive the wolf away!", "blue"))
                                                         health -= random.randint(22, 28)  # Health loss from the fight
                                                         print(colored(f"Narrator: After the encounter with the wolf, you continue forward and enter Dimware Valley.", "blue"))
                                                     else: # Player loses the fight
                                                         print(colored(f"Narrator: The wolf overpowers you and sinks its teeth into your arm! You fall unconscious. After a couple hours, you continued", "red"))
                                                         health -= random.randint(20, 30)  # Significant health loss from losing the fight
                                                         print(colored(f"Narrator: Your health drops significantly. Current HP: ❤️ {health}", "red"))
                                                         if health <= 0:
                                                             print(colored(f"Narrator: Game Over! The wolf's attack was too much, and you didn't survive. Better luck next time.", "red"))
                                                             return  # End the game if health is 0 or below
                                                         else:
                                                             print(colored(f"Narrator: You manage to escape the wolf, but your wounds are severe.","light_blue"))
                                                             heal_choice = input(colored("Do you want to heal? [heal] or [no]: ", "blue")).lower()
                                                             if heal_choice == "heal".lower():
                                                                 healing_items = ['Healing Herb', 'Potion', 'Health Fruit', 'Bandage']
                                                                 if any(healing_item in inventory for healing_item in healing_items):
                                                                     heal_amount = random.randint(4, 7)  # Random healing amount
                                                                     health += heal_amount  # Heal the player
                                                                     # Remove one healing item from inventory after use
                                                                     for healing_item in healing_items:
                                                                         if healing_item in inventory:
                                                                             inventory.remove(healing_item)
                                                                             print(colored(f"You've used {healing_item} and felt better! You regained {heal_amount} health. Current HP: ❤️  {health}", "blue"))
                                                                             print(colored(f"Current Inventory - {inventory}", "grey"))
                                                                             break  # Only remove one item at a time
                                                 elif choice == "escape".lower():
                                                         print(colored(f"Narrator: You attempt to run away from the wolf!", "blue"))
                                                         escape = random.choice([True, False])
                                                         if escape == True:
                                                             print(colored(f"Narrator: You managed to outrun the wolf and escape safely!", "blue"))
                                                           # Escape success or failure
                                                         else:
                                                              print(colored(f"Narrator: The wolf catches up to you, and you are forced into a battle!", "red"))
                                                              print(colored(f"*Fighting...Dodging...Falling...*","yellow"))
                                                              print(colored(f"**Wolf Pouncing...Teeth Baring...Ground Quaking...**","yellow"))
                                                              print(colored(f"***Claws Scratching...Dodging and Rolling...Heart Racing...***","yellow"))
                                                              fight_result = random.choice([True, False])
                                                              if fight_result:
                                                                   # Player wins after the second fight
                                                                     print(colored(f"Narrator: You defeat the wolf after a tough battle but lose health", "blue"))
                                                                     health -= random.randint(25, 35)  # Health loss from the second fight
                                                                     print(colored(f"Your current HP is ❤️ {health}", "blue"))
                                                              else:
                                                                   # Player loses the second fight
                                                                     print(colored(f"Narrator: The wolf overpowers you and you fall unconscious once again.", "red"))
                                                                     health -= random.randint(25, 35)  # Significant health loss
                                                                     print(colored(f"Your current HP is ❤️ {health}", "red"))
                                                                     if health <= 0:
                                                                         print(colored("Game Over! You couldn't survive the wolf's attacks. Better luck next time.", "red"))
                                                                         return  # End the game if health is 0 or below
                                                                     else:
                                                                         print(colored(f"Narrator: You manage to escape the wolf after the second fight, but your wounds are severe. Rest is needed.", "blue"))
                                                                         rest_or_continue = input(colored("Do you want to rest and heal (1) or keep going to Dimware Valley (2)? ", "blue")).lower()
                                                                         if rest_or_continue == "1":
                                                                             print(colored(f"Narrator: You decide to rest and tend to your wounds.", "blue"))
                                                                             health += random.randint(9, 14)  # Heal a small amount after resting
                                                                             print(colored(f"Narrator: You regain some health. Current HP: ❤️ {health}", "blue"))
                                                                             print(colored(f"Narrator: You continue your journey after feeling better.", "blue"))
                                                                             # Continue to Dimware Valley or further adventure...
                                                                         elif rest_or_continue == "2":
                                                                             print(colored(f"Narrator: You decide to press on and keep going to Dimware Valley despite your injuries.", "blue"))
                                                                            # Continue to Dimware Valley
                                                 print(colored("""
                                                                                 /\\.               <--- Dimware Valley                       
                                                                                /  \\.                             
                                                                       /\\      /----\\      /\\                     
                                                                      /  \\    /      \\    /  \\.                          
                                                                     /----\\  /        \\  /----\\.                            
                                                                    /      \\/          \\/      \\.                            
                                                                   /_______/\\__________/\\_______\\.                           
                                                                                                                               """, "light_green"))
                                                 print(colored(f"Narrator: As you continue to the valley, a massive troll emerges from behind a huge rock.", "blue"))
                                                 player_response = input(colored(f"Troll: You dare come through this valley without authority from me?! Unless you have an exchange, I will offer you a free pass, otherwise, you will face a fierce battle! \n[Battle] or [Exchange] ", "light_magenta"))
                                                 if player_response in ["[Battle]", "[battle]", "Battle", "battle"]:
                                                       print(colored(f"Troll: 'Prepare to fight, mortal!'", "light_magenta"))
                                                       print(colored("Narrator: You chose to engage in a battle!", "blue"))
                                                       print(colored("*Fighting...Jumping...Falling...*", "yellow"))
                                                       print(colored("**Troll Raging...Ground Shaking...Valley Echoing...**", "yellow"))
                                                       print(colored("***Pushing Through...Managing Attacks...Attempting Energy...***", "yellow"))
                                                       health -= random.randint(28, 48)
                                                       print(colored(f"Your current HP is ❤️ {health}", "red"))
                                                       if health <= 0:
                                                             print(colored("Game Over! You couldn't survive the troll's attacks. Better luck next time.", "red"))
                                                             return
                                                       else: 
                                                             item = "Philosopher's Stone"
                                                             inventory.append(item)
                                                             print(colored(f"Narrator: After a fierce battle, you managed to defeat the troll and pick up the Philosopher's Stone in the valley!", "blue"))
                                                             print(colored(f"New item found: {item}! Current inventory: {inventory}", "green"))
                                                             print(colored("Narrator: You managed to find the Philosopher's Stone and head back to the castle! After countless hours, the dragon found you accomplishing the request! Great Job!", "blue"))
                                                             print(colored("Dragon: Well Well Well...I thought you weren't going to make it. Such a lucky mortal you are....", "red"))
                                                             print(colored("Narrator: The dragon no longer bothers you or the castle. You gave the Philosopher's Stone as it left you peacefully...  \nPrincess was rescued and you all lived!", "light_blue"))
                                                             inventory.remove(item)
                                                             print(colored("Narrator: Game Over!", "light_blue"))
                                                 elif player_response.lower() in ["[exchange]", "exchange"]:
                                                     if "Glowing Dark Blue Crystal" in inventory:
                                                          inventory.remove("Glowing Dark Blue Crystal")
                                                          print(colored(f"Narrator: You offered {item} to the troll.", "blue"))
                                                          item = "Philosopher's Stone"
                                                          inventory.append(item)
                                                          print(colored(f"Troll: Hmm... fair enough. Here, take this.", "light_magenta"))
                                                          print(colored(f"New item received: {item}! Current inventory: {inventory}", "green"))
                                                          print(colored("Narrator: The troll lets you pass. You hurry back to the castle with the Philosopher's Stone in hand.", "blue"))
                                                          print(colored("Narrator: After countless hours, the dragon finds you fulfilling the request... and smiles.", "blue"))
                                                          print(colored("Dragon: Well Well Well...I thought you weren't going to make it. Such a lucky mortal you are....", "red"))
                                                          print(colored("Narrator: The dragon no longer bothers you or the castle. You gave the Philosopher's Stone as it left you peacefully...  \nPrincess was rescued and you all lived!", "light_blue"))
                                                          inventory.remove(item)
                                                          print(colored("Narrator: Game Over!", "light_blue"))
                                                          return
                                                     else:
                                                         print(colored("Troll: You have nothing to offer! Prepare for battle!", "light_magenta"))
                                                         print(colored("Troll: 'Prepare to fight, mortal!'", "light_magenta"))
                                                         print(colored("*Fighting...Jumping...Falling...*", "yellow"))
                                                         print(colored("**Troll Raging...Ground Shaking...Valley Echoing...**", "yellow"))
                                                         print(colored("***Pushing Through...Managing Attacks...Attempting Energy...***", "yellow"))
                                                         health -= random.randint(25, 30)
                                                         print(colored(f"Your current HP is ❤️ {health}", "red"))
                                                         if health <= 0:
                                                             print(colored("Game Over! You couldn't survive the troll's attacks. Better luck next time.", "red"))
                                                             return


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    else:
        print(colored("Invalid choice, please choose 'LDP' or 'SMP'.", "red"))
        path_choice(name, health, inventory)  # Recurse to make the player choose again.
        Wraith_Encounter(health, inventory, name)  # Continue the journey after healing (or not healing)
        print(colored(f"Narrator: Invalid choice. Please choose either 'Tree' or 'Field'.", "red"))
        path_choice(name, health, inventory)  # Recurse to make the player choose again.
def Wraith_Encounter(health, inventory):
    print(colored(f"Narrator: As you continue for another couple of hours, you find 2 glowing, floating entities... almost invisible. They seem harmless, so you approach one to ask about the path to 'Dimware Valley.'", "blue"))
    print(colored(f"Narrator: One entity states: ", "blue"))
    print(colored(f"Wraith_#2: For what reason do you seek that destination? What has led you down such a dark path?", "grey"))
    print(colored(f"Narrator: You must answer: 'A quest from the dragon.' or 'An urgent requirement to fulfill.'", "blue"))
    player_response_W = input(colored("Answer: ", "light_yellow")).lower()  # Player input from options given
    if player_response_W in [
        "a quest from the dragon", "a quest from the dragon.", "A Quest From The Dragon.", "A Quest From The Dragon", 
        "an urgent requirement to fulfill", "an urgent requirement to fulfill.", "An urgent requirement to fulfill.", "An Urgent Requirement To Fulfill"]:
        print(colored(f"Wraith_#1: In that case however, take the path you were heading into, for another 3-4 hours. Yet, you will face obstacles, such as deadly entities and terrain.", "grey"))
        print(colored(f"Wraith_#2: Since now you know the way, and voids you'll face, you must repay us back. For that, give us one of the following: 'Sanctional Ruby' || 'Wand' || 'Holy Book' || 'Poison'. ", "grey"))
        print(colored(f"Wraith_#1: Ah yes! In order for your soul to not fall into a trap by our command, you must give one of the following as requested for a payback of our advising...", "grey"))
        # Player input
        player_response_O = input(colored("Narrator: Give one of the following: 'Holy Book' or 'Wand' or 'Sanctional Ruby' or 'Poison.'" "If none or not 'trust' them, say 'Continue' if you desire them for better use: ", "blue")).lower()
# List of valid repay items
        repay_items = ['sanctional ruby', 'wand', 'holy book', 'poison']
# Check if the player's response is a valid repay item
    if player_response_O in repay_items:
    # Try to find matching item in inventory (case-insensitive)
         item_to_remove = next((item for item in inventory if item.lower() == player_response_O), None)
         if item_to_remove:
          print(colored("Narrator: You gave one of the required items to the wraiths and continue your journey.", "blue"))
          print(colored("Narrator: However, you still feel like they lied and are making you worried as if a weakness was cast upon you...", "blue"))
          health -= random.randint(10, 15)
          print(colored(f"Narrator: Your health decreases. Your new health is: ❤️ {health} HP.", "red"))
          inventory.remove(item_to_remove)
         else:
          print(colored(f"Narrator: You do not have the item '{player_response_O}' in your inventory!", "red"))
          print(colored("Narrator: You will continue without paying the wraiths back.", "blue"))
          health -= random.randint(11, 28)
          print(colored(f"Narrator: Your health is now: ❤️ {health} HP.", "red"))
        # If player enters something other than a valid option
    # Function to handle extra obstacles in the journey
    elif player_response_O == "Continue" or "continue":
        print(colored("Narrator: You will continue without paying the wraiths back. You feel as if you gottened a spell casted upon you.", "blue"))
        health -= random.randint(11, 28)
        print(colored(f"Narrator: Your health is now: ❤️ {health} HP.", "red"))
        print(colored(f"Narrator: You managed to get through the obstacle. As you continue, the path ahead is still treacherous.", "blue"))
        print(colored(f"Narrator: The sun begins to set as you feel the weight of the journey on your shoulders.", "blue"))
    else:
        print(colored("Invalid letter. Please try again.", "red"))
        Wraith_Encounter(health, inventory)  # Retry the input if the first condition is not met
    # This will take the game to the next challenge
    obstacles(health, inventory)

def obstacles(health, inventory):
    print(colored(f"Narrator: Another hour, you have come near the end of the mountain, the terrain grows more treacherous. A long old rickety wooden-bridge is your option or find a different route...", "blue"))
    bridge_choice = input(colored("Narrator: Do you want to cross the bridge, or try to find another way? (Cross/Find): ", "blue")).lower()
    # If player chooses to cross the bridge
    if bridge_choice == "cross":
        print(colored(f"Narrator: The weak bridge creaks under your weight, and halfway across, a piece of the bridge loosens abruptly away!", "blue"))
        print(colored(f"Narrator: You must make a quick decision to either jump onto a pine tree or grab onto a nearby rope hanging from the side onto a flat surface beneath you near the river?!", "blue"))
        jump_choice = input(colored(f"Narrator: Do you jump or grab the rope? (Jump/Rope): ", "blue")).lower()
        # If player chooses to jump
        if jump_choice == "jump":
            print(colored(f"Narrator: You jump, but the impact with the water knocks the wind out of you, causing minor scratched injuries from sliding down the pine tree.", "blue"))
            health -= random.randint(7, 12)  # Decrease health
            print(colored(f"Narrator: Your new health is now ❤️  {health} HP.", "blue"))
        # If player chooses to grab the rope
        elif jump_choice == "rope":
            print(colored(f"Narrator: You grab the rope just in time and swing to safety. However, as your foot slipped off of the edge of the mountain side, you lost grip, and fell into the long river, losing a bit of health!", "blue"))
            health -= random.randint(10, 15)  # Health damage
            print(colored(f"Narrator: Your new health is now ❤️  {health} HP.", "blue"))
        else:
            print(colored(f"Narrator: Unable to decide in time, you fall into the river and lose some health.", "blue"))
            health -= random.randint(10, 12)  # Decrease health
            print(colored(f"Narrator: Your new health is now ❤️  {health} HP.", "blue"))
        # After the obstacle, continue the journey, including goblin encounter
        goblin_encounter(health, inventory)  # Go straight to goblin encounter after crossing or finding another way
    # If player chooses to find another way
    elif bridge_choice == "find":
        print(colored(f"Narrator: You decide to look for another way, but you soon find yourself in a thick patch of brambles.", "blue"))
        print(colored(f"Narrator: The brambles seem to be full of thorns. You must decide if you want to cut through or try to go around.", "blue"))
        bramble_choice = input(colored(f"Narrator: Do you cut through the brambles or try to go around? (Cut/Go Around): ", "blue")).lower()
        # If player chooses to cut through
        if bramble_choice == "cut":
            print(colored(f"Narrator: You cut through the brambles, but a thorn scratches your arms and legs! \nYou still proceed along your journey...", "blue"))
            health -= random.randint(15, 18)
            print(colored(f"Narrator: Your new health is now ❤️  {health} HP.", "blue")) # Decrease health
            goblin_encounter(health, inventory)  # Continue to the goblin encounter after cutting through the brambles
        # If player chooses to go around
        elif bramble_choice == "go around":
            print(colored(f"Narrator: You carefully maneuver around the brambles, but the detour adds extra time to your journey.", "blue"))
            print(colored(f"Narrator: As you travel further, you encounter a mysterious house along with a farm. You notice an elderly man by the farm.", "blue"))
            print(colored(f"Farmer: Young one! What brings you this far from the castle?", "light_cyan"))
            player_Response = input(colored(f"Narrator: Answer by responding 'Dragon quest' or 'Important requirement'. ", "blue")).lower()
            # Check for valid response
            valid_responses = ["dragon quest", "important requirement"]
            if player_Response in valid_responses:
                print(colored(f"Farmer: Ahhh...I see. I won't delay you further, but I will advise to take rest young one. A journey needs rest, not only time. It will also recover you too!", "light_cyan"))
                # Ask if the player wants to rest
                player_rest = input(colored(f"Narrator: If you would like to rest for a day, then say 'Y', if not then say 'N'. ", "blue")).lower()
                if player_rest == "y":
                    print(colored(f"Narrator: You have chosen to rest for 1 day, and woke up early in sunrise. You also regained some health back! You proceeded back on track.", "blue"))
                    print(colored(f"Farmer: Take care now young one, and have a safe rest of your journey.", "light_cyan"))
                    heal_amount = random.randint(15, 25)  # Random healing
                    health += heal_amount  # Increase health   
                    print(colored(f"Narrator: Your health is now ❤️  {health} HP. You continued.", "blue"))
                elif player_rest == "n":
                    print(colored(f"Narrator: You decided to skip and get back on track, your health is still ❤️  {health} HP.", "blue"))
                else:
                    print(colored(f"Narrator: Unable to choose, you end up getting stuck in the brambles for too long. Time lost.", "blue"))
                    print(colored(f"Narrator: You've lost precious time, and your journey grows more difficult.", "blue"))
                goblin_encounter(health, inventory)  # Continue to goblin encounter
            else:
                print(colored(f"Narrator: Invalid response! Please choose correctly.", "red"))
                obstacles(health, inventory)  # Loop back to obstacle choice
        else:
            print(colored(f"Narrator: Invalid choice, please try again.", "red"))
            obstacles(health, inventory)  # Loop back to obstacle choice.
    else:
        print(colored("Invalid choice. Please try again.", "red"))
        obstacles(health, inventory)  # Repeat the obstacle choices if input is invalid.
def goblin_encounter(health, inventory):
    # Setting the scene, the player is on their journey and enters a foggy ravine.
    print(colored(f"Narrator: After hours of treacherous travel, you find yourself entering a foggy swamp, the air heavy and thick with the scent of moss.", "blue"))
    print(colored(f"Narrator: As you push forward, the faint sound of metal clashing and low growls breaks the silence. You cautiously approach the source of the noise.", "blue"))
    print(colored(f"Narrator: Through the mist, you see a group of goblins huddled around a fire, sharpening their crude weapons. They seem to be waiting for something... or someone.", "blue"))
    # Goblins notice the player, adding a sense of tension
    print(colored(f"Goblin Leader: 'Well well, look what we have here! *SNORK* Another fool wandering too deep into our territory. *SNORK*'", "green"))
    print(colored(f"Narrator: The goblins start to encircle you, eyeing your gear and looking at each other with mischievous grins.", "blue"))
    # Player has the choice to offer or fight
    choice = input(colored("Goblin Leader: 'You're lucky we will give you two choices, traveler. *SNORK* You can offer something of value to us, or you can fight for your life. What will it be? *SNORK* (Offer/Fight): ", "green")).lower()
    # If the player chooses to offer
    if choice == "offer":
        print(colored(f"Narrator: You carefully consider your options, looking at the items in your bag.", "light_blue"))
        # Check if the player has an item to offer
        offerable_items = ['Wand', 'Life Shield', 'Helmet', 'Sanctional Ruby', 'Lockpick']
        if any(item in inventory for item in offerable_items):
            offered_item = next(item for item in inventory if item in offerable_items)
            print(colored(f"Narrator: You offer the goblins your {offered_item}. Their eyes widen with greed as they snatch it from your hands.", "light_blue"))
            print(colored(f"Goblin Leader: 'This will do. You may pass, but remember, not all encounters are so easy. *SNORK SNORK*'", "green"))
            inventory.remove(offered_item)  # Remove the item from the inventory
            continue_journey(health, inventory)  # Proceed with the journey
        else:
            print(colored(f"Narrator: You attempt to offer something to the goblins, but they look through your pack and scoff.", "blue"))
            print(colored(f"Goblin Leader: 'You carry nothing of value. It seems your only choice is to fight! *SNORK*'", "light_green"))
            print(colored(f"Goblin: 'Prepare to face the fury of a goblin, mortal!'", "light_green"))
            print(colored(f"*Goblins Sorks...Stabbing...Ducking...*","green"))
            print(colored(f"**Goblins Claws Slashing...Screeching...Shadows Growing...**","green"))
            print(colored(f"***Dodging Blades...Countering With Speed...Gathering strength...***","green"))
            health -= random.randint(6, 12)
            # Proceed to fight if no offerable item
            fight_result = random.choice([True, False])  # 50/50 chance to win or lose
            if fight_result:
                print(colored(f"Narrator: You fight with determination and defeat the goblins! The leader falls first, and the others scatter in fear.", "blue"))
                continue_journey(health, inventory)  # Proceed with the journey
            else:
                print(colored(f"Narrator: The goblins overpower you with their numbers, and you barely escape with your life, wounded.", "blue"))
                health -= random.randint(15, 25)  # Player loses health if they lose the fight
                continue_journey(health, inventory)  # Proceed with the journey
    # If the player chooses to fight
    elif choice == "fight":
        print(colored(f"Narrator: You draw your weapon and prepare to face the goblins!", "blue"))
        print(colored(f"Goblin: 'Prepare to face the fury of a goblin, mortal!'", "light_green"))
        print(colored(f"*Goblins Snorks...Stabbing...Ducking...*","green"))
        print(colored(f"**Goblins Claws Slashing...Screeching...Shadows Growing...**","green"))
        print(colored(f"***Dodging Blades...Countering With Speed...Gathering Strength...***","green"))

        # Fight logic with a 50/50 outcome
        fight_result = random.choice([True, False])  # 50/50 chance to win or lose
        if fight_result:
            print(colored(f"Narrator: You fight with determination and defeat the goblins! The leader falls first, and the others scatter in fear.", "blue"))
            health -= random.randint(6, 12)
            continue_journey(health, inventory)  # Proceed with the journey
        else:
            print(colored(f"Narrator: The goblins overpower you with their numbers, and you barely escape with your life, wounded.", "blue"))
            health -= random.randint(15, 25)  # Player loses health if they lose the fight
            if health <= 0:
                print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                return  # Exit the game if health reaches 0
            continue_journey(health, inventory)  # Proceed with the journey
    else:
        print(colored(f"Narrator: Invalid choice. The goblins grow impatient and attack!", "blue"))
        health -= random.randint(15, 20)
        if health <= 0:
            print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
            return  # Exit the game if health reaches 0
        print(colored(f"Narrator: Your current HP is ❤️ {health} HP", "blue"))
        continue_journey(health, inventory)  # Retry the encounter if invalid choice
    # After the encounter, transition to the next part of the journey (Cyclops)
    print(colored(f"Narrator: After overcoming the obstacles, enemies, and tension, you find yourself on the final stretch towards Dimware Valley.", "blue"))
    Witch_obstacle(health, inventory)
def Witch_obstacle(health, inventory):
    # Ask if the player wants to confront or hide
    Witch_obstacle_choice = input(colored("Narrator: A dark figure emerges from the fog ahead. Do you want to confront it, or hide and wait? (Confront/Hide): ", "blue")).lower()
    # If player chooses to confront the figure
    if Witch_obstacle_choice == "confront":
        print(colored(f"Narrator: You boldly approach the figure, revealing it to be a terrifying witch!", "blue"))
        print(colored(f"Witch: 'You seek the Philosopher's Stone, do you not? Prove your worth, and I shall allow you passage.'", "magenta"))
        Witch_choice = input(colored("Narrator: Do you want to fight the witch or try to negotiate? (Fight/Negotiate): ", "blue")).lower()
        # If player chooses to fight
        if Witch_choice == "fight":
            print(colored("Narrator: You draw your weapon and engage in battle!", "blue"))
            if "Sword" in inventory or "Battle Axe" in inventory or "Dagger" in inventory or "Blessing Oil" in inventory or "Knife" in inventory or "Life Shield" in inventory:
                print(colored(f"Witch: 'Prepare to fight, imbecile!'", "magenta"))
                print(colored(f"*Fighting...Defending...Running...*", "yellow"))
                print(colored(f"**Witch Spells...Glass Shattering...Frogs Hopping...**", "yellow"))            #typed 'humping' instead of 'hopping' lmaoooooo
                print(colored(f"***Building Defense...Managing Attacks...Blocking Spells...***", "yellow"))
                print(colored(f"Narrator: Your weapon and defense are strong, and with skillful strikes, you defeat the witch!", "blue"))
                print(colored(f"Narrator: You have earned passage to Dimware Valley, but still gotten some damage.", "blue"))
                health -= random.randint(20, 27)
                if health <= 0:
                    print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                    return  # Exit the game if health reaches 0
                print(colored(f"Narrator: Your current HP is ❤️ {health} HP", "blue"))  # Battle damage
            else:
                print(colored(f"Narrator: Without a powerful weapon, the witch casts spells you.", "blue"))
                health -= random.randint(20, 27)
                if health <= 0:
                    print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                    return
                print(colored(f"Narrator: Your current HP is ❤️  {health} HP", "blue"))
        # If player chooses to negotiate
        elif Witch_choice == "negotiate":
            print(colored("Narrator: You attempt to reason with the witch, offering her a peaceful solution.", "blue"))
            negotiation_success = random.choice([True, False])
            if negotiation_success:
                print(colored("Narrator: Your negotiation is successful! The witch grants you passage to Dimware Valley.", "light_blue"))
            else:
                print(colored("Narrator: The witch does not take kindly to your words, and you are forced to fight.", "blue"))
                print(colored(f"Witch: 'Prepare to fight, imbecile!'", "magenta"))
                print(colored(f"*Fighting...Defending...Running...*", "yellow"))
                print(colored(f"**Witch Spells...Glass Shattering...Frogs Hopping...**", "yellow"))                   #typed 'humping' instead of 'hopping' lmaoooooo
                print(colored(f"***Building Defense...Managing Attacks...Blocking Spells...***", "yellow"))
                health -= random.randint(15, 20)
                if health <= 0:
                    print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                    return  # Exit the game if health reaches 0
                print(colored(f"Narrator: Your current HP is ❤️ {health} HP", "blue"))  # Minor damage from the negotiation failure
        else:
            print(colored("Invalid choice! The witch grows impatient and attacks.", "red"))
            health -= random.randint(15, 25)
            if health <= 0:
                print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                return  # Exit the game if health reaches 0
            print(colored(f"Narrator: Your current HP is ❤️ {health} HP", "blue"))
        # Continue journey after dealing with the witch
        cyclops_encounter(health, inventory)  # Transition to the Cyclops encounter
    # If player chooses to hide
    elif Witch_obstacle_choice == "hide":
        print(colored("Narrator: You decide to hide and wait, hoping the witch passes by.", "blue"))
        # 50/50 chance of being found or not
        hide_success = random.choice([True, False])
        if hide_success:
            print(colored("Narrator: You remain hidden, and the witch moves on without noticing you.", "blue"))
            cyclops_encounter(health, inventory)  # Continue to the Cyclops encounter
        else:
            print(colored("Narrator: Unfortunately, the witch senses your presence and finds you!", "blue"))
            print(colored(f"Witch: 'Prepare to fight, imbecile!'", "magenta"))
            print(colored(f"*Fighting...Defending...Running...*", "yellow"))
            print(colored(f"**Witch Spells...Glass Shattering...Frogs Hopping...**", "yellow"))                   #typed 'humping' instead of 'hopping' lmaoooooo
            print(colored(f"***Building Defense...Managing Attacks...Blocking Spells...***", "yellow"))
            health -= random.randint(15, 20)
            if health <= 0:
                print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                return  # Exit the game if health reaches 0
            print(colored(f"Narrator: Your current HP is ❤️ {health} HP", "blue"))
            # Proceed to the Cyclops encounter after the fight, rather than retrying the witch encounter
            cyclops_encounter(health, inventory)
    else:
        print(colored("Invalid choice! The witch grows impatient and attacks.", "red"))
        health -= random.randint(20, 25)
        print(colored(f"Narrator: Your current HP is ❤️  {health} HP", "blue"))
        Witch_obstacle(health, inventory)  # Retry the encounter if invalid choice
# Function to proceed to Cyclops encounter after witch or any obstacle
def cyclops_encounter(health, inventory):
    print(colored(f"Narrator: You find yourself crossing a vast plain when suddenly, the earth shakes. A Cyclops emerges in the distance.", "blue"))
    print(colored(f"Narrator: The Cyclops roars and approaches you, its enormous club swinging menacingly at its side.", "blue"))
    print(colored(f"Cyclops: 'Surrender, mortal, or face my wrath!'", "yellow"))
    choice = input(colored("Do you offer something to the Cyclops or fight? (Offer/Fight): ", "green")).lower()
    if choice == "offer":
        print(colored(f"Narrator: You look through your inventory, considering what to offer.", "blue"))
        offerable_items = ["Sanctional Ruby", "Potion", "Holy Book", "Blessing Oil", "Healing Herb"]
        if any(item in inventory for item in offerable_items):
            offered_item = next(item for item in inventory if item in offerable_items)
            print(colored(f"Narrator: You offer the Cyclops your {offered_item}. It accepts the gift with a greedy grin.", "light_blue"))
            inventory.remove(offered_item)
            continue_journey(health, inventory)  # Proceed after offering an item
        else:
            print(colored(f"Narrator: You have nothing the Cyclops values. It grows furious!", "blue"))
            print(colored(f"Cyclops: 'Prepare to fight, mortal!'","yellow"))
            fight_result = random.choice([True, False])
            if fight_result:
                print(colored(f"Narrator: You defeat the Cyclops in battle!", "blue"))
                health -= random.randint(4, 8)
                if health <= 0:
                    print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                    return  # Exit the game if health reaches 0
                print(colored(f"Narrator: Your current HP is ❤️ {health} HP", "blue"))
                continue_journey(health, inventory)
            else:
                print(colored(f"Narrator: The Cyclops overpowers you. You barely stayed alive.", "blue"))
                health -= random.randint(20, 30)
                if health <= 0:
                    print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                    return  # Exit the game if health reaches 0
                continue_journey(health, inventory)
    elif choice == "fight":
        print(colored(f"Narrator: You engage into defense and get ready for combat with the Cyclops!", "blue"))
        fight_result = random.choice([True, False])
        if fight_result:
            health -= random.randint(10, 15)
            if health <= 0:
                print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                return  # Exit the game if health reaches 0
            print(colored(f"Narrator: Your current HP is ❤️ {health} HP", "blue"))
            print(colored(f"Narrator: With all your strength, you defeat the Cyclops!", "blue"))
            continue_journey(health, inventory)
        else:
            print(colored(f"Narrator: The Cyclops overpowers you!", "blue"))
            health -= random.randint(20, 30)
            if health <= 0:
                print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                return  # Exit the game if health reaches 0
            print(colored(f"Narrator: Your current HP is ❤️ {health} HP", "red"))
            continue_journey(health, inventory)
    else:                           
        print(colored("Invalid choice! Please choose to 'Confront' or 'Hide'.", "red"))
        Witch_obstacle(health, inventory)  # Retry if invalid input
def continue_journey(health, inventory):
    print(colored(f"Narrator: Your current HP is ❤️ {health} HP", "blue"))
    print(colored(f"Your current inventory is: {inventory}", "light_grey"))
def cyclops_encounter(health, inventory):
    print(colored(f"Narrator: You continued onward, just as you were going into the Dimware Valley road, you have a bad sense of feeling...",'blue'))
    print(colored(f"Narrator: You find yourself crossing a vast plain when suddenly, the ground shakes. A cyclops emerges in the distance.", "blue"))
    print(colored(f"Narrator: The cyclops roars and approaches you, its enormous club swinging menacingly at its side.", "blue"))
    print(colored(f"Cyclops: 'Surrender, mortal, or face my wrath!'", "yellow"))
    choice = input(colored("Do you offer something to please the Cyclops or fight? (Offer/Fight): ", "light_yellow")).lower()
    if choice == "offer":
        print(colored(f"Narrator: You look through your inventory, considering what to offer.", "blue"))
        offerable_items = ["Sanctional Ruby", "Potion", "Holy Book", "Blessing Oil", "Healing Herb"]
        if any(item in inventory for item in offerable_items):
            offered_item = next(item for item in inventory if item in offerable_items)
            print(colored(f"Narrator: You offer the cyclops your {offered_item}. It accepts the gift with a greedy grin.", "blue"))
            print(colored(f"Cyclops: I better not see you back on the same path again, or you won't be as lucky next time....","yellow"))
            inventory.remove(offered_item)
            continue_journey(health, inventory)  # Proceed after offering an item
        else:
            print(colored(f"Narrator: You have nothing the Cyclops values. It grows furious!", "blue"))
            print(colored(f"Cyclops: 'Prepare to fight, mortal!'", "yellow"))
            print(colored(f"*Fighting...Dodging...Falling...*","light_yellow"))
            print(colored(f"**Cyclops Pounding...Ground Shaking...Cracks Forming...**","light_yellow"))
            print(colored(f"***Pushing Through...Managing Attacks...Attempting Energy...***","light_yellow"))
            fight_result = random.choice([True, False])
            if fight_result:
                print(colored(f"Narrator: You defeat the Cyclops in battle!", "blue"))
                health -= random.randint(8, 10)
                if health <= 0:
                    print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                    return  # Exit the game if health reaches 0
                continue_journey(health, inventory)
            else:
                print(colored(f"Narrator: The Cyclops overpowers you. You barely escape with your life.", "blue"))
                health -= random.randint(20, 30)
                if health <= 0:
                    print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                    return  # Exit the game if health reaches 0
                print(colored(f"Narrator: Your current HP is ❤️ {health} HP", "blue"))
                continue_journey(health, inventory)
    elif choice == "fight":
        print(colored(f"Narrator: You draw your weapon or fists and engage in combat with the Cyclops!", "blue"))
        print(colored(f"Cyclops: 'Prepare to fight, mortal!'", "light_yellow"))
        print(colored(f"*Fighting...Dodging...Falling...*","yellow"))
        print(colored(f"**Cyclops Pounding...Ground Shaking...Cracks Forming...**","yellow"))
        print(colored(f"***Pushing Through...Managing Attacks...Attempting Energy...***","yellow"))
        fight_result = random.choice([True, False])
        if fight_result:
            print(colored(f"Narrator: With all your strength, you defeat the Cyclops!", "blue"))
            health -= random.randint(5, 8)
            if health <= 0:
                print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                return  # Exit the game if health reaches 0
            continue_journey(health, inventory)
        else:
            print(colored(f"Narrator: The Cyclops overpowers you!", "blue"))
            health -= random.randint(20, 30)
            if health <= 0:
                print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                return  # Exit the game if health reaches 0
            print(colored(f"Narrator: Your current HP is ❤️ {health} HP", "blue"))
            continue_journey(health, inventory)
    troll_encounter(health, inventory)
def troll_encounter(health, inventory):
    print(colored("Narrator: After you continued through the Dimware Valley, a massive troll emerges from behind a huge rock. It snarls, glaring at you with hatred.", "blue"))
    print(colored("Troll: 'You trespass in MY domain, human. Pay the price or face my wrath!'", "light_magenta"))
    choice = input(colored("Narrator: Do you fight the troll or try to hide? (Fight/Hide): ", "blue")).lower()
    if choice == "fight":
        print(colored("Narrator: You draw your weapon or fists, ready to face the troll!", "blue"))
        fight_result = random.choice([True, False])
        if fight_result:
            print(colored(f"*Fighting...Dodging...Falling...*","yellow"))
            print(colored(f"**Troll Pounding...Ground Shaking...Dust Forming...**","yellow"))
            print(colored(f"***Hitting Through...Managing Attacks...Saving Life...***","yellow"))
            item = "Philosopher's Stone"  # Item found
            inventory.append(item)  # Add item to inventory
            print(colored(f"New item found: {item}! Current inventory: {inventory}", "green"))
            print(colored(f"Narrator: After a fierce battle, you managed to defeat the troll, pick up the Philosopher's Stone in the valley!", "blue"))
            print(colored(f"Narrator: You managed to find the Philosopher's Stone and head back to the castle! After countless hours, the dragon found you accomplishing the request! Great Job!","blue"))
            print(colored(f"Dragon: Well Well Well...I thought you weren't going to make it. Such a lucky mortal you are....", "red"))
            print(colored(f"The dragon no longer bothers you or castle. You gave the Philosopher's Stone as it left you peacefully...  \nPrincess was rescued and you all lived!","blue"))
            inventory.remove(item)
            print(colored(f"Narrator: Game Over!","light_blue"))
            health -= random.randint(5, 8)
            continue_journey(health, inventory)
        else:
            print(colored("Narrator: The troll strikes you with its massive club. You are knocked to the ground!", "blue"))
            health -= random.randint(20, 30)  # Damage from the troll
            if health <= 0:
                print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                return  # Exit the game if health reaches 0
            else:
                  item = "Philosopher's Stone"
                  inventory.append(item)
                  print(colored(f"New item found: {item}! Current inventory: {inventory}", "green"))
                  print(colored(f"Narrator: You managed to find the Philosopher's Stone in the cave near the troll's base and head back to the castle! You made a run and left the valley while stealing the {item}. \nAfter countless hours, the dragon found you accomplishing the request! Great Job!","blue"))
                  print(colored(f"Dragon: Well Well Well...I thought you weren't going to make it. Such a lucky mortal you are....", "red"))
                  print(colored(f"The dragon no longer bothers you or castle. You gave the Philosopher's Stone as it left you peacefully... \nPrincess was rescued and you all lived!","blue"))
                  inventory.remove(item)
                  print(colored(f"Narrator: Game Over!","light_blue"))
                  health -= random.randint(5, 8)
                  continue_journey(health, inventory)
    elif choice == "hide":
        print(colored("Narrator: You try to find a hidden spot behind some rocks, hoping the troll doesn't notice you.", "blue"))
        hide_success = random.choice([True, False])
        if hide_success:
            print(colored(f"Narrator: The troll sniffs the air, but doesn't seem to notice you hiding. You manage to slip away!", "blue"))
            item = "Philosopher's Stone"  # Item found
            inventory.append(item)  # Add item to inventory
            print(colored(f"New item found: {item}! Current inventory: {inventory}", "green"))
            print(colored(f"Narrator: You managed to find the Philosopher's Stone and head back to the castle! After countless hours, the dragon found you accomplishing the request! Great Job!","blue"))
            print(colored(f"Dragon: Well Well Well...I thought you weren't going to make it. Such a lucky mortal you are....", "red"))
            print(colored(f"The dragon no longer bothers you or castle. You gave the Philosopher's Stone as it left you peacefully... \nPrincess was rescued and you all lived!","blue"))
            inventory.remove(item)
            print(colored(f"Narrator: Game Over!","light_blue"))
            health -= random.randint(5, 8)
            continue_journey(health, inventory)
        else:
            print(colored("Narrator: The troll hears your movements and turns toward you, enraged, comes charging at you!", "blue"))
            print(colored(f"Troll: 'Prepare to fight, mortal!'", "light_magenta"))
            print(colored(f"*Fighting...Jumping...Falling...*","yellow"))
            print(colored(f"**Troll Raging...Ground Shaking...Valley Echoing...**","yellow"))
            print(colored(f"***Pushing Through...Managing Attacks...Attempting Energy...***","yellow"))
            health -= random.randint(14, 18)  # Damage from the troll noticing you
            item = "Philosopher's Stone"  # Item found
            inventory.append(item)  # Add item to inventory
            print(colored(f"New item found: {item}! Current inventory: {inventory}", "green"))
            print(colored(f"Narrator: You managed to find the Philosopher's Stone after the rage. You speeded back to the castle! After countless hours, the dragon found you have accomplished the request! Great Job!", "blue"))
            print(colored(f"Dragon: Well Well Well...I thought you weren't going to make it. Such a lucky mortal you are....", "red"))
            print(colored(f"Narrator: The dragon flew away...never to be seen again.","blue"))
            print(colored(f"The dragon no longer bothers you or castle. You gave the Philosopher's Stone as it left you peacefully... \nPrincess was rescued and you all lived!","blue"))
            inventory.remove(item)
            print(colored(f"Narrator: Game Over!","light_blue"))
            if health <= 0:
                 print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
                 return  # Exit the game if health reaches 0
        continue_journey(health, inventory)
    else:
        print(colored("Narrator: Invalid choice! The troll growls impatiently and strikes!", "blue"))
        health -= random.randint(15, 20)  # Minor damage from the troll for invalid choice
        if health <= 0:
            print(colored("Game Over! You have fallen in battle. Better luck next time.", "red"))
            return  # Exit the game if health reaches 0
        print(colored(f"Narrator: Your current HP is ❤️  {health} HP", "blue"))
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
while True:
    create_character()  # Start the character creation and game
    play_again = input(colored(f"\nWould you like to create another character? (yes/no): ", "yellow")).lower()
    if play_again != 'yes':
        print(colored(f"Thank you for taking your time and I hope you have enjoyed!", "blue"))
        break