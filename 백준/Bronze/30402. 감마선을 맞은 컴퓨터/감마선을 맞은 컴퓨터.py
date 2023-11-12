flag = False
for _ in range(15):
    for c in list(input().strip().split()):
        if c == 'w':
            print('chunbae')
        elif c == 'b':
            print('nabi')
        elif c == 'g':
            print('yeongcheol')
        else:
            continue
        flag = True
        break
    if flag:
        break