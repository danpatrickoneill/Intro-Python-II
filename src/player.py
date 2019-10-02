# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, location):
        self.location = location

    def getLocation(self):
        return self.location

    def setLocation(self, location):
        self.location = location

    def followPath(self, path):
        try:
            self.setLocation(self.location.paths[path])
            print(f'Entering location: {self.location.name}')
            return True
        except:
            print("There is no path in that direction. Please try again: ")
            return False
