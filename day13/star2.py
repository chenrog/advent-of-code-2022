def both_ints(a, b):
    return isinstance(a, int) and isinstance(b, int)


def both_nestable_lists(a, b):
    return isinstance(a, NestableList) and isinstance(b, NestableList)


class NestableList:
    def __init__(self, string):
        self.values = []
        depth = 0
        start = 0
        end = 0
        current_int = ""
        for i, char in enumerate(string):
            if char == '[':
                depth += 1
                if depth == 1:
                    start = i + 1
            elif char == ']':
                depth -= 1
                if depth == 0:
                    end = i
                    self.values.append(NestableList(string[start:end]))
            elif char != ',' and depth == 0:
                current_int += char
            else:
                if current_int:
                    self.values.append(int(current_int))
                    current_int = ""
        if current_int:
            self.values.append(int(current_int))

    def __lt__(self, other):
        count = min(len(self.values), len(other.values))
        for i in range(count):
            left = self.values[i]
            right = other.values[i]
            if both_ints(left, right) or both_nestable_lists(left, right):
                if left < right:
                    return True
                elif left > right:
                    return False
            elif isinstance(left, int) or isinstance(right, int):
                if isinstance(left, int):
                    left_as_list = NestableList(f"{left}")
                    if left_as_list != right:
                        return NestableList(f"{left}") < right
                else:
                    right_as_list = NestableList(f"{right}")
                    if right_as_list != left:
                        return left < NestableList(f"{right}")
        return len(self.values) < len(other.values)

    def __eq__(self, other):
        if len(self.values) != len(other.values):
            return False

        for i, _ in enumerate(self.values):
            left = self.values[i]
            right = other.values[i]
            if not both_ints(left, right) and not both_nestable_lists(left, right):
                return False
            elif left != right:
                return False

        return True

    def __str__(self):
        return "[" + ",".join(str(value) for value in self.values) + "]"


with open('input.txt', 'r', encoding='UTF-8') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

    packets = []
    for i in range(len(lines)):
        packet = lines[i]
        packet = packet[1:-1]

        packet = NestableList(packet)
        packets.append(packet)

    left_decoder = NestableList("[2]")
    right_decoder = NestableList("[6]")
    packets.append(left_decoder)
    packets.append(right_decoder)
    packets.sort()
    for packet in packets:
        print(packet)

    print((packets.index(left_decoder) + 1) * (packets.index(right_decoder) + 1))
