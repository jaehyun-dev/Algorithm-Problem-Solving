N = int(input())
for _ in range(N):
    s = input().split()
    for i in s[2:]:
        print(i, end=" ")
    print(s[0] + " " + s[1])