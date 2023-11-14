import sys, collections
input = sys.stdin.readline

def rotate(i, dir):
    vis[i] = True
    left_num = gears[i][6]
    right_num = gears[i][2]
    if dir == 1:
        gears[i].appendleft(gears[i].pop())
    else:
        gears[i].append(gears[i].popleft())
    if 0 < i and not vis[i - 1] and left_num != gears[i - 1][2]:
        rotate(i - 1, -dir)
    if i < 3 and not vis[i + 1] and right_num != gears[i + 1][6]:
        rotate(i + 1, -dir)

gears = []
for _ in range(4):
    gears.append(collections.deque(map(int, input().strip())))
K = int(input())
for _ in range(K):
    vis = [False] * 4
    i, dir = map(int, input().split())
    rotate(i - 1, dir)
score = 0
for i in range(4):
    score += gears[i][0] * (2 ** i)
print(score)