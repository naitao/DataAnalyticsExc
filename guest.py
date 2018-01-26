class Guest:
    def __init__(self, n, h):
        self.name = n
        self.hunger = h
    def eat(self):
        self.hunger -= 1
        if self.hunger == 0:
            print(self.name, ": I am full!")
        return self.hunger
    def __repr__(self):
        return "<guest " + self.name + "," + "hunger " + str(self.hunger) + ">"
