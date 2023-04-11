import sys
i = 1
flag = True
for line in sys.stdin:
    if "FBI" in line:
        print(i, end=" ")
        flag = False
    i += 1
if flag:
    print("HE GOT AWAY!")