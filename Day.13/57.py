# Print Vs Returu in Function

def sum(a,b):
    print(a+b)
    print("hello")
sum(2,3)

def sum_with_return(a,b):
    return a+b # stopped

result = sum_with_return(2,3)
result += 4
print(sum_with_return(2,3)*3)