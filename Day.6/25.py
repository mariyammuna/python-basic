# problem - 2
# python program to find the factorial of a given number 

a = int(input("Enter a value:"))
factorial = 1
for i in range (1,a+1):
    factorial = factorial*i
    print(factorial)