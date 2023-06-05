while 1:
    M, A, B = map(int, input().split())
    if M == A == B == 0:
        break
    t = M / A - M / B
    h = int(t)
    m = int((t - h) * 60)
    s = int(round((((t - h) * 60) % 1) * 60, 0))
    print(f"{h}:{str(m).zfill(2)}:{str(s).zfill(2)}")