file = open("KnapSack.py","r")
print(type(file))

fileContents = file.read()
#print(fileContents)

#we cant read the same file again after the read the file


print("=========")
file = open("KnapSack.py","r")
line = file.readline()
#print(line)
#readline read the file, line by line

#readlines store the lines of file in list
lines = file.readlines()
#print(lines)
#for line in lines:
 #   print(line)
print("=============")
file = open("SingleInher.py","r")
data = file.read(15)
#print(data)

file.close()
#print("Is file is closed:",file.closed)

file = open("students.xml","r")
data = file.read()
print(data)
#with this content we can read only textual files. Not image, video,etc files