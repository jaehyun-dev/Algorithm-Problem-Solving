while 1:
    l = list(input().split())
    if l == ['#']:
        break
    for i in l:
        print(i[::-1], end=" ")
    print()