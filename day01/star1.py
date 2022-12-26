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

largestBag = 0
elfToAsk = 0
for i in range(len(elves)):
    if elves[i] > largestBag:
        largestBag = elves[i]
        elfToAsk = i

print(largestBag)
