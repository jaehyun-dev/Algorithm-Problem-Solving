import collections
start = input()
end = input()
a = collections.deque()
a.append((int(start[1]) - 1, ord(start[0]) - 97, 0))
vis = [([0] * 8) for _ in range(8)]
i = 0
while a:
    r, c, n = a.popleft()
    if r == int(end[1]) - 1 and c == ord(end[0]) - 97:
        print(n)
        break
    vis[r][c] = 1
    for dr, dc in ((-2, -1), (-2, 1), (-1, 2), (1, 2), (2, -1), (2, 1), (-1, -2), (1, -2)):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < 8 and 0 <= nc < 8 and vis[nr][nc] != 1:
            a.append((nr, nc, n + 1))
    i += 1