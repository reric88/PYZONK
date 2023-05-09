# room_description = {
#     '1': 'You are surrounded by trees on all sides. Birds and squirrels are flitting about in the treetops, chirping and chittering without a care in the world. The leaves rustle in the wind and you get a strong whiff of pine needles, damp leaves and dirt. There is a clear path to the north and you can make out a building in the distance. There is also an overgrown path to the east, leading deeper into the forest.',
    
#     '2': 'You see a large shack ahead; the door is slightly ajar and you can hear some slow shuffling and scraping on wood coming from inside. Could it be someone who can help you, or could it be your assailant? As you ponder this, a dark silhouette passes across the gap between the door and the doorframe. A dense line of trees are to the east and to the west. There is a path to the south leading deeper into the forest and a path to the north leading into the shack.',

#     '3': 'The canopy blocks most of the light here and you can barely see past the wall of brush and brambles around you. The forest floor is covered in a thick layer of leaves and sticks; the overgrowth is suffocating. You can barely make out a narrow track of dirt on the ground leading west, as well as to the north and to the south. There is a hollowed out tree to the east. There seems to be a small white box lying on the ground there.',

#     '4': 'You can see some sunlight coming through the tops of the trees. There is a brook nearby and the light is glinting off the water with a quiet brilliance. You wouldn`t really mind staying here forever and you consider the option. After a few moments you snap out of your thoughts and rub your eyes. This place is bewitching and must hold some dark magic as it would be insane to stop here considering you can see what appears to be a bears den to the west. However, you are very thirsty... There is a path to the south through a dense wall of brambles and a path leading north alongside the brook. There is a impassable cliff wall to the east.',

#     '5': 'There is a hill to the south which is much to steep to climb. The gentle sound of nature here soothes you and the forest seems to be getting thinner. A refreshing breeze blows across your face and through your disheveled hair. A brook winds down the hill in a zig-zag, babbling over a bed of stones and pebbles before entering spring. There are a few fish darting about beneath the surface of the spring, that water is clear enough you can see to the bottom. There is an impassable cliff wall to the east and a steep drop to the north. A well-worn path leads from the spring to the west.',

#     '6': 'The trees sparsely line the side of the path, their trunks and limbs creating a natural archway. The forest floor is carpeted with a thin layer of fallen leaves and twigs, and shafts of sunlight filter through the branches overhead. The powerful aroma of pine needles and damp earth fills the air around you. There is a clear path leading west and through the archway you can see a manor in the distance. The path extends into the east, leading deeper into the forest. The edge of a cliff lies to the north and a thicket of trees to the south.',

#     '7': 'The manor is very old and falling apart. Boards hang from the walls at different angles, barely holding on by nails that are nearly rusted away. The rafters and purlins above the porch are bowed down as if a giant were resting on the roof. The balusters have nearly fallen away and the handrail is supported by the few remaining. There is a door to the south leading into the manor, and an open doorway on the porch to the west also leading inside. There is a path with few pieces of gravel embedded in the dirt leading to the east into a forest.',

#     '8': 'The foyer is littered with broken items and covered in a thick later of dust. Taking a closer look at the items laying about the floor, you can see what appears to be a rapier sticking halfway out of the floorboards. It would be useful to have a weapon, but you aren`t sure if it would be wise to retrieve it not knowing who the owner is, or why it is stuck into the floor. There is an open doorway to the north and a staircase to the south.',

#     '9': 'No description yet.',

#     '10': 'No description yet.',

#     '11': 'No description yet.',

#     '12': 'No description yet.',

#     '13': 'No description yet.',

#     '14': 'No description yet.',

#     '15': 'No description yet.',

#     '16': 'No description yet.',

#     '17': 'No description yet.',
# }

# room_enter = {

# }

# items = {
#     'cookie': 'a chocolate-chip cookie.',
#     'rock': 'a very smooth stone.',
#     'gum': 'some cinnamon flavored gum',
#     'toothbrush': 'a used toothbrush',
# }

# room_description = {
#     '1': 'A Big Room',
#     '2': 'A Small Room',
#     '3': 'A Medium Room'
# }

# current_room = 0

# def look(room_num):
#     '''Prints a detailed description of your current room'''
#     room = room_description[f'{room_num}']
#     print(room)

# def walk(room_num):
#     '''Prints general description of the room you enter'''
#     room = room_enter[f'{room_num}']
#     print(room)

# def look(look_item):
#     '''Prints description of what the player specifies, if available'''
#     see = 'You see '
#     look_item = input()
#     if look_item == 'room':
#         print(room_number[f'{current_room}'])
#     elif current_room == 0 and look_item == 'cookie':
#         print(see, items[f'{look_item}'])


# print('Please enter something')
# user_input = input()

# while current_room == 0:
#     look(user_input)

items = {
    'cookie': 'a chocolate-chip cookie.',
    'rock': 'a very smooth stone.',
    'gum': 'some cinnamon flavored gum',
    'toothbrush': 'a used toothbrush',
}

room_description = {
    '1': 'A Big Room. There is a cookie on the floor.',
    '2': 'A Small Room. There is a rock in the corner and some gum on the bed.',
    '3': 'A Medium Room. There is a toothbrush on the desk.'
}

room_enter = {
    '1': 'You enter a big room with high ceilings and lots of space.',
    '2': 'You enter a small room with a single window and a small bed.',
    '3': 'You enter a medium-sized room with a large desk and bookshelves.'
}

current_room = '1'

def describe_room(room_num):
    '''Prints a detailed description of your current room'''
    room = room_description[room_num]
    print(room)

def enter_room(room_num):
    '''Prints general description of the room you enter'''
    room = room_enter[room_num]
    print(room)

def look_item(item_name):
    '''Prints description of what the player specifies, if available'''
    see = 'You see '
    if item_name == 'room':
        describe_room(current_room)
    elif current_room == '1' and item_name == 'cookie':
        print(see + items[item_name])
    elif current_room == '2' and item_name == 'rock':
        print(see + items[item_name])
    elif current_room == '2' and item_name == 'gum':
        print(see + items[item_name])
    elif current_room == '3' and item_name == 'toothbrush':
        print(see + items[item_name])


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