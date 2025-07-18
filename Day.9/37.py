# List comprehension : Part - 2

# [expressionb(element) for element in list condition]

# Example 4: Using if with list comprehension
# a = []
# for i in range(1, 20):
#     if i % 3 == 0:
#         a.append(i)
# print(a)
# b = [i for i in range(1,20) if i % 3 == 0]
# print(b)
# Example 5: Nested if with list comprehension
# a = []
# for i in range(1, 20):
#     if i % 3 == 0:
#          a.append(i)
#     if i % 5 == 0:
#          a.append(i)
# print(a)
# b = [i for i in range(1,20) if i % 3 == 0 or i % 5 == 0]
# print(b)
# Example 6: If...else with list comprehension
# [if else for i in list]

# a = []
# for i in range(20):
#     if i % 2 == 0:
#         a.append("Even")
#     else:
#         a.append("Odd")
# print(a)

b = ["even" if i % 2 == 0 else "odd" for i in range(20)]
print(b)