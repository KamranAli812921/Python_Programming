import os
print(os.getcwd())
# file = open(r'02_file\file.txt','r')

# for line in file:
#     if 'y' in line:
#         print(line,end="")
# file.close()
with open(r'02_file\file.txt','r') as file:
    for line in file:
        print(line,end="")