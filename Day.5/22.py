# Pattern Printing 2-
# ascii value

# a
# b b
# c c c
# d d d d
# e e e e e
# f f f f f f
# g g g g g g g

for row in range(7):
    for col in range(row+1):
        print(chr(65+row), end= " ")    #65 ata boro hater jonno 
    print()