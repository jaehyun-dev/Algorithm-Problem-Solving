while 1:
    a = input()
    if a == "END":
        break
    print("".join(list(a)[::-1]))