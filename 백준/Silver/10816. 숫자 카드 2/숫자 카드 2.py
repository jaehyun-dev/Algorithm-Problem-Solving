import sys
import collections
n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().rstrip().split()))

counter = collections.Counter(cards)

for i in range(m - 1):
    print(counter[num[i]], end=" ")
print(counter[num[-1]])