def time_diff(time1, time2):
    def to_seconds(t):
        h, m, s = map(int, t.split(":"))
        return h * 3600 + m * 60 + s

    def to_hhmmss(seconds):
        h = seconds // 3600
        m = (seconds % 3600) // 60
        s = seconds % 60
        return f"{h:02}:{m:02}:{s:02}"

    sec1 = to_seconds(time1)
    sec2 = to_seconds(time2)
    diff = (sec2 - sec1) % (24 * 3600)

    return to_hhmmss(diff)

time1 = input()
time2 = input()
print(time_diff(time1, time2))