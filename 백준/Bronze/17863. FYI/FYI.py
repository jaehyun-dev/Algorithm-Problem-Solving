N = input()
flag = 0
for i in range(3):
    if N[i] != '5':
        flag = 1
        break
print("YES" if flag == 0 else "NO")