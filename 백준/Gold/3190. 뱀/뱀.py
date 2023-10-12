import sys, collections
input = sys.stdin.readline

def rotate(C):
    global d
    if C == 'L':
        d = (d - 1) % 4
    elif C == 'D':
        d = (d + 1) % 4

def check(r, c):
    return 0 <= r < N and 0 <= c < N and not vis[r][c]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
r = 0
c = 0
d = 1
sec = 0

q = collections.deque()
q.append([0, 0])

N = int(input())
vis = [([0] * N) for _ in range(N)]
vis[0][0] = 1
K = int(input())
apple = []
for _ in range(K):
    apple.append(list(map(int, input().split())))
L = int(input())
flag = False

for _ in range(L):
    l = input().split()
    X = int(l[0]) - sec
    C = l[1]
    i = 0
    while i < X:
        sec += 1
        r = r + dr[d]
        c = c + dc[d]
        if not check(r, c):
            flag = True
            break
        q.append([r, c])
        vis[r][c] = 1
        if [r + 1, c + 1] not in apple:
            a = q.popleft()
            vis[a[0]][a[1]] = 0
        else:
            apple.remove([r + 1, c + 1])
        i += 1
    rotate(C)
    if flag:
        break
if not flag:
    while (check(r + dr[d], c + dc[d])):
        sec += 1
        r = r + dr[d]
        c = c + dc[d]
        if not check(r, c):
            flag = True
            break
        q.append([r, c])
        vis[r][c] = 1
        if [r + 1, c + 1] not in apple:
            a = q.popleft()
            vis[a[0]][a[1]] = 0
        else:
            apple.remove([r + 1, c + 1])
print(sec if flag else sec + 1)