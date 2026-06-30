file = open('02_fileIO.txt','r')
for line in file:
    if 'y' in line:
        print(line,end="")
file.close()