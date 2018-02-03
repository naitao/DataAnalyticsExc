class Guest:

    def __init__(self, name, hunger):
        self.name = name
        self.hunger = hunger

    def __repr__(self):
        return '<guest {}, hunger {}>'.format(self.name, self.hunger)

    def eat(self):
        if self.hunger == 0:
            print('I am full!')
        else:
            self.hunger -= 1

        return self.hunger
