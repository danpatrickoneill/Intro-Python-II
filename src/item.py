class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name.capitalize() + "\n" + self.description

    def get_name(self):
        return self.name

    def get_desc(self):
        return self.description

    def on_take(self):
        print(f'You have taken the {self.name}')

    def on_drop(self):
        print(f'You have dropped the {self.name}')
