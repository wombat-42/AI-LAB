
import random

class VacuumCleanerBot:
    def __init__(self, room):
        self.room = room
        self.pos_x = 0
        self.pos_y = 0
        self.clean_count = 0

    def print_room(self):
        print("Room state:")
        for row in self.room:
            print(row)
        print()

    def clean(self):
        if self.room[self.pos_x][self.pos_y] == 1:
            print(f"Cleaning position ({self.pos_x}, {self.pos_y})")
            self.room[self.pos_x][self.pos_y] = 0
            self.clean_count += 1
        else:
            print(f"Position ({self.pos_x}, {self.pos_y}) is already clean")

    def move(self, direction):
        if direction == "up" and self.pos_x > 0:
            self.pos_x -= 1
        elif direction == "down" and self.pos_x < len(self.room) - 1:
            self.pos_x += 1
        elif direction == "left" and self.pos_y > 0:
            self.pos_y -= 1
        elif direction == "right" and self.pos_y < len(self.room[0]) - 1:
            self.pos_y += 1
        else:
            print(f"Can't move {direction}. Out of bounds.")
        print(f"Moved to ({self.pos_x}, {self.pos_y})")

    def start_cleaning(self):
        while any(1 in row for row in self.room):
            self.clean()
            self.print_room()
            direction = random.choice(["up", "down", "left", "right"])
            self.move(direction)
        print(f"Cleaning complete! Total cleaned: {self.clean_count} cells.")

def create_room(rows, cols):
    room = []
    for _ in range(rows):
        row = [random.choice([0, 1]) for _ in range(cols)]
        room.append(row)
    return room

def main():
    rows = int(input("Enter the number of rows for the room: "))
    cols = int(input("Enter the number of columns for the room: "))
    room = create_room(rows, cols)
    print("Initial room state:")
    for row in room:
        print(row)
    bot = VacuumCleanerBot(room)
    bot.start_cleaning()

if __name__ == "__main__":
    main()

Enter the number of rows for the room: 2
Enter the number of columns for the room: 2
Initial room state:
[1, 0]
[1, 0]
Cleaning position (0, 0)
Room state:
[0, 0]
[1, 0]

Moved to (1, 0)
Cleaning position (1, 0)
Room state:
[0, 0]
[0, 0]

Moved to (0, 0)
Cleaning complete! Total cleaned: 2 cells.