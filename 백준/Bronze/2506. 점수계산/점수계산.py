N = int(input())
arr = list(map(int, input().split()))
i = 0
count = 1
score = 0
while i < len(arr):
    if arr[i]:
        score += count
        count += 1
    else:
        count = 1
    i += 1
print(score)