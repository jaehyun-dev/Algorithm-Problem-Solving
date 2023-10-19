import sys
input = sys.stdin.readline

class dice():
    r = 0
    c = 0

    top = 0
    bottom = 0
    north = 0
    south = 0
    east = 0
    west = 0

    def __init__(self, r, c):
        self.r = r
        self.c = c

    def move(self, dir):
        dr = [1, 0, 0, -1]
        dc = [0, 1, -1, 0]
        self.r += dr[dir % 4]
        self.c += dc[dir % 4]

    def number(self):
        if graph[self.r][self.c] == 0:
            graph[self.r][self.c] = self.bottom
        else:
            self.bottom = graph[self.r][self.c]
            graph[self.r][self.c] = 0

    def roll(self, dir):
        temp = [self.top, self.east, self.west, self.north, self.south, self.bottom]
        self.bottom = temp[dir]
        if dir == 1:
            self.east = temp[0]
            self.top = temp[2]
            self.west = temp[5]
        elif dir == 2:
            self.east = temp[5]
            self.top = temp[1]
            self.west = temp[0]
        elif dir == 3:
            self.top = temp[4]
            self.north = temp[0]
            self.south = temp[5]
        elif dir == 4:
            self.top = temp[3]
            self.north = temp[5]
            self.south = temp[0]
        dice.move(dir)
        dice.number()

def check(r, c, dir):
    dr = [1, 0, 0, -1]
    dc = [0, 1, -1, 0]
    nr = r + dr[dir % 4]
    nc = c + dc[dir % 4]
    if 0 <= nr < N and 0 <= nc < M:
        return True
    return False

N, M, x, y, K = map(int, input().split())
dice = dice(x, y)
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
k = list(map(int, input().split()))
for d in k:
    if check(dice.r, dice.c, d):
        dice.roll(d)
        print(dice.top)