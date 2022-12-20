

class CPU(object):
  def __init__(self):
    self.x = 1
    self.cycle = 1
    self.cycleCheckpoints = [20, 60, 100, 140, 180, 220]
    self.totalSignalStrength = 0

  def incrementCycleAndCheck(self):
    if self.cycle in self.cycleCheckpoints:
      self.totalSignalStrength += (self.cycle * self.x)
    self.cycle += 1

  def increaseX(self, val):
    self.x += val


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

print(cpu.totalSignalStrength)
