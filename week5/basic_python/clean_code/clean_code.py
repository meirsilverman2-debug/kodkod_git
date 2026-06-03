# question_1: Correct Naming
# from this:
"""
def f(l):
    r = []
    for x in l:
        if x[1] >= 18 and x[2] == "active":
            r.append(x[0])
    return r

d = [
    ["Dan", 25, "active"],
    ["Noa", 16, "active"],
    ["Yael", 30, "inactive"],
]

print(f(d))
"""
# to this:

def filter_users(users: list[str|int]) -> list[str]:
    """
        Gets a list of users and rturn a list of adults and active users only.
    """
    adults_and_active_users = []

    for user in users:
        if user[1] >= 18 and user[2] == True:
            adults_and_active_users.append(users[0])

    return adults_and_active_users

users = [
    ["Dan", 25, True],
    ["Noa", 16, True],
    ["Yael", 30, False],
]

print(filter_users(users))

# question_2: Small Functon
# from this
"""
def handle_purchase(user_email, product_name, product_price, stock, quantity):
    if not user_email:
        print("Invalid user")
        return None
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity")
        return None

    price = product_price * quantity
    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85

    stock -= quantity

    order_user = user_email
    order_product = product_name
    order_quantity = quantity
    order_total = price
    order_status = "confirmed"
    print(f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}")
    return order_user, order_product, order_quantity, order_total, order_status
"""
# to this

def is_email(user_email: str) -> str|None:
    """
    Checks if the user is through an email.
    """
    if not user_email:
        print("Invalid user!!!")
        return False
    return user_email


# user = ""
# is_user_email(user) # for tests

def is_amount_valid(quantity: int, stock:int ) -> int|None:
    """
    Gets tha quantity of the product and rturn the amount if it is valid else it ret
    """
    if quantity <= 0 or quantity > stock:
        print("Invalid quantity!!!")
        return False
    return quantity


def the_total_price(product_price: int, quantity:int) -> int:
    """
    Gives the buyer the end price meaning the total.
    """
    price = product_price * quantity

    if quantity >= 10:
        price *= 0.9
    if quantity >= 50:
        price *= 0.85
    return price
    

def  handle_purcase(user_email, product_name, product_price, stock, quantity):
    if is_email(user_email):  
        order_user = is_email(user_email)
    else:
        return
    if is_amount_valid(quantity, stock):
        order_quantity = is_amount_valid(quantity, stock)
    else:
        return
    order_product = product_name
    order_total = the_total_price(product_price, quantity)
    stock -= quantity

    order_status = "confirmed"
    print(f"Order {order_status}: {order_user} bought {order_quantity}x {order_product} for ${order_total}")
    return order_user, order_product, order_quantity, order_total, order_status

# handle_purcase("'vfdbdfb", "soda", 5, 3, 7  ) # trying to ru the code

# question_3: Single Responsibility
# from this:
"""
def manage_students(names, grades, new_name, new_grade):
    # validation
    if not new_name or len(new_name) < 2:
        print("Error: invalid name")
        return students
    if new_grade < 0 or new_grade > 100:
        print("Error: grade must be 0-100")
        return students

    # add student
    grades.append(new_grade)

    # calculate stats
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)

    # print report
    print("=== Student Report ===")
    for i in range(len(names)):
        print(f"  {names[i]}: {grades[i]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")

    # save to file
    with open("students.txt", "w") as f:
        for i in range(len(names)):
            f.write(f"{names[i]},{grades[i]}\n")

    return names, grades
"""
# to this

def validation(new_name, new_grade):
    if not new_name or len(new_name) < 2:
        print("Error: invalid name")
        return False
    if new_grade < 0 or new_grade > 100:
        print("Error: grade must be 0-100")
        return True

def add_student(grades, new_grade, names, new_name):
    # add student
    grades.append(new_grade)
    names.append(new_name)


def calculate_stats(grades):
    total = sum(grades)
    average = total / len(grades)
    top_count = sum(1 for g in grades if g >= 90)
    failing_count = sum(1 for g in grades if g < 56)

    




def print_report(names, grades):
    print("=== Student Report ===")
    for i in range(len(names)):
        print(f"  {names[i]}: {grades[i]}")
    print(f"Average: {average:.1f}")
    print(f"Top students: {top_count}")
    print(f"Failing: {failing_count}")


def save_to_file(names, grades):
    with open("students.txt", "w") as f:
        for i in range(len(names)):
            f.write(f"{names[i]},{grades[i]}\n")

    # return names, grades


def manage_students(names, grades, new_name, new_grade):

    validation(names, new_name, new_grade)
    add_student(grades, new_grade)
    # calculate_stats(grades)
    # print_report(names, grades,)
    # save_to_file(names, grades)

    print(names, grades)



manage_students(["Meir", "David"], [80, 40], "Manman", 100)