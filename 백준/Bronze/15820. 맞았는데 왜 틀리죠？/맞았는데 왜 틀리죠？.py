import sys
input = sys.stdin.readline
s1, s2 = map(int, input().split())
tflag = True
sflag = True
for _ in range(s1):
    a = list(map(int, input().split()))
    if a[0] != a[1]:
        tflag = False
for _ in range(s2):
    a = list(map(int, input().split()))
    if a[0] != a[1]:
        sflag =False
if tflag:
    if sflag:
        print("Accepted")
    else:
        print("Why Wrong!!!")
else:
    print("Wrong Answer")