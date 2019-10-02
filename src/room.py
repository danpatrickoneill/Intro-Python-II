# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def getName(self):
        return self.name

    def getDesc(self):
        return self.description

    def getPaths(self):
        """
        Loops over cardinal directions checking if 'direction_to' attribute has been assigned; if so, adds direction and room as key value pair in paths dictionary
        """
        directions = ['n', 'e', 's', 'w']

        for d in directions:
            if hasattr(self, f'{d}_to'):
                self.paths[d] = getattr(self, f'{d}_to')
