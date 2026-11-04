rooms = {
    'A': 'Dirty',
    'B': 'Dirty'
}

location = 'A'

while 'Dirty' in rooms.values():

    print("Vacuum cleaner is in room", location)

    if rooms[location] == 'Dirty':
        print("Room", location, "is dirty. Cleaning...")
        rooms[location] = 'Clean'

    else:
        print("Room", location, "is clean. Moving...")

    if location == 'A':
        location = 'B'
    else:
        location = 'A'

print("\nAll rooms are clean!")
print(rooms)