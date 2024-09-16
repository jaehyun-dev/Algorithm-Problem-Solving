K = int(input())
s = input()
r = len(s) // K
graph = [([0] * K) for _ in range(r)]
for i in range(len(s)):
    if (i // K % 2 == 0):
        graph[i // K][i % K] = s[i]
    else:
        graph[i // K][K - (i % K) - 1] = s[i]
ans = ""
for j in range(K):
    for i in range(r):
        ans += graph[i][j]
print(ans)