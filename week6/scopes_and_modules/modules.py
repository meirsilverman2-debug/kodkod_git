import mathutils # option_1
from mathutils import cube, square
from tools import add
from datetime import datetime as dt
import math
import geometry
# Modules_Excrcise:

# execise_5:

# option_1
print(mathutils.square(5))
print(mathutils.cube(3))

# option_2
print(square(5))
print(cube(3))

# exercise_6:

print(add(2, 3)) # it is a seccess!!! it dosn't print those test in tools.

# exercise_7:

print(dt.today())
print(dt.now())

# exercise_8:

def public_names(math):
    lst = [name for name in math if "_" not in name]

    return sorted(lst)

# result = public_names(dir(math))
# print(result)

# exercise_9:

# from this:
def add_item(item, bag=[]):
    bag.append(item)
    return bag

result = add_item(1)
result = add_item(1)
print(result)

# to this:
def add_item_v2(item, bag= None):
    if bag == None:
        bag = []
    
    bag.append(item)
    return bag

result2 = add_item_v2(1)
result2 = add_item_v2(1)

print(result2)

# exercise_10:

ac = geometry.c(5)
ar = geometry.r(2, 5)

print(ac)
print(ar)






