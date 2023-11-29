n, c = map(int, input().split())
all = 0
bedroom = 0
cost = 0
for _ in range(n):
    a, t = input().split()
    all += int(a)
    if t == "bedroom":
        bedroom += int(a)
    if t != "balcony":
        cost += int(a)
    else:
        cost += int(a) / 2
print(all)
print(bedroom)
print(cost * c)