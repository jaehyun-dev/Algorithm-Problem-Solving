class bot():
    cnt = 0

    def __init__(self, r, c, d):
        self.r = r
        self.c = c
        self.d = d

    def clean(self):
        self.cnt += 1

    def rotate(self):
        self.d = (self.d - 1) % 4

    def forward(self):
        self.r += dr[self.d]
        self.c += dc[self.d]

    def backward(self):
        self.r -= dr[self.d]
        self.c -= dc[self.d]

def check(r, c):
    return 0 <= r < N and 0 <= c < M and graph[r][c] == 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
visited = [([False] * M) for _ in range(N)]
bot = bot(r, c, d)
while 1:
    if not visited[bot.r][bot.c]:
        bot.clean()
        visited[bot.r][bot.c] = True
    flag = True
    for i in range(4):
        nr = bot.r + dr[i]
        nc = bot.c + dc[i]
        if check(nr, nc) and not visited[nr][nc]:
            flag = False
    if flag:
        nr = bot.r - dr[bot.d]
        nc = bot.c - dc[bot.d]
        if check(nr, nc):
            bot.backward()
            continue
        else:
            break
    else:
        bot.rotate()
        nr = bot.r + dr[bot.d]
        nc = bot.c + dc[bot.d]
        if check(nr, nc) and not visited[nr][nc]:
            bot.forward()
            continue

print(bot.cnt)