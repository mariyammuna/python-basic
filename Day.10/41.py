# problem - 2 : count unique elements in an list
a = [1,2,2,3,3,3,4,5,6]
b = []
count = 0
for i in a:
    if i not in b:
        count += 1
        b.append(i)
print(count)