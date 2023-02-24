colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a')
# data.writelines(colors)
# data.writelines('\n')
# data.close()

# data  = open('file.txt', 'a')
# data.writelines(colors)
# data.write('line3\n')
# data.write('line4\n')
# data.close()

# with open('file.txt','r+') as data:
#     data.write('line3\n')
#     data.write('line4\n')
import re

with open("file.txt", "r") as file:
    lines = file.readlines()
    print(lines)
    # substring = "lines"
    # m = int(lines.find(substring))
    # del lines[m]

with open("file.txt", "w") as file:
    file.writelines(lines)
    # print(m, lines)
