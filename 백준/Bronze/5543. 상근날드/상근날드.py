a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
burger = [a, b, c]
beverage = [d, e]
price = []
for i in burger:
    for j in beverage:
        price.append(i + j)
print(min(price) - 50)