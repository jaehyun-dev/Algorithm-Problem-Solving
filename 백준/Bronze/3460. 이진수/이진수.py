T = int(input())
for _ in range(T):
    n = bin(int(input()))[2:]
    ans = []
    for i in range(len(n)):
        if n[i] == '1':
            ans.append(len(n) - i - 1)
    print(*ans[::-1])