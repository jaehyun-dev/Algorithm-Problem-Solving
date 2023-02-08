ans = 0
for i in range(1, 4):
    ans += i * int(input())
print("happy" if ans > 9 else "sad")