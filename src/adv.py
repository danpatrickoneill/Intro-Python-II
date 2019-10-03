import shutil
import textwrap

from room import Room
from player import Player
from item import Item

# Formatting functions


def lineBreak():
    print('\n')


def centerText(text):
    width, height = shutil.get_terminal_size()
    return text.center(width)

# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Declare all the items
item = {
    "torch":  Item("torch", "No more than a candle really, but good enough to get around by"),
    "coin": Item("coin", "A filthy old coin")
}

# Add a bit of treasure to the treasure room
room['treasure'].addItem(item['coin'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
hero = Player("Hero", room['outside'])

# Set player characters initial inventory
hero.addItem(item['torch'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

while True:
    # Print current location and description
    print(centerText(hero.current_room.getName()))
    for line in textwrap.wrap(hero.current_room.getDesc(), 40):
        print(centerText(line))
    lineBreak()

    # Request user input for direction to command
    userInput = input("Please choose your next move: ").lower()
    # Split command string for later length checks and set user action
    commands = userInput.split(" ")
    action = commands[0]

    # Set available cardinal directions
    directions = ['n', 'e', 's', 'w']

    # Sets available paths for current location
    hero.current_room.setPaths()

    if len(commands) == 1:
        # If the user enters a cardinal direction, attempt to command to the room there.
        if action in directions:
            print(action)
            hero.followPath(action)

        # If the user enters "i", show player inventory.
        elif action == 'i' or action == "inventory":
            hero.checkInventory()

        # If the user enters "q", quit the game.
        elif action == 'q':
            print("Thanks for playing!")
            break

        # Print an error message if the movement isn't allowed.
        else:
            print('Invalid direction. Please try again: ')

    # Conditional dealing with compound inputs
    elif len(commands) == 2:
        target = commands[1]

        if action == "get" or action == "take":
            try:
                hero.takeItem(item[target])
            except:
                print('Invalid command. Please try again: ')

        if action == "drop":
            try:
                hero.dropItem(item[target])
            except:
                print('Invalid command. Please try again: ')
    lineBreak()
