import time

import random

# Create a pause between messages in the game.
def print_pause(message, delay=0):
    print(message)
    time.sleep(delay)

# List of monster names that will be used when the game randomly generates
# a monster.
monster_name = ["Rajang", "Khezu", "Lunastra", "Rathian", "Rathalos",
                "Yian Kut-Ku"]

# List of weapon names that will be used when the game randomly generates
# a weapon.
weapon_name = ["Voidsteel Sword", "Dwarven Axe", "Excalibur",
               "William Wallace Sword", "Elven Inferno Staff"]

# Define a function that confirms a player's input is valid.
def valid_input(prompt, options):
    # continuous loop over current prompt while true.
    while True:
        # create variable that lowercases player's input.
        option = input(prompt).lower()
        # If variable is within the list of options.
        if option in options:
            # return the player's input.
            return option
        # If input is incorrect, loop will break, and print try again.
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')

# Define introduction to the game.
def intro():
    print_pause("You are an aspiring Merchant from the City Evermore,"
                " looking \nto open up a Merchant Guild in the nearby "
                "town of Rivenspire.", 1.5)
    print_pause("Rivenspire is surrounded by three different types of "
                "terrain.", 1.5)
    print_pause("Hammerfell Mountain Range to the West, Tebath River to the"
                " South, \nand the Forest of Morrowind to the North and East.",
                1.5)
    print_pause("You will need to find the safest path to Rivenspire in "
                "order to create a trade route.\n", 1.5)

# Define a function call for starting exploration; include three parameters for
# monster name, weapon type, and current set of items. These three parameters
# will need to be include in all defined functions.
def exploration(monster, weapon, items):
    # Print explanation of where the player can travel from Evermore.
    print_pause("Enter 1 to travel to Hammerfell Mountains.\nEnter 2 to travel"
                " to the Forest of Morrowind.\nEnter 3 to travel by the Tebath"
                " River.\nWhat would you like to do?", .5)
    # Ask the player if they would like to travel to Hammerfell, Morrowind, or
    # Tebath.
    # validate the input with valid_input.
    choice = valid_input("(Please enter 1, 2, or 3.)\n", ["1", "2", "3"])
    # if 1 is selected the Hammerfell function is called, if 2 the Morrowind
    # function is called, and if 3 the Tebath function is called.
    if choice == "1":
        Hammerfell(monster, weapon, items)
    elif choice == "2":
        Morrowind(monster, weapon, items)
    elif choice == "3":
        Tebath(monster, weapon, items)

# Define function call for Hammerfell location, include mountain and cave
# scenarios.
def Hammerfell(monster, weapon, items):
    print_pause("You travel along the Hammerfell Mountain Range.", 1.5)
    print_pause("The path diverges up the mountain or into a cave.", 1.5)
    # Created a separate function for the mountain choice.
    mountain(monster, weapon, items)

# Mountain function defines wether the player will enter the cave, continue up
# the mountain, or return to the starting point in Evermore.
def mountain(monster, weapon, items):
    mountain_choice = valid_input("Enter 1 to continue up the path.\n"
                                  "Enter 2 to enter the cave.\n"
                                  "Enter 3 to return to Evermore.\n",
                                  ["1", "2", "3"])
    # if player selects 1, mountain_range function is called, if 2 then the
    # cave function is called, and if 3 then the exploration function is called.
    if mountain_choice == "1":
        mountain_range()
    elif mountain_choice == "2":
        cave(monster, weapon, items)
    elif mountain_choice == "3":
        print_pause("You are welcomed back by the Guards at the Front Gate.",
                    1.5)
        exploration(monster, weapon, items)

# Define moutain_range scenario if the player continues up the mountain.
def mountain_range():
    print_pause("As you move along the path, you hear a sudden rumble "
                "from above.", 1.5)
    print_pause("OH NO! It's an avalanche. You try to flee, but are crushed "
                "by the boulders above.", 1.5)
    print_pause("GAME OVER", 1)

