n = int(input())
d = set()
ans = 0
for i in range(1, n + 1):
    if i in d:
        break
    else:
        if n % i == 0:
            if i != n // i:
                ans += i + n //i
            else:
                ans += i
        d.add(i)
        d.add(n // i)
print(ans * 5 - 24)