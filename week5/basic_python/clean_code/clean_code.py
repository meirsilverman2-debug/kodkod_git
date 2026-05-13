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

handle_purcase("'vfdbdfb", "soda", 5, 3, 7  )