# Define cave scenario, player will recevie their weapon and be sent back to
# the moutain trail. If the player has already visited the cave they will
# receive nothing and be sent back to the trail.
def cave(monster, weapon, items):
    if "weapon" in items:
        print_pause("You peer cautiously into the cave.", 1.5)
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.", 1.5)
        print_pause("You walk back out to the trail path.", 1.5)
        mountain(monster, weapon, items)
    else:
        print_pause("You peer cautiously into the cave.", 1.5)
        print_pause("It turns out to be only a very small cave.", 1.5)
        print_pause("Your eye catches a glint of metal behind a rock.", 1.5)
        print_pause(f"You have found the {weapon} of Ogoroth!", 1.5)
        print_pause("Better safe than sorry on your adventure.", 1.5)
        print_pause("You walk back out to the trail path.\n", 1.5)
        # Weapon is added to the items list.
        items.append("weapon")
        mountain(monster, weapon, items)

# Define function for Morrowind location. Player will experience the Elven
# tribe and have to make a choice to either trade or return to Evermore.
def Morrowind(monster, weapon, items):
    print_pause("You approach the Forest of Morrowind and find a local "
                "tribe of Elves.", 1.5)
    print_pause("The Elves do not allow you access to the forest, however "
                "are open to trading supplies and goods.", 1.5)
    print_pause("Would you like discuss trade with the Elven tribe or "
                "return to Evermore?\n", .5)
    # Ask the player if they would like to trade or return to Evermore.
    # validate the input with valid_input.
    forest_choice = valid_input("Enter 1 to trade.\nEnter 2 for"
                                " Evermore.\n", ["1", "2"])
    # if player selects 1, trade function is called, if 2 then exploration
    # function is called.
    if forest_choice == "1":
        trade(monster, weapon, items)
    elif forest_choice == "2":
        print_pause("You return to Evermore.\n", 1)
        exploration(monster, weapon, items)

# Define trade function.
def trade(monster, weapon, items):
    print_pause("There are several goods for sale from food, weapons,"
                " carts, and ships.", 1.5)
    # If the player has visited the the river at Evermore. "river" is in items.
    if "river" in items:
        # Player will commence trade with the Elven tribe, however if they have
        # already traded with the Elven tribe and recieved the longboat,
        # then they will return to Evermore. "longboat" is in items.
        if "longboat" in items:
            print_pause("You purchase an Apple Pie from the Elves.", 1.5)
            print_pause("There's nothing else you need from here.", 1.5)
            print_pause("You return to Evermore.\n", 1)
            exploration(monster, weapon, items)
        # Otherwise, player will successfully trade with the Elven tribe
        # and receive the longboat prior to returning to Evermore.
        else:
            print_pause(f"You purchase the Elves' strongest longboat with"
                        " a bulky hull.", 1.5)
            print_pause("You return to Evermore with the boat in tow.\n", 1)
            # longboat is added to the items list.
            items.append("longboat")
            exploration(monster, weapon, items)
    # otherwise, the player will not purchase the longboat and return to
    # Evermore.
    else:
        print_pause("You enjoy the Elves' fresh pastries and purchase a"
                    " dozen chocolate croissants.", 1.5)
        print_pause("You return to Evermore.\n", 1)
        exploration(monster, weapon, items)

# Define function Tebath location. The player will experience multiple scenarios
# based on if they have visited the Dockmaster and contain "river"
# and "longboat" in their items.
def Tebath(monster, weapon, items):
    # If player has seen the Dockmaster and received the item, "river" then
    # they will be asked if they also have a longboat.
    if "river" in items:
        print_pause("The Dockmaster asks if you've aquired a vessel to "
                    "sail along the river.", 1.5)
        # If the player has the longboat in their items, then they can commence
        # the final scenario in fighting the monster.
        if "longboat" in items:
            print_pause("Luckily you have purchased the Elven longboat.", 1)
            # Ask the player if they would like to set sail or return to
            # Evermore, validate the input with valid_input.
            river_choice = valid_input("Press 1 to set sail.\nPress 2 to"
                                       " return to the City.\n", ["1", "2"])
            # If 1 then travel_river function is called and if 2 then
            # exploration function is called.
            if river_choice == "1":
                travel_river(monster, weapon, items)
            elif river_choice == "2":
                print_pause("You leave the Docks.\n", 1)
                exploration(monster, weapon, items)
        # Otherwise, if "longboat" is not in items then player returns to
        # the City.
        else:
            print_pause("You have not aquired a vessel, you return to "
                        "the City.\n", 1)
            exploration(monster, weapon, items)
    # Otherwise, player talks to the Dockmaster and discovers the monster
    # and a way to defeat the monster. 'river' is added to items.
    else:
        print_pause("You discuss traveling to Rivenspire from Evermore "
                    "with the Dockmaster.", 1.5)
        print_pause(f"They tell you a {monster} has taken over the river, "
                    "destroying all boats traveling towards Rivenspire.", 1.5)
        print_pause("You determine you'll need a ship with a strong hull "
                    f"to withstand the {monster}'s attacks.", 1.5)
        print_pause("You have no way to set sail right now.", 1.5)
        print_pause("The Dockmaster recalls a ship craftsmaster living with "
                    "the Elves in the Forest of Morrowind.", 1.5)
        print_pause("You may want to check out the Elven marketplace.", 1.5)
        print_pause("You leave the Docks.\n", 1)
        # river is added to the items list.
        items.append("river")
        exploration(monster, weapon, items)

