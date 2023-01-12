import sys
for line in sys.stdin:
    if line == "\n":
        break
    else:
        print(line.strip())