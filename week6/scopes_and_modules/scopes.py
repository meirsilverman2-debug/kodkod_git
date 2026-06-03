# Scopes Exercise:

# exercise_1:

count = 0

def bump():

    global count
    count += 1

def value():
    return count

bump()
bump()
bump()

v = value()
print(v)

# exercise_2:

def make_counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        return count
    return inner
    
c = make_counter()
print(c())
print(c())
print(c())




# exercise_3:

x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()
    print(x)

outer()
print(x)

# exercise_4:

list = [1, 2, 3]
# print(list(range(5)))

"""
Because the word list is a built in function that cast somthing to a list or creat a list as a variable or list comprehension
etc. so in this line of code the moment that you assign some sort of value to list
you changed it from a built in function to a global variable so 
next line of code will lose its ability to call it function so you will receive a type error from this reason python first goes to the lower scope which is in this case the global scope which above it you have the built in scope
as we learnd it goes by LEGB so it does not reach to the built in scope it's stayed on the global scop ect....

"""
