N = int(input())
print("뭐야", end="")
flag = True
for _ in range(N):
    if input() == "anj":
        flag = False
        break
print("?" if flag else ";")