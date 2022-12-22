class Forest:
  def __init__(self):
    self.rows = []
    self.rowCount = 0
    self.colCount = 0

  def addRow(self, row):
    self.rows.append(row)
    self.rowCount += 1
    if self.colCount == 0:
      self.colCount = len(self.rows[0])

  def checkScenicScore(self, row, col):
    return self.__checkTreesLeftOf(row, col) * self.__checkTreesRightOf(row, col) * self.__checkTreesTopOf(row, col) * self.__checkTreesBottomOf(row, col)

  def __checkTreesLeftOf(self, row, col):
    currentTreeHeight = self.rows[row][col]
    treesVisible = 0
    for j in reversed(range(col)):
      treeHeight = self.rows[row][j]
      treesVisible += 1
      if treeHeight >= currentTreeHeight:
        break
    # print(treesVisible)
    return treesVisible

  def __checkTreesRightOf(self, row, col):
    currentTreeHeight = self.rows[row][col]
    treesVisible = 0
    for j in range(col+1, self.colCount):
      treeHeight = self.rows[row][j]
      treesVisible += 1
      if treeHeight >= currentTreeHeight:
        break
    # print(treesVisible)
    return treesVisible

  def __checkTreesTopOf(self, row, col):
    currentTreeHeight = self.rows[row][col]
    treesVisible = 0
    for i in reversed(range(row)):
      treeHeight = self.rows[i][col]
      treesVisible += 1
      if treeHeight >= currentTreeHeight:
        break
    # print(treesVisible)
    return treesVisible

  def __checkTreesBottomOf(self, row, col):
    currentTreeHeight = self.rows[row][col]
    treesVisible = 0
    for i in range(row+1, self.rowCount):
      treeHeight = self.rows[i][col]
      treesVisible += 1
      if treeHeight >= currentTreeHeight:
        break
    # print(treesVisible)
    return treesVisible

  def __str__(self):
    return "\n".join(str(i) for i in self.rows)


with open('input.txt', 'r') as f:
  lines = f.readlines()

  forest = Forest()
  for line in lines:
    forest.addRow(list(map(int, line.strip())))

  greatestScenicScore = 0
  for i in range(forest.rowCount):
    for j in range(forest.colCount):
      scenicScore = forest.checkScenicScore(i, j)
      if scenicScore > greatestScenicScore:
        greatestScenicScore = scenicScore
  print(greatestScenicScore)

  # print(forest.checkScenicScore(3,3))
  # print(forest)
