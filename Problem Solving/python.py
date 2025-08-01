nums = 5
gums = int(input("Guess the number: "))

if nums>gums:
    print("Too low")   
elif gums>nums:
    print("Too high")
elif gums==nums:
    print("Correct!")