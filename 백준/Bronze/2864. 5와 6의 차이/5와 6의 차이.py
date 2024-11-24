A, B = input().split()
AM = Am = BM = Bm = ""
for i in A:
    if i in ('5', '6'):
        AM += '6'
        Am += '5'
    else:
        AM += i
        Am += i
for i in B:
    if i in ('5', '6'):
        BM += '6'
        Bm += '5'
    else:
        BM += i
        Bm += i
print(int(Am) + int(Bm), int(AM) + int(BM))