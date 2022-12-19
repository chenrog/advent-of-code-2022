from functools import reduce

myInput = open('input.txt', 'r')

lines = myInput.readlines()


class Directory(object):
  def __init__(self, path):
    self.path = path
    self.files = {}
    self.nestedDirPaths = []

  def addNestedDirPath(self, dirName):
    self.nestedDirPaths.append(self.path + dirName)

  def addFile(self, file):
    self.files[file.name] = file

  def size(self):
    nestedDirectoriesSize = 0
    for path in self.nestedDirPaths:
      nestedDirectoriesSize += directoriesByPath[path].size()
    return reduce(lambda x, y: x + y.size, self.files.values(), 0) + nestedDirectoriesSize

  def __str__(self):
    return "Directory: " + self.path + " has " + str(int(len(self.nestedDirPaths))) + " nested directories and " + str(int(len(self.files))) + " files, size: " + str(self.size())


class File(object):
  def __init__(self, name, size):
    self.name = name
    self.size = int(size)


def currentPathAsString():
  return "".join(currentPath)

def getCurrentDirectory():
  return directoriesByPath[currentPathAsString()]


currentPath = []
directoriesByPath = {}
for line in lines:
  line = line.strip()
  line = line.split(" ")
  # handle movement commands, we ignore LS as the subsequent information is what we care about
  if line[0] == "$" and line[1] == "cd":
    if line[2] == "/":
      currentPath = ["/"]
    elif line[2] == "..":
      currentPath.pop()
    else:
      currentPath.append(line[2])
    if currentPathAsString() not in directoriesByPath.keys():
      directoriesByPath[currentPathAsString()] = Directory(currentPathAsString())
    continue
  # handle adding a nested directory, could have a dupe name so we only care at this level
  if line[0] == "dir":
    directory = getCurrentDirectory()
    directory.addNestedDirPath(line[1])
    directoriesByPath[currentPathAsString()] = directory
    continue
  # add file to directory, could have a dupe name so we only care at this level
  if line[0].isnumeric():
    fileName, fileSize = line[1], line[0]
    getCurrentDirectory().addFile(File(fileName, fileSize))
    continue


answer = 0
for directory in directoriesByPath.values():
  if directory.size() < 100000:
    answer += directory.size()
print("answer: ", answer)


# print("Directories:", directoriesByPath.keys())
# for directoryPath in directoriesByPath.keys():
#   print(directoriesByPath[directoryPath])
