import sys
import collections
for line in sys.stdin:
    if line == "#\n":
        break
    a = collections.Counter(line.lower())
    count = 0
    for i in ['a', 'e', 'i', 'o', 'u']:
        count += a[i]
    print(count)