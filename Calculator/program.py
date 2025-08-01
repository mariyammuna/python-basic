# mini calculator 10 + 20 = 30
first = input("Enter 1st Number")
operator = input("Enter A operator (+,-,*,%) : ")
second = input("Enter 2nd Number : ")

first=int(first)
second=int(second)

if operator=="+":
    print(first+second)
elif operator=="-":
    print(first-second)
elif operator=="*":
    print(first*second)
elif operator=="%":
    print(first%second)
else:
    print("Operator Invalided")