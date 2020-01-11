import shutil
import textwrap

from room import Room
from player import Player
from item import Item

# Formatting functions

view_width, view_height = shutil.get_terminal_size()


def line_break():
    print('\n')


def center_text(text):
    return text.center(view_width)

def show_room(player):
    print(center_text(player.current_room.get_name()))
    for line in textwrap.wrap(player.current_room.get_desc(), 40):
        print(center_text(line))
    line_break()

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
room['treasure'].add_item(item['coin'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
hero = Player("Hero", room['outside'])

# Set player characters initial inventory
hero.add_item(item['torch'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

previous_room = None

while True:
    # Print current location and description

    if hero.current_room != previous_room:
        show_room(hero)

    previous_room = hero.current_room

    # Sets available paths for current location
    hero.current_room.set_paths()

    # Request user input for direction to command
    user_input = input("Please choose your next move: ").lower()
    # Split command string for later length checks and set user action
    commands = user_input.split(" ")
    action = commands[0]

    # Set available cardinal directions
    directions = ['n', 'e', 's', 'w']

    if len(commands) == 1:
        # If the user enters a cardinal direction, attempt to command to the room there.
        if action in directions:
            hero.follow_path(action)

        # If the user enters "i", show player inventory.
        elif action == 'i' or action == "inventory":
            hero.check_inventory()

        # If the user enters "q", quit the game.
        elif action == 'q':
            print("Thanks for playing!")
            break

        # Print an error message if the movement isn't allowed.
        else:
            print('Invalid direction. Try again.')

    # Conditional dealing with compound inputs
    elif len(commands) == 2:
        target = commands[1]

        if action == "get" or action == "take":
            try:
                hero.take_item(item[target])
            except:
                print('Invalid command. Try again.')

        if action == "drop":
            try:
                hero.drop_item(item[target])
            except:
                print('Invalid command. Try again.')
                
    line_break()
