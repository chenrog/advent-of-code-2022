# elves are the index, they have bags of food worth x calories where x is the value
elves = []

elvesInput = open('input.txt', 'r')

lines = elvesInput.readlines()

bag = 0
for line in lines:
    if line == '\n':
        elves.append(bag)
        bag = 0
    else:
        bag += int(line)

elves.append(bag)

print(elves)

largestBags = [0, 0, 0]
for i in range(len(elves)):
    if elves[i] > largestBags[0]:
        largestBags = [elves[i], largestBags[1], largestBags[2]]
        largestBags.sort()

print(sum(largestBags))
