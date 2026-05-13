# num = int(input("Please enter an integer: "))

# if num < 0:
#     num = 0
#     print("Negative changed to zero")
# elif num == 0:
#     print("Zero")
# elif num == 1:
#     print("Single")
# else:
#     print("More")

# # Measure some strings:
# words = ["cat", "window", "defenstrate"]
# for w in words:
#     print(w, len(w))

# Create a small collection
# users = {"Meir": "active",
#          "Manman": "inactive",
#          "Mimi": "inactive",
#          "David": "active",
        #  }

# Strategy: Iterate over a copy
# for user, status in users.copy().items:
#     if status == "inactive":
#         del users[user]

# Strategy: Create a new collection
# active_users = {}
# for user, status in users.items():
#     if status == "active":
        #  active_users[user] = status

# for i in range(5):
#         print(i)

# print(list(range(5, 10)))

# print(list(range(0, 10, 3)))

# print(list(range(-10, -100, -30)))

# list = ["tiny", "deep", "unscrupulous", "bid"]
# for i in range(len(list)):
#     print(i, list[i])

# print(range(10))

# print(sum(range(10)))

# Question_1:

# age = int(input("Enter your age: "))

# if age < 0 or age > 120:
#     print("Invalid")

# elif 0 < age <= 12:
#     print("Child") 

# elif  13 <= age <= 17:
#     print("Teen")

# else:
#     print("Adult")

# Question_2:

# char = input("Enter a char: ")

# if char not in "abcdefjhijklmnopqrstuvwxyz":
#     print("Invalid")

# elif char in "aeiou":
#     print("vowel")

# else:
#     print("Consonant")

# Question_3:

# age = int(input("Enter your age: "))

# if age < 16:
#     print("reject")

# elif age >= 18:

#     if age in range(19,22):
#         print("Enter")
    
#     else:
#         VIP_card = input("Please enter yes/no: ")
        
#         if VIP_card == "YES":
#             print("Enter")
        
#         else:
#             print("reject")

# Question_4:

# code = "Meirsilver7"
# password = input("Enter your password: ")

# if password == code:
#     print("Access Granted")

# else:

#     if len(password) < 8 :
#         print("Too short")

#     else:
#         print("Wrong password")

# Question_5:

# x = int(input("Enter coordinate: "))
# y = int(input("Enter coordinate: "))

# if   10 < x < 50 and 20 < y < 80:
#     print("Insid the rectangle")

# elif (x == 10 or x == 50) or (y == 80 or y ==20):
#     print("On the edge")

# else:
#     print("Outside the rectangle")

# Question_6:

# name = input("Please enter your name: ")
# print(f" greeting {name or "Anonymous"}")

# Question_8:

# def how_many_are_positiv(num1: int, num2:int, num3:int)-> int:
#     print((num1 > 0) + ( num2 > 0) +                                                                                                                                                                                                                                                                                  (num3 > 0))

# how_many_are_positiv(1, 2, -3)

# Question_10:

score = int(input("Please choose a score from 0 to 100: "))

print("A" if score >= 90 and score <= 100 else "B" if score >= 80 and score <=89 else "C" if score >= 70 and score <= 79 else "F" if score < 70 else "NOT valid" )
































