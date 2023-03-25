a = {1: 'A',
     2: 'B',
     3: 'C',
     4: 'D',
     0: 'E'
     }

for _ in range(3):
    b = list(map(int, input().split()))
    c = b.count(0)
    print(a[c])