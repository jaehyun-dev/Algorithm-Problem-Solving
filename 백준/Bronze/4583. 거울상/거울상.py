d = {
    'b': 'd',
    'd': 'b',
    'p': 'q',
    'q': 'p',
    'i': 'i',
    'o': 'o',
    'v': 'v',
    'w': 'w',
    'x': 'x'
}
while 1:
    w = input()
    if w == '#':
        break
    flag = 1
    ans = ""
    for i in w:
        if i not in d:
            flag = 0
            break
        else:
            ans = d[i] + ans
    if flag:
        print(ans)
    else:
        print("INVALID")