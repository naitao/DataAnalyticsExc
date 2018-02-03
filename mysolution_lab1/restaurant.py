class Restaurant:
    def __init__(self, s):
        self.tables = [None] * s

    def seat(self, guest):
        is_available_table = not all (self.tables)
        if is_available_table:
            index = next(i for i, table in enumerate(self.tables) if table is None)
            self.tables[index] = guest
            print("Seating guest " + guest.name + " at table " + str(index))
            return True
        if not is_available_table:
            print("No free table!")

    def serve(self):
        is_available_guest = any(self.tables)
        while is_available_guest:
           index = next(i for i, table in enumerate(self.tables) if table is not None)
           if self.tables[index].hunger > 0:
               print("Serving guest " + self.tables[index].name)
               self.tables[index].hunger -= 1
               if self.tables[index].hunger == 0:
                   self.tables[index] = None
               break
        if not is_available_guest:
            print("No guest to serve")
