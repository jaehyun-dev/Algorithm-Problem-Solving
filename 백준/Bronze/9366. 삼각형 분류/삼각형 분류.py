T = int(input())
for i in range(T):
    a = sorted(list(map(int, input().split())))
    b = len(set(a))
    if a[0] + a[1] <= a[2]:
        type = 'invalid!'
    elif b == 3:
        type = 'scalene'
    elif b == 2:
        type = 'isosceles'
    else:
        type = 'equilateral'
    print(f"Case #{i + 1}: {type}")