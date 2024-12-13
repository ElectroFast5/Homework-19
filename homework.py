homeworkFile=open("homeworkFileLol.txt")
print(homeworkFile.read())


def readSetLines(filePath,n):
  file1=open(filePath)
  count=""
  for i in range(n):
    file1=open(filePath)
    count+=file1.readlines()[i]
  print(count)

readSetLines("homeworkFileLol.txt",int(input('How many lines?: ')))


def readSetLines(filePath,n):
  file1=open(filePath)
  count=""
  for i in range(-1,-n-1,-1):
    file1=open(filePath)
    count+=file1.readlines()[i]
  print(count)

readSetLines("homeworkFileLol.txt",int(input('How many lines?: ')))


lines=open(input("Enter the file directory: ")).readlines()


count=""
for i in range(7):
  file1=open("homeworkFileLol.txt")
  count+="\n"+file1.readlines()[i][:11]
print(count)