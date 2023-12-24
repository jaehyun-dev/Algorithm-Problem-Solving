a = ["Double eagle", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey"]
i = 1
while 1:
    p, s = map(int, input().split())
    if p == 0:
        break
    print(f"Hole #{i}")
    if s == 1:
        print("Hole-in-one", end="")
    else:
        print(a[min(s - p + 3, 5)], end="")
    print(".\n")
    i += 1