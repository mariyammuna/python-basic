# Simple Problem String Sorting
# Input : x3b4U5i2
# Output : bbbbiiUUUUUxxx
a = input()
res = ""
for i in range(0, len(a), 2):
    # res = res + a[i]
    print(f"{a[i]} {a[i+1]}")
    res = res + a[i]*int()