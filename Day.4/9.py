a = int(input())
b = int(input())
c = int(input())

# if a>= b:
#    if a >= c:
#       print(a, "is the largest")
#    else:
#        print(c, "is the largest")
# else: # b hocche boro a er theke
#    if b >= c:
#        print(b, "is the largest")
#    else:
#        print(c, "is the largest")
if a>= b and a >= c:
    print(a, "is the largest")
elif b>=a and b>= c:
    print (b, "is the largest")
else:
    print(c, "is the largest")    