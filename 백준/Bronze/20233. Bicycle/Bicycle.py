a, x, b, y, T = int(input()), int(input()), int(input()), int(input()), int(input())
o1 = a + max(0, T - 30) * x * 21
o2 = b + max(0, T - 45) * y * 21
print(o1, o2)