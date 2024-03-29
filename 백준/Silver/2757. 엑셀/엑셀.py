import sys
import collections
for line in sys.stdin:
    cell = line.strip()
    if cell == "R0C0":
        break
    row = cell[1:cell.index("C")]
    c = int(cell[cell.index("C") + 1:])
    col = ""
    r = collections.deque()
    while 0 < c:
        r.appendleft((c - 1) % 26)
        c = (c - 1) // 26
    while r:
        col += chr(r.popleft() + 65)
    print(col + row)