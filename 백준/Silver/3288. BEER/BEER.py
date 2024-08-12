class beer:
    def __init__(self):
        self.dir = 0

    def turn1(self):
        self.dir = (self.dir - 1) % 4

    def turn2(self):
        self.dir = (self.dir + 1) % 4

dir = ['U', 'L', 'D', 'R']
N = int(input())
beers = []
for r in range(1, N + 1):
    row = []
    for c in range(1, N - r + 2):
        row.append(beer())
    beers.append(row)
for i in range(N):
    row = input()
    for j in range(i + 1):
        beers[N - i - 1][j].dir = dir.index(row[j])
for i in range(N):
    for j in range(N - i):
        for _ in range(beers[i][j].dir):
            beers[i][j].turn1()
            print(i + 1, j + 1)
            if i + 1 < N:
                if 0 <= j - 1:
                    beers[i + 1][j - 1].turn2()
                if j < N - i - 1:
                    beers[i + 1][j].turn2()