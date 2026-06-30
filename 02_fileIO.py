file = open('02_fileIO.txt','r')
for line in file:
    print(line,end="")
file.close()