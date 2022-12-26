import heapq
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
        self.g_score = 9999
        self.h_score = 9999

    def __lt__(self, other):
        return self.h_score < other.h_score

    def __str__(self) -> str:
        start = "*" if self.start else ""
        end = "*" if self.end else ""
        return str(f'{self.elevation:>02d}') + start + end


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

    def astar(self):
        self.start_node.g_score = 0
        self.start_node.h_score = distance(self.start_node, self.end_node)
        queue = [self.start_node]
        came_from = {}

        heapq.heapify(queue)
        while queue:
            current = heapq.heappop(queue)
            if current == self.end_node:
                return path_length(came_from, current)

            for neighbor in self.get_node_neighbors(current):
                if current.g_score + 1 < neighbor.g_score:
                    came_from[neighbor] = current
                    neighbor.g_score = current.g_score + 1
                    neighbor.h_score = neighbor.g_score + distance(neighbor, self.end_node)
                    if neighbor not in queue:
                        heapq.heappush(queue, neighbor)

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
with open('test_input.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

    for i, line in enumerate(lines):
        line = line.strip()

        nodeRows.append([])
        for c in line:
            nodeRows[i].append(c)

for row in nodeRows:
    print(row)

# Change elevation to nodes
graph = Graph()
for y, row in enumerate(nodeRows):
    for x, elevation in enumerate(row):
        START = elevation == "S"
        END = elevation == "E"
        node = Node(x, y, elevations[elevation], START, END)

        if START:
            graph.start_node = node
        if END:
            graph.end_node = node

        graph.add_node(node)

graph.row_count = len(nodeRows)
graph.col_count = len(nodeRows[0])
print(graph)
print(graph.astar())
