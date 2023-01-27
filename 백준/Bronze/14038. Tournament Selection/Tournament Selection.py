a = 0
for _ in range(6):
    if input() == "W":
        a += 1

if a < 1:
    print(-1)
elif a < 3:
    print(3)
elif a < 5:
    print(2)
else:
    print(1)