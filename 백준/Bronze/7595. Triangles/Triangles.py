while 1:
    a = int(input())
    if not a:
        break
    for i in range(1, a + 1):
        print("*" * i)