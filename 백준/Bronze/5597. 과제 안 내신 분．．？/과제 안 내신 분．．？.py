arr = [*range(1, 31)]
for _ in range(28):
    arr.remove(int(input()))
print(arr[0])
print(arr[1])