import sys
input = sys.stdin.readline
n = int(input())
l = [0, "", "double-", "triple-"]
for _ in range(n):
    a = list(map(int, input().split()))
    count = len(list(filter(lambda x: x >= 10, a)))
    print(*a)
    print("zilch" if not count else l[count] + "double")
    print()