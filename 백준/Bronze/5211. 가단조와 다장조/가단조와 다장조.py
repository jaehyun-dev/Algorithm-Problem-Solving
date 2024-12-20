s = input()
M = 0
m = 0
prev = "|"
i = 0
while i < len(s):
    if prev == "|":
        if s[i] in ["A", "D", "E"]:
            m += 1
        elif s[i] in ["C", "F", "G"]:
            M += 1
    prev = s[i]
    i += 1
if M == m:
    if s[i - 1] in ["A", "D", "E"]:
        m += 1
    else:
        M += 1
if m < M:
    print("C-major")
else:
    print("A-minor")