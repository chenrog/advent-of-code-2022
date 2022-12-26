class RopeEnd(object):
    def __init__(self):
        self.x, self.y = 0, 0

    def move(self, command):
        if command == "L":
            self.x -= 1
        if command == "R":
            self.x += 1
        if command == "U":
            self.y += 1
        if command == "D":
            self.y -= 1

    def follow(self, other):
        if self.__sameSpot(other) or self.__withinOneCell(other):
            return
        elif self.__sameRow(other):
            self.__moveHorizontalTowards(other)
        elif self.__sameColumn(other):
            self.__moveVerticalTowards(other)
        elif not self.__sameRow(other) and not self.__sameColumn(other):
            self.__moveHorizontalTowards(other)
            self.__moveVerticalTowards(other)

    def __sameSpot(self, other):
        return self.x == other.x and self.y == other.y

    def __withinOneCell(self, other):
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    def __sameRow(self, other):
        return self.y == other.y

    def __sameColumn(self, other):
        return self.x == other.x

    def __moveHorizontalTowards(self, other):
        self.x += 1 if self.x < other.x else -1

    def __moveVerticalTowards(self, other):
        self.y += 1 if self.y < other.y else -1

    def __str__(self):
        return "x:" + str(self.x) + ",y:" + str(self.y)


def updateTailLocations(tail):
    tailHash = str(tail.x) + "," + str(tail.y)
    allTailVisitedLocations[tailHash] = 0


head = RopeEnd()
tail = RopeEnd()
allTailVisitedLocations = {}
with open('input.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        command, times = line.strip().split(" ")
        for t in range(int(times)):
            head.move(command)
            tail.follow(head)
            updateTailLocations(tail)

print("head:", head)
print("tail:", tail)
print("tailVisits:", len(allTailVisitedLocations.keys()))
