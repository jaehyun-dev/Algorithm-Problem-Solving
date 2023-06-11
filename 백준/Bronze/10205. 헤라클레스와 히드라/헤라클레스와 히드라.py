K = int(input())
for i in range(K):
    h = int(input())
    count = h
    for j in input():
        if j == "c":
            count += 1
        elif j == "b":
            count -= 1
    print(f"Data Set {i + 1}:")
    print(count)
    print()