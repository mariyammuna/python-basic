# Indexing and immutability in python
a = "Hello world"
    # 012345678910
    # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
# print(a[10])
# print(a[-1])
# a[-1] = "D"
# print(a)
# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i], end = " ")
print(a[2:10:3])

