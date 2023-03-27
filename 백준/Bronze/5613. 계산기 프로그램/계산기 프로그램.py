import sys
input = sys.stdin.readline
answer = int(input())
i = 0
while True:
    a = input().strip()
    if a == "=":
        print(answer)
        break
    if i % 2 == 0:
        oper = a
    else:
        answer = int(eval(f"{answer} {oper} {a}"))
    i += 1