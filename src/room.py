# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {'n': None, 'e': None, 's': None, 'w': None}
        self.items = []

    def get_name(self):
        return self.name

    def get_desc(self):
        return self.description

    def set_paths(self):
        """
        Loops over cardinal directions checking if 'direction_to' attribute has been assigned; if so, adds direction and room as key value pair in paths dictionary
        """
        for path in self.paths:
            path_to = f'{path}_to'
            if hasattr(self, path_to):
                self.paths[path] = getattr(self, path_to)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
