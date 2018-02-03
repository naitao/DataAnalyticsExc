class Restaurant:

    def __init__(self, seatings):
        self.seatings = seatings
        self.tables = [None for _ in range(0, seatings)]

    def seat(self, guest):
        is_table_available = not all(self.tables)
        if is_table_available:
            idx = next(i for i, t in enumerate(self.tables) if t is None)
            print('Seating guest {} at table {}'.format(guest.name, idx))
            self.tables[idx] = guest
        else:
            print('No free table!')

        return is_table_available

    def serve(self):
        is_somebody_seating = any(self.tables)
        if is_somebody_seating:
            idx = next(i for i, t in enumerate(self.tables) if t is not None)
            print('Serving guest {}'.format(self.tables[idx].name))
            if not self.tables[idx].eat():
                self.tables[idx] = None
        else:
            print('No guest to serve!')
