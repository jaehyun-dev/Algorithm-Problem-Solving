import sys
input = sys.stdin.readline
n = int(input())
while 1:
    a = int(input())
    if a == 0:
        break
    print(f"{a} is ", end="")
    if a % n != 0:
        print("NOT ", end="")
    print(f"a multiple of {n}.")