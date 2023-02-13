A, B = int(input()), int(input())
h = [*range(1, 13)]
print(h[(A + B) % 12 - 1])