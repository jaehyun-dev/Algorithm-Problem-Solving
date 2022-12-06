a, b = map(int, input().split())
M_0, m_0 = max(a, b), min(a, b)
M, m = M_0, m_0
while True:
    share = M // m
    remainder = M % m
    if remainder == 0:
        break
    M = m
    m = remainder

print(m)
if m == 1:
    print(M_0 * m_0)
elif M_0 % m_0 == 0:
    print(M_0)
else:
    print(int(M_0 * m_0 / m))

# eluis80776님의 답    
# m, n = map(int, (input().split()))
# o = m * n
# while n != 0:
#     t = m % n
#     m, n = n, t
# print(m, o // m, sep = '\n')
