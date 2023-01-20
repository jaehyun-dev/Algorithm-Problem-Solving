a = []
for _ in range(3):
    a.append(int(input()))
if len(set(a)) == 1 and 60 in a:
    print("Equilateral")
elif sum(a) == 180:
    if len(set(a)) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")