rooms = {
    '1': {
        'description': 'A Big Room.',
        'enter': 'You enter a big room with high ceilings and lots of space.',
        'items': {
            'cookie': 'a chocolate-chip cookie.',
        },
        'item_desc': {
            'cookie': 'There is a cookie on the floor.'
        },
    },
    '2': {
        'description': 'A Small Room. There is a rock in the corner and some gum on the bed.',
        'enter': 'You enter a small room with a single window and a small bed.',
        'items': {
            'rock': 'a very smooth stone.',
            'gum': 'some cinnamon flavored gum',
        },
    },
    '3': {
        'description': 'A Medium Room. There is a toothbrush on the desk.',
        'enter': 'You enter a medium-sized room with a large desk and bookshelves.',
        'items': {
            'toothbrush': 'a used toothbrush',
        },
    },
}

current_room = '1'
room = rooms[f'{current_room}']
inventory = []

def describe_room(room_num):
    '''Prints a detailed description of your current room'''
    room = rooms[f'{room_num}']
    # item_desc = rooms[f'{room_num}']['item_desc'][f'{item}']
    print(room['description'])
    for item in room['item_desc']:
        print(room['item_desc'][item])    

def enter_room(room_num):
    '''Prints general description of the room you enter'''
    room = rooms[f'{room_num}']['enter']
    print(room)

def look_item(item_name):
    '''Prints description of what the player specifies, if available'''
    see = 'You see '
    if item_name == 'room':
        describe_room(current_room)
    else:
        try:
            print(see + rooms[current_room]['items'][item_name])
        except KeyError:
            print("You don't see that here.")

def take_item(item):
    '''Takes the specified item, if possible, adds it to inventory and removes it from the room'''
    target_list = rooms[f'{current_room}']['items']
    if item in target_list:
        inventory.append(f'{item}')
        del target_list[f'{item}']
        del 

start_game = True
print('Please enter something')
user_input = input()

while start_game:
    '''Start the game'''
    if user_input == 'quit':
        quit()
    # Room 1
    while current_room == '1':
        if user_input == 'look':
            describe_room(current_room)
        elif user_input == 'walk':
            enter_room('2')
            current_room = '2'
        elif user_input.startswith('take'):
            take_item(user_input.split()[1])
        elif user_input.startswith('look '):
            look_item(user_input.split()[1])
        else:
            print('Invalid command.')
        # print('Please enter something')
        user_input = input()

    # Room 2
    while current_room == '2':
        if user_input == 'look':
            describe_room(current_room)
        elif user_input == 'walk':
            enter_room('3')
            current_room = '3'
        elif user_input.startswith('look '):
            look_item(user_input.split()[1])
        else:
            print('Invalid command.')
        # print('Please enter something')
        user_input = input()

    # Room 3
    while current_room == '3':
        if user_input == 'look':
            describe_room(current_room)
        elif user_input == 'walk':
            enter_room('1')
            current_room = '1'
        elif user_input.startswith('look '):
            look_item(user_input.split()[1])
        else:
            print('Invalid command.')
        # print('Please enter something')
        user_input = input()