def state():
    global snr
    if w <= 0:
        print(f"{snr} RIP")
    elif 1 / 2 * o < w < 2 * o:
        print(f"{snr} :-)")
    else:
        print(f"{snr} :-(")
    snr += 1

def action(a, n):
    global w
    global is_alive
    if is_alive:
        if a == 'E':
            w -= n
        else:
            w += n
    if w <= 0:
        is_alive = 0

snr = 1
is_alive = 1
while 1:
    line = input()
    if line == "0 0":
        break
    elif line == "# 0":
        state()
    else:
        a, b = line.split()
        if a in ('F', 'E'):
            action(a, int(b))
        else:
            o, w = map(int, (a, b))
            is_alive = 1