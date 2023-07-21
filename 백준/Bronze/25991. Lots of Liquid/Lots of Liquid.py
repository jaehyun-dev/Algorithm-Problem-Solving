import sys
input = sys.stdin.readline
n = int(input())
c = list(map(float, input().split()))
print(sum(list(map(lambda x: x ** 3, c))) ** (1/3))