arr = []

def push(n):
    arr.insert(0, n)

def pop():
    if len(arr) == 0:
        print(-1)
        return
    print(arr[0])
    arr.remove(arr[0])

def size():
    print(len(arr))

def empty():
    if len(arr) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(arr) != 0:
        print(arr[0])
    else:
        print(-1)

n = int(input())
command_arr = []
for _ in range(n):
    command_arr.append(list(input().split()))

for i in command_arr:
    command = i[0]
    if command == 'push':
        push(i[1])
    elif command == 'pop':
        pop()
    elif command == 'size':
        size()
    elif command == 'empty':
        empty()
    elif command == 'top':
        top()