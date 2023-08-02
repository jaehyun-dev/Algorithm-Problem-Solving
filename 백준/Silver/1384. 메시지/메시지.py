g = 1
while 1:
    n = int(input())
    if n == 0:
        break
    name = []
    nasty = []
    flag = 0
    for _ in range(n):
        l = list(input().split())
        name.append(l[0])
        temp = []
        for i in range(n - 1):
            if l[1:][i] == 'N':
                flag = 1
                temp.append(i)
        nasty.append(temp)
    print(f"Group {g}")
    g += 1
    if not flag:
        print("Nobody was nasty")
    else:
        for j in range(n):
            for k in range(len(nasty[j])):
                print(f"{name[j - nasty[j][k] - 1]} was nasty about {name[j]}")
    print()