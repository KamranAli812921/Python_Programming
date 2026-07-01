import os
print(os.getcwd())
file = open(r'02_file\file.txt','r')

for line in file:
    if 'y' in line:
        print(line,end="")
file.close()
with open(r'02_file\file.txt','r') as file:
    for line in file:
        print(line,end="")

with open(r'02_file\file.txt','r') as file:
    lines=file.readline()
    while lines:
        print(lines,end="")
        lines=file.readline()

with open(r'02_file\file.txt','r') as file:
    lines=file.readlines()
    while lines:
        print(lines,end="")
        lines=file.readline()
print(type(lines))

with open(r'02_file\file.txt','r') as file:
    lines=file.readlines()
for line in lines[::-1]:
    print(line,end="")