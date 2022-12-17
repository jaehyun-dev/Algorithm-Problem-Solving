import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))
set = sorted(list(set(arr)))
for i in range(len(arr)):
    start = 0
    end = len(set) - 1
    while start <= end:
        index = (start + end) // 2
        if set[index] < arr[i]:
            start = index + 1
        elif set[index] > arr[i]:
            end = index - 1
        else:
            print(index) if i == len(arr) - 1 else print(index, end=" ")
            break