class Forest:
  def __init__(self):
    self.rows = []
    self.visibleTrees = {}
    self.rowCount = 0
    self.colCount = 0

  def addRow(self, row):
    self.rows.append(row)
    self.rowCount += 1
    if self.colCount == 0:
      self.colCount = len(self.rows[0])

  def checkVisibleTrees(self):
    self.__checkTreesLeftToRight()
    self.__checkTreesRightToLeft()
    self.__checkTreesTopToBottom()
    self.__checkTreesBottomToTop()

  def __checkTreesLeftToRight(self):
    for i in range(self.rowCount):
      minVisibleHeight = -1
      for j in range(self.colCount):
        treeHeight = self.rows[i][j]
        # print("req:"+str(minVisibleHeight), "tree:"+str(treeHeight))
        if treeHeight > minVisibleHeight:
          minVisibleHeight = treeHeight
          treeHash = str(i) + "," + str(j)
          self.visibleTrees[treeHash] = 0

  def __checkTreesRightToLeft(self):
    for i in range(self.rowCount):
      minVisibleHeight = -1
      for j in reversed(range(self.colCount)):
        treeHeight = self.rows[i][j]
        # print("req:"+str(minVisibleHeight), "tree:"+str(treeHeight))
        if treeHeight > minVisibleHeight:
          minVisibleHeight = treeHeight
          treeHash = str(i) + "," + str(j)
          self.visibleTrees[treeHash] = 0

  def __checkTreesTopToBottom(self):
    for j in range(self.colCount):
      minVisibleHeight = -1
      for i in range(self.rowCount):
        treeHeight = self.rows[i][j]
        # print("req:"+str(minVisibleHeight), "tree:"+str(treeHeight))
        if treeHeight > minVisibleHeight:
          minVisibleHeight = treeHeight
          treeHash = str(i) + "," + str(j)
          self.visibleTrees[treeHash] = 0

  def __checkTreesBottomToTop(self):
    for j in range(self.colCount):
      minVisibleHeight = -1
      for i in reversed(range(self.rowCount)):
        treeHeight = self.rows[i][j]
        # print("req:"+str(minVisibleHeight), "tree:"+str(treeHeight))
        if treeHeight > minVisibleHeight:
          minVisibleHeight = treeHeight
          treeHash = str(i) + "," + str(j)
          self.visibleTrees[treeHash] = 0

  def __str__(self):
    return "\n".join(str(i) for i in self.rows)

  def printVisibleTrees(self):
    rows = []
    for i in range(self.rowCount):
      row = []
      for j in range(self.colCount):
        treeHash = str(i) + "," + str(j)
        if treeHash in self.visibleTrees.keys():
          row.append(1)
        else:
          row.append(0)
      rows.append(row)
    print("\n".join(str(x) for x in rows))


with open('input.txt', 'r') as f:
  lines = f.readlines()

  forest = Forest()
  for line in lines:
    forest.addRow(list(map(int, line.strip())))

  forest.checkVisibleTrees()

  print(len(forest.visibleTrees.keys()))
  # print()
  # forest.printVisibleTrees()
  # print()
  # print(forest)
