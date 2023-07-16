p = {"Poblano": 1500,
     "Mirasol": 6000,
     "Serrano": 15500,
     "Cayenne": 40000,
     "Thai": 75000,
     "Habanero": 125000}
t = 0
N = int(input())
for _ in range(N):
    t += p[input()]
print(t)