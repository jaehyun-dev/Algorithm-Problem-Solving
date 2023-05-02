g = [1, 2, 3, 3, 4, 10]
s = [1, 2, 2, 2, 3, 5, 10]
T = int(input())
for i in range(T):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = sum([i * j for i, j in zip(g, a)])
    y = sum([i * j for i, j in zip(s, b)])
    if x > y:
        print(f"Battle {i + 1}: Good triumphs over Evil")
    elif x < y:
        print(f"Battle {i + 1}: Evil eradicates all trace of Good")
    else:
        print(f"Battle {i + 1}: No victor on this battle field")