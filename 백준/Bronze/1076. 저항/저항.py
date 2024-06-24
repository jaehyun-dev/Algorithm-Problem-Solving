a = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
c1 = input()
c2 = input()
c3 = input()
ans = (a.index(c1) * 10 + a.index(c2)) * (10 ** a.index(c3))
print(ans)