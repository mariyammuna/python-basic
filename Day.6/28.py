# Problem - 5
# Python Program to Check Armstrong Number

# Method-1
# a = int(input())
# num_len = len(str(a))
# temp = a
# sum = 0
# while temp>0:
#    lst_digit = temp%10
#    sum = sum + lst_digit**num_len
#    # temp = temp // 10
#    temp //= 10
# if sum == a:
#    print("Armstrong number")
# else:
#    print("Not Armstrong")

# Method - 2

a = input()
num_len = len(a)
sum = 0

for i in a:
    sum = sum + int(i) ** num_len

if int(a) == sum:
    print("Armstrong")
else:
    print("Not Armstrong")
