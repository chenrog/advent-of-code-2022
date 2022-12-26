myInput = open('input.txt', 'r')

lines = myInput.readlines()


class Stack(object):

    def __init__(self):
        self.crates = []

    def append(self, crate):
        self.crates.append(crate)

    def prepend(self, crate):
        self.crates.insert(0, crate)

    def pop(self):
        return self.crates.pop()

    def print(self):
        print(self.crates)


def cleanInstruction(instruction):
    instruction = instruction.strip()
    instruction = instruction.replace("move", "")
    instruction = instruction.replace("from", "")
    instruction = instruction.replace("to", "")
    instruction = instruction.split(" ")
    for i in reversed(range(len(instruction))):
        if instruction[i] == "":
            instruction.pop(i)
        else:
            instruction[i] = int(instruction[i])
    return instruction


stacks = []
stacksNeeded = int(len(lines[0]) / 4)
for i in range(stacksNeeded):
    stacks.append(Stack())

instructionLineStart = 0
# stacks
for i in range(len(lines)):
    # check if we're at the end of the stack setup
    lineStripped = lines[i].strip()
    if lineStripped == "":
        instructionLineStart = i + 1
        break

    # set up stacks
    for j in range(stacksNeeded):
        leftIdx = j * 4
        rightIdx = leftIdx + 3

        crate = lines[i][leftIdx:rightIdx]
        crate = crate.strip("[ ]")
        # if this is the last line before instructions
        if crate.isdigit():
            break

        if crate != "":
            stacks[j].prepend(crate)

for i in range(len(stacks)):
    stacks[i].print()

print()

# instructions
for i in range(instructionLineStart, len(lines)):
    instruction = cleanInstruction(lines[i])
    amountToMove = instruction[0]
    # decrement from and to stacks by 1 so they are 0 index
    fromStack = instruction[1] - 1
    toStack = instruction[2] - 1

    for j in range(amountToMove):
        crate = stacks[fromStack].pop()
        stacks[toStack].append(crate)

for i in range(len(stacks)):
    stacks[i].print()

print()

finalString = ""
for i in range(len(stacks)):
    finalString += stacks[i].pop()

print(finalString)
