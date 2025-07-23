# Problem no - 1 : swaping two list elements
a = [17,12,13,15,16,10]
temp = a[0]
a[0] = a[-1] # [len(a) -1]
a[-1] = temp
print(a)