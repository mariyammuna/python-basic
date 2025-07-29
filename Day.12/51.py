# Palindrome String Checking

# input : "madam"
# output : "yes"

a = input("Enter string : ")
if a == a[::-1]:
    print("Yes")
else:
    print("No")