while 1:
    w = input()
    if w == "#":
        break
    for _ in range(len(w)):
        if w[0] in ["a", "e", "i", "o", "u"]:
            break
        else:
            w = w[1:] + w[0]
    print(w + "ay")