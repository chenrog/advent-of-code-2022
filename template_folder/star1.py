with open('test_input.txt', 'r', encoding='UTF-8') as f:
    lines = f.readlines()

    for i, line in enumerate(lines):
        line = line.strip()
        print(i, line)
