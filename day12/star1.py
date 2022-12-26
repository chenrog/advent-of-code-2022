import heapq

elevations = {
  "a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,
  "o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26, "S":0, "E":27
  }

class Node(object):
  def __init__(self, x, y, elevation, start=False, end=False):
    self.coordinates = (x, y)
    self.elevation = elevation
    self.start = start
    self.end = end

  def __str__(self) -> str:
    start = "*" if self.start else ""
    end = "*" if self.end else ""
    return str(self.elevation) + start + end


class Graph(object):
  nodes = {}
  startNode = None
  endNode = None
  rowCount = None
  colCount = None

  def addNode(self, node):
    self.nodes[node.coordinates] = node

  def astar(self):
    return __astar(startNode, endNode, neighbors, heuristic)

  def __astar(self, startNode, endNode, neighbors, heuristic):
    queue = [(heuristic(startNode), startNode)]
    visited = set()

    while queue:
      _, current = heapq.heappop(queue)
      if current == goal:
        return path(current)
      visited.add(current)
      for s in successors(current):
        if s not in visited:
          heapq.heappush(queue, (heuristic(s), s))

  def heuristic():

  def __str__(self):
    return "|".join(str(node) for _, node in self.nodes.items())


# Read in elevation
nodeRows = []
with open('test_input.txt', 'r') as f:
  lines = f.readlines()

  for i, line in enumerate(lines):
    line = line.strip()

    nodeRows.append([])
    for c in line:
      nodeRows[i].append(elevations[c])

# for row in nodeRows:
#   print(row)


# Change elevation to nodes
startNode = None
endNode = None
graph = Graph()
for row in range(len(nodeRows)):
  for col in range(len(nodeRows[row])):
    elevation = nodeRows[row][col]

    if elevation == 0:
      start = True
      elevation = 1
    else:
      start = False

    if elevation == 27:
      end = True
      elevation = 26
    else:
      end = False

    node = Node(col, row, elevation, start, end)
    graph.addNode(node)

    if start:
      graph.startNode = node
    if end:
      graph.endNode = node

graph.rowCount = len(nodeRows)
graph.colCount = len(nodeRows[0])
print(graph.bfs())
