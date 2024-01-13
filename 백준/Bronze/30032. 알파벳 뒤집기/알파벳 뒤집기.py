a = {'d': ['q', 'b'],
     'b': ['p', 'd'],
     'q': ['d', 'p'],
     'p': ['b', 'q']
     }
N, D = map(int, input().split())
for _ in range(N):
    s = input()
    for i in s:
        print(a[i][D - 1], end="")
    print()