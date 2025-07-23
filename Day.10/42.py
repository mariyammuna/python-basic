# problem - 3
# Given a list, extract all elements whose frequency is greater then k
# Input : test_list = [4,6,4,3,3,4,3,3,4,3,8], K = 3
# output : [4,3]
test_list = [4, 6, 4, 3, 3, 4, 3, 3, 4, 3, 8]
K = 3
res = []
for i in test_list:
    freq = test_list.count(i)
    if freq > K and i not in res:
        res.append(i)
print(res)