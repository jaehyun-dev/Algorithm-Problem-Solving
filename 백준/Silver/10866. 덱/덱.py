import sys
n = int(input())
arr = []
for _ in range(n):
    command = list(sys.stdin.readline().split())
    a = command[0]
    if a == 'push_front':
        arr.insert(0, int(command[1]))
    elif a == 'push_back':
        arr.append(int(command[1]))
    elif a == 'pop_front':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop(0))
    elif a == 'pop_back':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop(-1))
    elif a == 'size':
        print(len(arr))
    elif a == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif a == 'front':
        print(-1) if len(arr) == 0 else print(arr[0])
    else:
        print(-1) if len(arr) == 0 else print(arr[-1])