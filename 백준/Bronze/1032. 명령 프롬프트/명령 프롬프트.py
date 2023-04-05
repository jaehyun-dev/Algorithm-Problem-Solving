N = int(input())
name = list(input())
for _ in range(N - 1):
    file = list(input())
    for i in range(len(name)):
        if name[i] != file[i]:
            name[i] = "?"
print("".join(name))