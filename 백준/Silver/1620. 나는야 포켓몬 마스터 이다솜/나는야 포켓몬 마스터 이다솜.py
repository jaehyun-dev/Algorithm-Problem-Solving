import sys
n, m = map(int, sys.stdin.readline().strip().split())
dic_name = {}
dic_num = {}
for i in range(n):
    a = sys.stdin.readline().strip()
    dic_name[a] = str(i + 1)
    dic_num[str(i + 1)] = a
for _ in range(m):
    b = sys.stdin.readline().strip()
    if b in dic_name:
        print(dic_name[b])
    else:
        print(dic_num[b])