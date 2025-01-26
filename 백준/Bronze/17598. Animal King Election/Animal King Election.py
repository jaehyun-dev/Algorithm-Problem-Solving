v = {"Tiger": 0, "Lion": 0}
for _ in range(9):
    v[input()] += 1
print("Lion" if v["Tiger"] < v["Lion"] else "Tiger")