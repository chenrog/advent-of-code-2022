from enum import Enum

myInput = open('input.txt', 'r')

class RPS(Enum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

  def fromString(string):
    if string == "A" or string == "X":
      return RPS.ROCK
    if string == "B" or string == "Y":
      return RPS.PAPER
    if string == "C" or string == "Z":
      return RPS.SCISSORS

  def value(self):
    if self == RPS.ROCK:
      return 1
    if self == RPS.PAPER:
      return 2
    if self == RPS.SCISSORS:
      return 3

  def pointsAgainst(self, opponent):
    if self == opponent:
      return 3
    if self.beats(opponent):
      return 6
    else:
      return 0

  def beats(self, opponent):
    if self == RPS.ROCK and opponent == RPS.SCISSORS:
      return True
    if self == RPS.PAPER and opponent == RPS.ROCK:
      return True
    if self == RPS.SCISSORS and opponent == RPS.PAPER:
      return True
    return False


lines = myInput.readlines()

totalScore = 0
for line in lines:
  opponent, me = line.strip().split(" ")

  me = RPS.fromString(me)
  opponent = RPS.fromString(opponent)
  # print(me, opponent)

  score = me.value() + me.pointsAgainst(opponent)
  # print(score)

  totalScore += score

print(totalScore)
