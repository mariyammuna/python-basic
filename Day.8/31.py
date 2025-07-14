# More about indexing
a = [12, 20, 34, "Phitron"]
# 0 1 2 3
# print(a[0])
# print(a[-3])
# print(a[-20]) # highest -4 howa possible
# print(len(a))
# a[-3] = 500 #changed in memory
# if 20 in a:
#     print("Found")
# else:
#    print("Not Found")
# print(a)
# ******travering********
# for i in a:
#    print(i)
# for i in range(-1, -len(a)-1, -1):
#    print(a[i])
# for i in range(len(a)-1, -1, -1):
#    print(a[i])
b = [[12, 13], [18, 23, "phitron"], [-1, -19]]
   #     0             1                 2
b[0][1] = 200
# b[0][2] = 300
print(b[0][1])