T = int(input())
for _ in range(T):
    a = float(input())
    print(f"${format(round(a * .8, 2), '.2f')}")