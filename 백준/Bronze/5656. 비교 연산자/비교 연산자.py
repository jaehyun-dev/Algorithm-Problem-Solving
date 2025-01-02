import sys
i = 1
for line in sys.stdin:
    a, o, b = line.strip().split()
    a = int(a)
    b = int(b)
    res = "false"
    if o == "E":
        break
    if o == ">":
        if a > b:
            res = "true"
    elif o == ">=":
        if a >= b:
            res = "true"
    elif o == "<":
        if a < b:
            res = "true"
    elif o == "<=":
        if a <= b:
            res = "true"
    elif o == "==":
        if a == b:
            res = "true"
    elif o == "!=":
        if a != b:
            res = "true"
    print(f"Case {i}: {res}")
    i += 1