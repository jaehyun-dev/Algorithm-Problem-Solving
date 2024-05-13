mbti = list(input())
d = {'E': 'I',
     'I': 'E',
     'S': 'N',
     'N': 'S',
     'T': 'F',
     'F': 'T',
     'J': 'P',
     'P': 'J'}
for i in mbti:
    print(d[i], end="")