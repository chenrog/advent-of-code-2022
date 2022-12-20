class Monkey(object):
  def __init__(self):
    self.items = []
    self.operation = ()
    self.test = ()
    self.testTrueMonkey = -1
    self.testFalseMonkey = -1
    self.inspectCount = 0

  def addItems(self, items):
    self.items += items

  def addItem(self, item):
    self.items.append(item)

  def setOperation(self, operation):
    self.operation = operation

  def setTest(self, test):
    self.test = test

  def setTestTrueMonkey(self, monkeyIdx):
    self.testTrueMonkey = monkeyIdx

  def setTestFalseMonkey(self, monkeyIdx):
    self.testFalseMonkey = monkeyIdx

  def getFirstItem(self):
    return self.items.pop(0)

  def hasItems(self):
    return len(self.items) > 0

  def incrementInspectCount(self):
    self.inspectCount += 1

  def __str__(self) -> str:
    return "Items:" + ",".join(str(item) for item in self.items) + " | true:" + str(self.testTrueMonkey) + " | false:" + str(self.testFalseMonkey) + " | inspections:" + str(self.inspectCount)


def getStartingItemsFrom(line):
  line = line.strip().strip("Starting items: ").split(", ")
  return list(map(int, line))

def getOperationFrom(line):
  line = line.strip().replace("Operation: new = ", "").split(" ")
  def operation(x):
    def operationPredicate(y=0):
      if line[2] == "old":
        y = x
      else:
        y = int(line[2])
      if line[1] == "+":
        return x + y
      if line[1] == "-":
        return x - y
      if line[1] == "/":
        return x / y
      if line[1] == "*":
        return x * y
    return operationPredicate
  return operation

def getTestFrom(line):
  divisibleByVal = int(line.strip().replace("Test: divisible by ", ""))
  def test(x):
    return x % divisibleByVal == 0
  return test

def getTestTrueMonkey(line):
  monkey = int(line.strip().replace("If true: throw to monkey ", ""))
  return monkey

def getTestFalseMonkey(line):
  monkey = int(line.strip().replace("If false: throw to monkey ", ""))
  return monkey

monkeys = []
with open('input.txt', 'r') as f:
  lines = f.readlines()

  monkeyCount = (len(lines) + 1) // 7
  for m in range(monkeyCount):
    startingLine = m * 7
    monkey = Monkey()
    monkey.addItems(getStartingItemsFrom(lines[startingLine+1]))
    monkey.setOperation(getOperationFrom(lines[startingLine+2]))
    monkey.setTest(getTestFrom(lines[startingLine+3]))
    monkey.setTestTrueMonkey(getTestTrueMonkey(lines[startingLine+4]))
    monkey.setTestFalseMonkey(getTestFalseMonkey(lines[startingLine+5]))
    monkeys.append(monkey)
    # print(monkey)


for round in range(20):
  for monkey in monkeys:
    while monkey.hasItems():
      monkey.incrementInspectCount()
      item = monkey.getFirstItem()
      item = monkey.operation(item)()
      item = item // 3
      if monkey.test(item):
        monkeys[monkey.testTrueMonkey].addItem(item)
      else:
        monkeys[monkey.testFalseMonkey].addItem(item)

highestInspections = [0, 0]
for monkey in monkeys:
  if monkey.inspectCount > highestInspections[0]:
    highestInspections = [monkey.inspectCount, highestInspections[0]]
  print(monkey)

print("Monkey Business: ", highestInspections[0] * highestInspections[1])
