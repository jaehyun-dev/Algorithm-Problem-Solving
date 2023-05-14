T = int(input())
for _ in range(T):
    a = int(input())
    print(f"Pairs for {a}: ", end="")
    ans = []
    for i in range(1, a // 2 + 1):
        if i != a - i:
            ans.append((i, a - i))
    if a > 2:
        for j in range(len(ans) - 1):
            print(f"{ans[j][0]} {ans[j][1]}, ", end="")
        print(f"{ans[-1][0]} {ans[-1][1]}")
    else:
        print()