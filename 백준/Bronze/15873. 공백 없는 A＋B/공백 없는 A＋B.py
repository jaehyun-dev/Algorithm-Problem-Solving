a = list(input())
if len(a) == 2:
    print(int(a[0]) + int(a[1]))
elif len(a) == 3:
    if a[1] == '0':
        print(int(a[0] + a[1]) + int(a[2]))
    else:
        print(int(a[0]) + int(a[1] + a[2]))
else:
    print(int(a[0] + a[1]) + int(a[2] + a[3]))