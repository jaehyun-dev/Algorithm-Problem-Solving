s = input()
i = j = I = J = 0
while i < len(s) or j < len(s):
    i = s.find("IOI", i)
    j = s.find("JOI", j)
    if 0 <= i:
        I += 1
        i += 1
    if 0 <= j:
        J += 1
        j += 1
    if i == -1 and j == -1:
        break
print(J)
print(I)