import sys
N = int(sys.stdin.readline())
A = sys.stdin.read()
s = 0
num = ""
for c in A:
    if c == " ":
        if num:
            s += int(num)
            num = ""
    else:
        num += c
s += int(num)
print(s - (N * (N - 1) // 2))