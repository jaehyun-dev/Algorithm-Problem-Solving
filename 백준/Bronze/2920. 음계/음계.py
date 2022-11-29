arr = input().split()
if arr == sorted(arr):
    print("ascending")
elif arr == sorted(arr, reverse=True):
    print("descending")
else:
    print("mixed")