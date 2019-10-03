# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def getCurrentRoom(self):
        return self.current_room

    def setCurrentRoom(self, current_room):
        self.current_room = current_room

    def followPath(self, path):
        try:
            self.setCurrentRoom(self.current_room.paths[path])
            print(f'Entering location: {self.current_room.name}')
            return True
        except:
            print("There is no path in that direction. Please try again: ")
            return False

    def addItem(self, item):
        self.inventory.append(item)
