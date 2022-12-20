with open('test_input.txt', 'r') as f:
  lines = f.readlines()

  for line in lines:
    line = line.strip()
    print(line)
