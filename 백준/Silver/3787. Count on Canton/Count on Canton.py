import sys
for line in sys.stdin:
    N = int(line.strip())
    i = 0
    s = 0
    while s < N:
        i += 1
        s += i
    m = N - s + i
    if i % 2:
        print(f"TERM {N} IS {i - m + 1}/{m}")
    else:
        print(f"TERM {N} IS {m}/{i - m + 1}")