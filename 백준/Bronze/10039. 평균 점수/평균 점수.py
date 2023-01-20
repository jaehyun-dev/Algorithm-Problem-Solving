num = []
for _ in range(5):
    a = int(input())
    num.append(a if a >= 40 else 40)
print(sum(num) // 5)