import sys
m = int(sys.stdin.readline())
s = set()
for _ in range(m):
    arr = list(sys.stdin.readline().strip().split())
    a = arr[0]
    if len(arr) == 2:
        b = int(arr[1])
    if a == 'add':
        s.add(b)
    elif a == 'remove':
        if b in s:
            s.remove(b)
    elif a == 'check':
        print(1 if b in s else 0)
    elif a == 'toggle':
        s.remove(b) if b in s else s.add(b)
    elif a == 'all':
        s = set([*range(1, 21)])
    elif a == 'empty':
        s = set()