input()
a = set(map(int, input().split()))
b = set(map(int, input().split()))
d = a - b
print(len(d))
print(*sorted(list(d)))