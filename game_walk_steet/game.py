class Place:
    """class to create a place"""

    def __init__(self, name):
        """
        Description

        """
        self.name = name
        self.description = None
        self.linked_places, self.linked_place_name = [], []
        self.link_place_directions, self.character, self.item = [], None, None

    def __str__(self):
        pass

    def set_description(self, description):
        self.description = description
        return self.description

    def link_place(self, room, direction):
        """set the directions of linked places and create a list of linked places
                to move among them"""
        self.linked_places.append(room)
        self.link_place_directions.append(direction)
        self.linked_place_name.append(room.name)

    def set_character(self, character):
        self.character = character

    def set_item(self, item):
        self.item = item

    def get_details(self):
        print(self.name)
        print('--------------------')
        print(self.description)
        for i in range(len(self.linked_places)):
            print("The {} is {}".format(self.linked_places[i].name, self.link_place_directions[i]))

    def get_character(self):
        return self.character

    def get_item(self):
        return self.item

    def move(self, command):
        """Move in input direction to other place"""
        for i in range(len(self.link_place_directions)):
            if command == self.link_place_directions[i]:
                return self.linked_places[i]


class Walker:
    """class to create a walker"""

    def __init__(self, name, description):
        """
        Description

        """
        self.name = name
        self.character_description = description
        self.phrase, self.weakness = None, None

    def __str__(self):
        pass

    def set_conversation(self, phrase):
        self.phrase = phrase

    def set_weakness(self, weakness):
        self.weakness = weakness

    def describe(self):
        print(self.name + ' is here!')
        print(self.character_description)

    def talk(self):
        print('[{} says]: '.format(self.name) + self.phrase)

    def fight(self, fight_with):
        """Fight with enemy with fight_with
            If fight_thing is its weakness - you WIN
            else - you LOSE"""
        if fight_with == self.weakness:
            print("You fend {} off with the {}".format(self.name, self.weakness))
            return True

        print("{} crushes you, puny adventurer!".format(self.name))
        return False


class Item:
    """class to create a item"""

    def __init__(self, name,):
        """
        Description

        """
        self.name = name
        self.item_description = None

    def __str__(self):
        pass

    def set_description(self, description):
        self.item_description = description

    def describe(self):
        if self.item_description is not None:
            print('The [{}] is here - '.format(self.name) + self.item_description)

    def get_name(self):
        return self.name
