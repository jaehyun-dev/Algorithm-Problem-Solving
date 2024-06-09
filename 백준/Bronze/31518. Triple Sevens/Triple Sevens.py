n = int(input())
f = 1
for _ in range(3):
    if 7 not in list(map(int, input().split())):
        f = 0
        break
print(777 if f else 0)