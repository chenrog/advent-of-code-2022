

class CPU(object):
  def __init__(self):
    self.x = 1
    self.cycle = 0
    self.cyclesPerRow = 40
    self.rows = []
    self.totalSignalStrength = 0

  def incrementCycleAndCheck(self):
    row = self.cycle // self.cyclesPerRow
    isFirstPixelInRow = self.cycle % self.cyclesPerRow == 0
    if isFirstPixelInRow:
      self.rows.append([])
    if self.currentPixelIsRendered():
      self.rows[row].append("#")
    else:
      self.rows[row].append(".")
    self.cycle += 1

  def currentPixelIsRendered(self):
    pixelsRange = [self.x - 1, self.x, self.x + 1]
    return self.cycle % self.cyclesPerRow in pixelsRange

  def increaseX(self, val):
    self.x += val

  def __str__(self):
    rows = []
    for row in self.rows:
      rows.append("".join(str(i) for i in row))
    return "\n".join(str(i) for i in rows)


cpu = CPU()
with open('input.txt', 'r') as f:
  lines = f.readlines()

  for line in lines:
    line = line.strip()

    if line == "noop":
      cpu.incrementCycleAndCheck()
    else:
      val = line.split(" ")[1]
      cpu.incrementCycleAndCheck()
      cpu.incrementCycleAndCheck()
      cpu.increaseX(int(val))

print(cpu)
