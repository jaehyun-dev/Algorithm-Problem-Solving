a = {"fdsajkl;": "in-out",
     "jkl;fdsa": "in-out",
     "asdf;lkj": "out-in",
     ";lkjasdf": "out-in",
     "asdfjkl;": "stairs",
     ";lkjfdsa": "reverse"}
s = input()
print(a[s] if s in a else "molu")