class Monkey(object):
  def __init__(self):
    self.items = []
    self.operation = ()
    self.testFactor = -1
    self.testTrueMonkey = -1
    self.testFalseMonkey = -1
    self.inspectCount = 0

  def addItem(self, item):
    self.items.append(item)

  def getFirstItem(self):
    return self.items.pop(0)

  def __str__(self) -> str:
    return "inspections:" + str(self.inspectCount) + " | Items:" + ",".join(str(item) for item in self.items)


class Item(object):
  def __init__(self, startingValue):
    self.startingValue = startingValue
    self.remaindersByFactor = {}

  def test(self, factor):
    # for factor, remainder in self.remaindersByFactor.items():
    #   if remainder % factor == 0:
    #     self.remaindersByFactor[factor] = 0

    # return self.remaindersByFactor == 0

    if self.remaindersByFactor[factor] % factor == 0:
      self.remaindersByFactor[factor] = 0
      return True
    return False

  def addFactor(self, factor):
    self.remaindersByFactor[factor] = self.startingValue

  def addValue(self, value):
    for factor, remainder in self.remaindersByFactor.items():
      self.remaindersByFactor[factor] = remainder + value

  def multiplyValue(self, value):
    for factor, remainder in self.remaindersByFactor.items():
      self.remaindersByFactor[factor] = remainder * value

  def squareValue(self):
    for factor, remainder in self.remaindersByFactor.items():
      self.remaindersByFactor[factor] = remainder * remainder

  def __str__(self) -> str:
    remaindersByFactor = []
    for factor, remainder in self.remaindersByFactor.items():
      remaindersByFactor.append(str(factor) + ":" + str(remainder))
    # return "startingValue:" + str(self.startingValue) + " | " + "remaindersByFactor: " + ", ".join(remaindersByFactor)
    return "startingValue:" + str(self.startingValue)


# PARSING FUNCTIONS
def getStartingItemsFrom(line):
  line = line.strip().strip("Starting items: ").split(", ")
  line = list(map(int, line))
  items = []
  for startingValue in line:
    items.append(Item(startingValue))
  return items

def getOperationFrom(line):
  line = line.strip().replace("Operation: new = ", "").split(" ")
  def operation(x):
    def operationPredicate(y=0):
      if line[2] == "old":
        x.squareValue()
        # y = x
        return x
      else:
        y = int(line[2])
      if line[1] == "+":
        x.addValue(y)
        # return x + y
        return x
      if line[1] == "*":
        x.multiplyValue(y)
        # return x * y
        return x
    return operationPredicate
  return operation

def getTestFrom(line):
  divisibleValue = int(line.strip().replace("Test: divisible by ", ""))
  return divisibleValue

def getTestTrueMonkey(line):
  monkey = int(line.strip().replace("If true: throw to monkey ", ""))
  return monkey

def getTestFalseMonkey(line):
  monkey = int(line.strip().replace("If false: throw to monkey ", ""))
  return monkey


# SETUP
monkeys = []
items = []
factors = []
with open('test_input.txt', 'r') as f:
  lines = f.readlines()

  monkeyCount = (len(lines) + 1) // 7
  for m in range(monkeyCount):
    startingLine = m * 7
    monkey = Monkey()
    startingItems = getStartingItemsFrom(lines[startingLine+1])
    monkey.items += startingItems
    items += startingItems
    monkey.operation = getOperationFrom(lines[startingLine+2])
    testFactor = getTestFrom(lines[startingLine+3])
    monkey.testFactor = testFactor
    factors.append(testFactor)
    monkey.testTrueMonkey = getTestTrueMonkey(lines[startingLine+4])
    monkey.testFalseMonkey = getTestFalseMonkey(lines[startingLine+5])
    monkeys.append(monkey)
    # print(monkey)

  for i in items:
    for f in factors:
      i.addFactor(f)


# ROUNDS
rounds = 1000
for round in range(rounds):
  for monkey in monkeys:
    while len(monkey.items) > 0:
      monkey.inspectCount += 1
      item = monkey.getFirstItem()
      item = monkey.operation(item)()
      if item.test(monkey.testFactor):
        monkeys[monkey.testTrueMonkey].addItem(item)
      else:
        monkeys[monkey.testFalseMonkey].addItem(item)


# OUTPUTS
for m in range(len(monkeys)):
  print("Monkey:" + str(m), "|", monkeys[m])

highestInspections = [0, 0]
for monkey in monkeys:
  if monkey.inspectCount > highestInspections[0]:
    highestInspections = [monkey.inspectCount, highestInspections[0]]

print("Monkey Business: ", highestInspections[0] * highestInspections[1])
