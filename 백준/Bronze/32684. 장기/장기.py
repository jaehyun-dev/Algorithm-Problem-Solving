s = [13, 7, 5, 3, 3, 2]
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = sum(x * y for x, y in zip(s, a))
d = sum(x * y for x, y in zip(s, b)) + 1.5
print("cocjr0208" if d < c else "ekwoo")