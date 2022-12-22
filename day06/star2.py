myInput = open('input.txt', 'r')

lines = myInput.readlines()

for line in lines:
  for i in range(len(line)-14):
    string = line[i:i+14]

    stringDict = {}
    uniqueString = True
    for j in range(len(string)):
      if string[j] in stringDict.keys():
        uniqueString = False
        break
      else:
        stringDict[string[j]] = 1

    if uniqueString:
      print(string)
      print(i + 14)
      break
