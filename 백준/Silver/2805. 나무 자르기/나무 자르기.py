import sys
n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(tree)
while start <= end:
    index = (start + end) // 2
    count = 0
    for i in tree:
        count += max(i - index, 0)
    if count >= m:
        start = index + 1
    else:
        end = index - 1

print(end)