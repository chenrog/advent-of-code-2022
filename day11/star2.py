from decimal import Decimal

class Monkey(object):
  def __init__(self):
    self.items = []
    self.operation = ()
    self.test = ()
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
    if self.remaindersByFactor[factor] % factor == 0:
      self.remaindersByFactor[factor] = 0

  def addFactor(self, factor):
    self.remaindersByFactor[factor] = self.startingValue

  def addValue(self, value):
    for factor, remainder in self.remaindersByFactor.items():
      self.remaindersByFactor[factor] = remainder + value

  def multiplyValue(self, value):
    for factor, remainder in self.remaindersByFactor.items():
      self.remaindersByFactor[factor] = remainder * value

  def __str__(self) -> str:
    remaindersByFactor = []
    for factor, remainder in self.remaindersByFactor.items():
      remaindersByFactor.append(str(factor) + ":" + str(remainder))
    return "startingValue:" + str(self.startingValue) + " | " + "remaindersByFactor: " + ", ".join(remaindersByFactor)



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
      if line[1] == "*":
        return x * y
    return operationPredicate
  return operation

def getTestFrom(line):
  divisibleByVal = int(line.strip().replace("Test: divisible by ", ""))
  def test(x):
    return x % divisibleByVal == 0
  return divisibleByVal, test

def getTestTrueMonkey(line):
  monkey = int(line.strip().replace("If true: throw to monkey ", ""))
  return monkey

def getTestFalseMonkey(line):
  monkey = int(line.strip().replace("If false: throw to monkey ", ""))
  return monkey


# SETUP
monkeys = []
with open('test_input.txt', 'r') as f:
  lines = f.readlines()

  monkeyCount = (len(lines) + 1) // 7
  for m in range(monkeyCount):
    startingLine = m * 7
    monkey = Monkey()
    monkey.items = getStartingItemsFrom(lines[startingLine+1])
    monkey.operation = getOperationFrom(lines[startingLine+2])
    monkey.testFactor, monkey.test = getTestFrom(lines[startingLine+3])
    monkey.testTrueMonkey = getTestTrueMonkey(lines[startingLine+4])
    monkey.testFalseMonkey = getTestFalseMonkey(lines[startingLine+5])
    monkeys.append(monkey)
    # print(monkey)


# ROUNDS
rounds = 20
for round in range(rounds):
  for monkey in monkeys:
    while len(monkey.items) > 0:
      monkey.inspectCount += 1
      item = monkey.getFirstItem()
      item = monkey.operation(item)()
      if monkey.test(item):
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
