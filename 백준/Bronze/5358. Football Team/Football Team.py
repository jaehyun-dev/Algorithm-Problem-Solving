import sys
dic = {'i': 'e',
       'e': 'i',
       'I': 'E',
       'E': 'I'}
for line in sys.stdin:
    if line == "\n":
        break
    for i in range(len(line)):
        print(dic[line[i]] if line[i] in dic else line[i], end="")