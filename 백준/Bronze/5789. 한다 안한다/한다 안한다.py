N = int(input())
for _ in range(N):
    a = input()
    print("Do-it", end="")
    print("" if a[len(a) // 2 - 1] == a[len(a) // 2] else "-Not")