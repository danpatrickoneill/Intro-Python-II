# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        self.items = []

    def getName(self):
        return self.name

    def getDesc(self):
        return self.description

    def setPaths(self):
        """
        Loops over cardinal directions checking if 'direction_to' attribute has been assigned; if so, adds direction and room as key value pair in paths dictionary
        """
        if not self.paths:
            print("Setting paths!")

            directions = ['n', 'e', 's', 'w']

            for d in directions:
                # set attr string based on current direction
                d_to = f'{d}_to'
                if hasattr(self, d_to):
                    self.paths[d] = getattr(self, d_to)

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.remove(item)
