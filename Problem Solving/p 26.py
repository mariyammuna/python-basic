num = int(input("How many numbers ?"))
lst = []

for n in range(num):
    numbers = int(input("Enter a number: "))
    lst.append(numbers)
    
print("sum of them :", sum(lst))