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
        if hasattr(self, 'n_to'):
            self.paths['n'] = self.n_to

        if hasattr(self, 'e_to'):
            self.paths['e'] = self.e_to

        if hasattr(self, 's_to'):
            self.paths['s'] = self.s_to

        if hasattr(self, 'w_to'):
            self.paths['w'] = self.w_to
