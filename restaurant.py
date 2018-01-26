class Restaurant:
    def __init__(self, size, tables = None):
        self.size = size
        self.tables = [tables]*size
        
    def seat(self, guest):
        for i in range(len(self.tables)):
            if self.tables[i] == None:
                print("Seating guest ", guest.name, " at table ", i)
                self.tables[i] = guest
                return True
        print("No free table!")
        return False
    
    def serve(self):
            isAllNone = True
            for i in range(len(self.tables)):
                if self.tables[i] is not None:
                    isAllNone = False
                    if self.tables[i].hunger > 0:
                        print("serving guest " + self.tables[i].name)
                        self.tables[i].eat()
                        if self.tables[i].hunger == 0:
                            self.tables[i] = None
                        break
            if isAllNone:
                print("No guest to serve!")



