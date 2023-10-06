def check(r, c, pos):
    for i in range(r):
        if (pos[i] == c or i - r == pos[i] - c or i - r == c - pos[i]):
            return False
    return True

def recur(r, pos):
    global ans
    if r == N:
        ans += 1
        return
    for i in range(N):
        if check(r, i, pos):
            pos[r] = i
            recur(r + 1, pos)
    return

N = int(input())
ans = 0
pos = [0] * N
recur(0, pos)
print(ans)