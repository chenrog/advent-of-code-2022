myInput = open('input.txt', 'r')

lines = myInput.readlines()

class Elf(object):

  def __init__(self, minID, maxID):
    self.minID = minID
    self.maxID = maxID

  def fromElfString(elf):
    elfMin, elfMax = elf.strip().split("-")
    return Elf(int(elfMin), int(elfMax))

  def isWithin(self, elf):
    return elf.minID <= self.minID and elf.maxID >= self.maxID

  def print(self):
    print("Elf: " + str(self.minID) + "," + str(self.maxID))


overlaps = 0
for i in range(len(lines)):
  elf1, elf2 = lines[i].strip().split(",")
  elf1 = Elf.fromElfString(elf1)
  elf2 = Elf.fromElfString(elf2)

  if elf1.isWithin(elf2) or elf2.isWithin(elf1):
    overlaps += 1

print(overlaps)
