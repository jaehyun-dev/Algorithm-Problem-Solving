w = b = 0
for _ in range(8):
    l = input()
    c = l.count
    w += c('P') + c('N') * 3 + c('B') * 3 + c('R') * 5 + c('Q') * 9
    b += c('p') + c('n') * 3 + c('b') * 3 + c('r') * 5 + c('q') * 9
print(w - b)