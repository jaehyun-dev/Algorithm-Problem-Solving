k = int(input())
c = 25 + k * 0.01
if c < 100:
    print("100.00")
elif c > 2000:
    print("2000.00")
else:
    print(format(c, ".2f"))