# String reversing
# Input : "I love coding using Python"
# Output : I evol gnidoc gnisu nohtyP
a = input("")
a = a.split(" ")
print(a)
result = ""
for i in a:
    print(result)
    result += i[::-1] +" "
print(result)