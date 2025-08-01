# Default Parameters and Keyword Arguments in function

def greetings(name = 'Rahim', age = "23"):
    print(f"Hello {name}. You are {age} years old")

greetings()
greetings("Korim", 30)
greetings("Rashid", 34)
greetings(age = 23, name = "Halim")