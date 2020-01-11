# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def get_current_room(self):
        return self.current_room

    def set_current_room(self, current_room):
        self.current_room = current_room

    def check_inventory(self):
        print("You carry with you: ")
        for item in self.inventory:
            print(item)

    def follow_path(self, path):
        next_room = self.current_room.paths[path]
        if next_room:
            self.set_current_room(next_room)
        else:
            print("There is no path in that direction. Please try again: ")

    def add_item(self, item):
        self.inventory.append(item)

    def take_item(self, item):
        if item in self.current_room.items:
            self.inventory.append(item)
            self.current_room.remove_item(item)
            item.on_take()
        else:
            print(f"I don't see any {item.name}s here")

    def drop_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.current_room.add_item(item)
            item.on_drop()
        else:
            print(f"You don't have any {item.name}s to drop!")
