import sys
bracket_open = ["(", "["]
bracket_close = [")", "]"]
while True:
    input = sys.stdin.readline()
    if input == ".\n":
        break
    arr = []
    flag = True
    for i in input:
        if i in bracket_open or i in bracket_close:
            if i in bracket_open:
                arr.append(i)
            else:
                if len(arr) > 0:
                    if arr[-1] == bracket_open[bracket_close.index(i)]:
                        arr.pop()
                    else:
                        flag = False
                        break
                else:
                    flag = False
                    break
    print("yes" if len(arr) == 0 and flag == True else "no")