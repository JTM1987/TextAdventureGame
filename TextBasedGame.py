""" Simple text based game which allows a player to move between rooms and collect 6
items in order to defeat a "Boss". Player must navigate all six rooms in the enemy
base and gather the six items in their corresponding rooms before encountering
the boss, else the player loses the game."""


# Introduction to the game
def Intro():
    print('Welcome to the infiltrate and assassinate game.')
    print('You must carefully navigate through all of the rooms and gather six items:')
    print('A handgun, jacket, pants, headgear, gloves and boots.')
    print('If you encounter the Enemy Captain before collecting the items,'
          ' you will raise suspicion and be defeated!')
    print('_' * 64)


# Function for retrieving items from rooms
def retrieve_item(location, command, rooms, inventory):
    inventory.append(rooms[location]['Item'])
    del rooms[location]['Item']


# Function for movement between rooms
def player_move(location, command, rooms):
    location = rooms[location][command]
    return location


str = ''
# List variable for holding the required items in the players inventory
inventory = []
# Players starting location
location = 'Breezeway'
Intro()
# Defining valid directions
directions = ['North', 'South', 'East', 'West']


def main():
    rooms = {
        # A dictionary which contains the basic layout of the game(Rooms and their corresponding items)
        'Breezeway': {'East': 'Conference Room', 'Quit': 'Exit'},
        'Conference Room': {'North': 'Upper Barracks', 'East': 'Captain\'s Office', 'South': 'Lower Barracks',
                            'West': 'Breezeway', 'Quit': 'Exit', 'Item': 'Handgun'},
        'Captain\'s Office': {'North': 'Captain\'s Quarters', 'Quit': 'Exit', 'Item': 'Gloves'},
        'Captain\'s Quarters': {''},
        'Upper Barracks': {'East': 'Upper Latrine and Showers', 'South': 'Conference Room', 'Quit': 'Exit',
                           'Item': 'Jacket'},
        'Upper Latrine and Showers': {'West': 'Upper Barracks', 'Quit': 'Exit', 'Item': 'Pants'},
        'Lower Barracks': {'North': 'Conference Room', 'East': 'Lower Latrine and Showers', 'Quit': 'Exit',
                           'Item': 'Headgear'},
        'Lower Latrine and Showers': {'West': 'Lower Barracks', 'Quit': 'Exit', 'Item': 'Boots'}
    }
    str = ''
    # List variable for holding the required items in the players inventory
    inventory = []
    # Players starting location
    location = 'Breezeway'
    Intro()
    while True:
        # If player encounters the boss, with or without the required items
        if location in 'Captain\'s Quarters':
            # If the player wins the game
            if len(inventory) == 6:
                print('You enter the Captain\'s Quarters and remain undetected due to your disguise.')
                print('You raise your weapon and quickly dispatch the enemy captain.')
                print('You won! Thank you for playing')
                break
            # If the player loses the game
            else:
                print('You enter the Captain\'s Quarters and raise suspicion due to your strange attire.')
                print('The enemy captain quickly raises his gun and shoots you!')
                print('You\'ve been defeated! Thank you for playing.')
                break
        # Updates the players status and prompts the player for their next move
        print('You are in the {}'.format(location))
        print('You currently have', inventory)
        # Prompts the player with the item contained in each room, if that room contains an item.
        if location != 'Captain\'s Quarters' and 'Item' in rooms[location].keys():
            print('You look around, and see {}'.format(rooms[location]['Item']))
        print('_' * 64)
        command = input('What do you want to do next: ').title().split()
        # If player enters a command to move to the next room
        if len(command) >= 2 and command[1] in rooms[location].keys():
            location = player_move(location, command[1], rooms)
            continue
        # If player enters command to get an item, error handling exception for no item\already retrieved
        try:
            if len(command[0]) == 3 and command[0] == 'Get' and ' '.join(command[1:]) in rooms[location]['Item']:
                print('You pick up the {}'.format(rooms[location]['Item']))
                print('_' * 64)
                retrieve_item(location, command, rooms, inventory)
        except KeyError:
            print('Oops! Not a valid movement or command!')


main()