# Define travel_river function, once you meet the monster, the fight function
# will commence.
def travel_river(monster, weapon, items):
    print_pause("You set sail along the Tebath River preparing for your "
                f"encounter with the {monster}.", 1.5)
    print_pause(f"The {monster} emerges from the water!", 1.5)
    print_pause(f"The {monster} attacks you!", 1.5)
    fight(monster, weapon, items)

# Define fight function.
def fight(monster, weapon, items):
    print_pause("Would you like to (1) fight or (2) run away?", .5)
    # Ask player if they would like to fight the monster or retreat.
    fight_choice = valid_input("Please enter 1 or 2.\n", ["1", "2"])
    # if yes, the player fights.
    if fight_choice == "1":
        # if player has the 'weapon' within items then they will be victorious.
        if "weapon" in items:
            print_pause(f"As the {monster} moves to attack, you unsheath "
                        "your new weapon.", 1.5)
            print_pause(f"The {weapon} of Ogoroth shines brightly in your "
                        "hand as you brace yourself for the attack.", 1.5)
            print_pause(f"But the {monster} takes one look at your shiny new "
                        "toy and runs away!", 1.5)
            print_pause(f"You have rid the Tebath River of the {monster}.",
                        1.5)
            print_pause("You safely make it to Rivenspire, hailed as a Hero!\n"
                        "You are victorious in establishing a Merchant "
                        "Guild in Rivenspire!", 1.5)
        # Otherwise, the player will be defeated.
        else:
            print_pause(f"You unleash a barrage of arrows at the {monster}, "
                        "however they do little damage.", 1.5)
            print_pause("Your longboat could only withstand so much from the "
                        "wicked beast.", 1.5)
            print_pause("The wicked beast unleashes \"HOLY FIRE!\" onto your "
                        "ship, sinking \nyou to the bottom depths of "
                        "the river.", 1.5)
            print_pause("You have been defeated!", 1)
    # if no, the player retreats to Evermore and exploration function is called.
    elif fight_choice == "2":
        print_pause("You escaped the wrath of the wicked beast.", 1.5)
        print_pause("Luckily, your longboat received minimal damage.", 1.5)
        print_pause("You return to Evermore, where would you like to go?\n", 1)
        exploration(monster, weapon, items)

# Define function to play again if player loses or wins.
def play_again():
    #  Confirm player input to play again is valid.
    start_over = valid_input("Would you like to play again? (y/n)\n",
                             ["y", "n"])
    # if player selects no, thank them for playing and exit game loop.
    if start_over == "n":
        print_pause("Thank you for playing.", 1)
        exit(0)

# Define function for playing the adventure game.
def play_adventure_game():
    # create items variable assigned to empty list of items.
    items = []
    # create monster variable with random selection of monster name.
    monster = random.choice(monster_name)
    # create weapon variable with random selection of weapon name.
    weapon = random.choice(weapon_name)
    # commence game with intro message and call exploration function.
    intro()
    exploration(monster, weapon, items)

# Define function for the adventure game loop.
def adventure_game():
    # game will continue to run until false, or loop is broken.
    while True:
        # Call play_adventure_game function to start.
        play_adventure_game()
        # play again function will break loop if player chooses not to play
        # again.
        play_again()


# Start of the Adventure
if __name__ == '__main__':
    adventure_game()
