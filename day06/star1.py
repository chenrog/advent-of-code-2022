myInput = open('input.txt', 'r')

lines = myInput.readlines()

for line in lines:
    for i in range(len(line) - 4):
        string = line[i:i + 4]

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
            print(i + 4)
            break
