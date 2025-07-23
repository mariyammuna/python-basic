# problem - 4
# create the following list using list comprehension
# [[1,2,3,4], [0,2,3,4], [0,1,3,4], [0,1,2,4], [0,1,2,3]]
a = [[j for j in range(5) if i!=j] for i in range(5)]
print(a)