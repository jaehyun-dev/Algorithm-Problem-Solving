a = list(map(int, input().split()))
b = ["A", "B", "C"]
if a.count(0) == 1:
    print(b[a.index(0)])
elif a.count(1) == 1:
    print(b[a.index(1)])
else:
    print("*")