import sys
import statistics
import collections
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))

def round_func(n):
    if n - int(n) == -0.5:
        return int(n)
    else:
        return round(n)

mean = round_func(statistics.mean(arr))
median = (sorted(arr)[n//2])

arr_counter = collections.Counter(sorted(arr)).most_common(2)
if len(arr_counter) > 1 and arr_counter[0][1] == arr_counter[1][1]:
    mode = arr_counter[1][0]
else:
    mode = arr_counter[0][0]

arr_range = max(arr) - min(arr)

print(mean)
print(median)
print(mode)
print(arr_range)