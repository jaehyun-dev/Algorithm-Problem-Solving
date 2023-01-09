import sys
count = 0
for line in sys.stdin:
    if line.strip() == "":
        break
    count += 1
print(count)