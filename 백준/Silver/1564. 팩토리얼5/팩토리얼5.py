N = int(input())
a = 1
total2 = 0
total5 = 0
for i in range(1, N + 1):
    cnt2 = 0
    cnt5 = 0
    while i % 2 == 0:
        i //= 2
        cnt2 += 1
    while i % 5 == 0:
        i //= 5
        cnt5 += 1
    a *= i
    a = int(str(a)[-5:])
    total2 += cnt2
    total5 += cnt5
if total2 < total5:
    a *= 5 ** (total5 - total2)
elif total5 < total2:
    a *= 2 ** (total2 - total5)
print(str(a)[-5:].zfill(5))