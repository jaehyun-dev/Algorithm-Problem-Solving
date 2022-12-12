t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))
    index = m
    count = 0
    while len(queue) > 0:
        if index == 0:
            if queue[index] == max(queue):
                queue.pop(0)
                print(count + 1)
                break
            else:
                queue.append(queue.pop(0))
                index = len(queue) - 1
        else:
            if queue[0] == max(queue):
                queue.pop(0)
                count += 1
            else:
                queue.append(queue.pop(0))
            index -= 1