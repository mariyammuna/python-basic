# method 1

year = int(input())

# if year % 400 == 0:
#    print("leap year")
# elif year % 100 == 0:
#    print("not a leap year")
# elif year % 4 == 0:
#    print("leap year")
# else:
#    print("not a leap year")

# method 2
if year % 400 == 0 and year % 100 == 0:
    print("leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("leap year")
else:
    print("not a leap year")

# method 3
if (year % 400 == 0) or (year %100 != 0 and year % 4 == 0):
    print("leap year")
else:
    print("not a leap year")