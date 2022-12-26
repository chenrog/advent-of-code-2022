import heapq
import itertools
import math

elevations = {
    "a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11,
    "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21,
    "v": 22, "w": 23, "x": 24, "y": 25, "z": 26, "S": 1, "E": 26
}


class Node:
    def __init__(self, x, y, elevation, start=False, end=False):
        self.coordinates = (x, y)
        self.elevation = elevation
        self.start = start
        self.end = end

    def __lt__(self, other):
        return False

    def __str__(self) -> str:
        start = "*" if self.start else ""
        end = "*" if self.end else ""
        return str(f'{self.elevation:>02d}') + start + end + str(self.coordinates)


def path_length(came_from, current):
    path_length = 0
    while current in came_from.keys():
        current = came_from[current]
        path_length += 1
    return path_length


def distance(node, target_node):
    a = abs(node.coordinates[0] - target_node.coordinates[0])
    b = abs(node.coordinates[1] - target_node.coordinates[1])
    return math.sqrt(a ** 2 + b ** 2)


class Graph:
    nodes = {}
    start_node: Node = None
    end_node: Node = None
    row_count: int = None
    col_count: int = None

    def add_node(self, node):
        self.nodes[node.coordinates] = node

    def astar(self, start_node):
        g_score = {start_node: 0}
        h_score = {start_node: distance(start_node, self.end_node)}
        queue = [(h_score[start_node], start_node)]
        came_from = {}

        heapq.heapify(queue)
        while queue:
            _, current = heapq.heappop(queue)
            if current == self.end_node:
                return path_length(came_from, current)

            for neighbor in self.get_node_neighbors(current):
                if neighbor not in g_score.keys():
                    g_score[neighbor] = 9999
                if g_score[current] + 1 < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = g_score[current] + 1
                    h_score[neighbor] = g_score[neighbor] + distance(neighbor, self.end_node)
                    if neighbor not in queue:
                        heapq.heappush(queue, (h_score[neighbor], neighbor))

        return 9999

    def get_node_neighbors(self, node):
        neighbors = []

        x, y = node.coordinates
        if x > 0:
            neighbor = self.nodes[(x - 1, y)]
            if neighbor.elevation <= node.elevation + 1:
                neighbors.append(neighbor)
        if x < self.col_count - 1:
            neighbor = self.nodes[(x + 1, y)]
            if neighbor.elevation <= node.elevation + 1:
                neighbors.append(neighbor)
        if y > 0:
            neighbor = self.nodes[(x, y - 1)]
            if neighbor.elevation <= node.elevation + 1:
                neighbors.append(neighbor)
        if y < self.row_count - 1:
            neighbor = self.nodes[(x, y + 1)]
            if neighbor.elevation <= node.elevation + 1:
                neighbors.append(neighbor)

        return neighbors

    def __str__(self):
        string = ""
        for y in range(self.row_count):
            for x in range(self.col_count):
                string += str(self.nodes[(x, y)])
                string += "|"
            string += "\n"
        return string


# Read in elevation
nodeRows = []
with open('input.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

    for i, line in enumerate(lines):
        line = line.strip()

        nodeRows.append([])
        for c in line:
            nodeRows[i].append(c)

# Change elevation to nodes
graph = Graph()
starts = []
for y, row in enumerate(nodeRows):
    for x, elevation in enumerate(row):
        START = (elevation == "S" or elevation == "a")
        END = elevation == "E"
        node = Node(x, y, elevations[elevation], START, END)

        if START:
            graph.start_node = node
            starts.append(node)
        if END:
            graph.end_node = node

        graph.add_node(node)

graph.row_count = len(nodeRows)
graph.col_count = len(nodeRows[0])

min = 9999
for start in starts:
    # print(start)
    dist = graph.astar(start)
    if dist < min:
        min = dist

print(min)
