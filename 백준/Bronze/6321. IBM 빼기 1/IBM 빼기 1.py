n = int(input())
for _ in range(n):
    a = list(input())
    res = ""
    for i in a:
        res += chr(ord(i) + 1) if i != "Z" else "A"
    print(f"String #{_ + 1}")
    print(res)
    if _ != n - 1:
        print()