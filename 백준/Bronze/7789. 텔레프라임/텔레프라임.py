def is_prime(n):
    if n < 2:
        return True
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i < n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

a, b = input().split()
b = int(b + a)
a = int(a)
print("Yes" if is_prime(a) and is_prime(b) else "No")