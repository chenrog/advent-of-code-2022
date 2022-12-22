from enum import Enum

myInput = open('input.txt', 'r')

class RPS(Enum):
  ROCK = 1
  PAPER = 2
  SCISSORS = 3

  def fromOpponentString(opponent):
    if opponent == "A":
      return RPS.ROCK
    if opponent == "B":
      return RPS.PAPER
    if opponent == "C":
      return RPS.SCISSORS

  def fromMeString(me, opponent):
    if me == "X":
      return RPS.whatLosesTo(opponent)
    if me == "Y":
      return opponent
    if me == "Z":
      return RPS.whatBeats(opponent)

  def whatLosesTo(rps):
    if rps == RPS.ROCK:
      return RPS.SCISSORS
    if rps == RPS.PAPER:
      return RPS.ROCK
    if rps == RPS.SCISSORS:
      return RPS.PAPER

  def whatBeats(rps):
    if rps == RPS.ROCK:
      return RPS.PAPER
    if rps == RPS.PAPER:
      return RPS.SCISSORS
    if rps == RPS.SCISSORS:
      return RPS.ROCK

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

  opponent = RPS.fromOpponentString(opponent)
  me = RPS.fromMeString(me, opponent)
  # print(me, opponent)

  score = me.value() + me.pointsAgainst(opponent)
  # print(score)

  totalScore += score

print(totalScore)
