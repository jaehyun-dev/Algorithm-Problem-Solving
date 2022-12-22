a, b, c = map(int, input().split())
def check(num):
    if num == 1:
        return a % c
    else:
        left = check(num // 2)
        if num % 2 == 0:
            return (left ** 2) % c
        else:
            return (left ** 2 * a) % c
print(check(b))