# exercise_1:

def safe_int(s):
    try:
        return int(s)
    except Exception as e:
        print(f"The error is: {e}")
        return None
    
# safe_int("42")
# result = safe_int("42")
# result2 = safe_int("abs")
# print(result)
# print(result, result2)

# exercise_2:

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "undefined"
    
# result = safe_divide(10, 2)
# print(result)

# result2 =safe_divide(10, 0)
# print(result2)

# exercise_3:

def get_value(d, key):
    try:
        return d[key]
    except Exception as e:
        print(e)
        print(type(e))
        print(type(e).__name__)
        return "missing"
    
# result = get_value({"a": 1}, "a")
# print(result)

# result2 = get_value({"a": 1}, "b")
# print(result2)

# exercise_4:

def parse_int(values):

    numbers = []

    for value in values:
        try:
            numbers.append(int(value))
        except ValueError, TypeError:
            continue
    return numbers

# result = parse_int(["1", "2", "x", "3", "y"])
# print(result)

# exercise_5:

def set_age(age):
    
    if age < 0 or age > 150:
        raise ValueError
    else:
        return age
    
# result = set_age(25)
# print(result)


# result2 = set_age(-3)
# print(result2)

# exercise_6:

def divide(a, b):
    return(a / b)

def retry(func, a, b, n):

    for i in range(n):
        try:
            return func(a, b)
        except Exception as e:
            print(type(e).__name__)
            if i == (n -1):
                raise

# result = retry(divide, 2, 0, 2)
# print(result)


# exercise_7:

def count_errors(funcs):
    funcs_works = 0
    for func in funcs:
        try:
            func()
            funcs_works += 1
        except Exception:
            continue
    return funcs_works

# result = count_errors([lambda: 1, lambda: 1/0, lambda: int("x"), lambda:2])
# print(result)

    
# exercise_8:

"""
empty at moment
"""


