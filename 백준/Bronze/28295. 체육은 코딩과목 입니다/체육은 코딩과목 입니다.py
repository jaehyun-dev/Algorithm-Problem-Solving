a = 0
b = ["N", "E", "S", "W"]
for _ in range(10):
    a += int(input())
print(b[a % 4])