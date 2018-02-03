from guest import Guest
from restaurant import Restaurant

g1 = Guest('Alice', 1)
g2 = Guest('John', 2)
g3 = Guest('Mary', 3)

guests = [g1, g2, g3]

r = Restaurant(2)

while guests:
    print(r.tables)
    if r.seat(guests[-1]):
        guests.pop()
    r.serve()

print(r)
