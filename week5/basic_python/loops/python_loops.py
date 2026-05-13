"""

# Question_1:

for i in range(1, 10):

    if i % 2 == 0:
        continue

    if i == 7:
        break

    print(i)
    
Question_2:

password = input("Enter your password: ")

while True:

    if password == "1234":
        print("Wellcome")
        break

    else:
        print("Try again")
        password = input("Enter your password: ")

# Question_3:

products = []

while True:
    product = input("Enter a product name(type 'done' to exit): ")

    if product == "done":
        break


    if product != "done":
        products.append(product)

 
print(products)

# Question_3(part_2):

for row in range(1, 3):
    for col in range(1, 3):
        if col == 2:
            break
    print(row, col)

# Question_4:

vowels = 0
string = input("Please entr a sentence: ")

for char in string:

    if char in "aeiou" or char in "AEIOU":
        vowels += 1

print(vowels)



# Question_5:

for i in range(1, 6):

    for j in range(1, 6):

        print(f"{i} x {j} = {i * j}")

# Question_6:

acc = " "
string = input("Enter a string sentence: ")

for char in string:
    acc = char + acc

print(acc)

# Question_7:

even_digits = 0
integer = int(input("Enter a positive number: "))

while integer > 0:

    if (integer % 10) % 2 == 0:
         even_digits += 1

    integer = integer // 10


    # if (integer // 100) % 2 == 0:
    #     even_digits += 1

    # if (integer % 10) % 2 == 0:
    #     even_digits += 1

    # if (integer % 100 // 10) % 2 == 0:
    #     even_digits += 1

print(even_digits) 
    

# Question_8:

new_string = " "
string = input("Enter a sentence: ")
 
for char in string:
    new_string += (char * 2)

print(new_string)

# Question_9:

highest = 0
while True:

    num = int(input("Enter a positive number: "))

    if num == 0:
        break

    elif num > highest:
        highest = num

print(highest)


# Question_10:

string = input("Enter everything you want: ")
valid = True
for ch in string:

    if ch in "1234567890" or ch.isalpha():
        continue

      
    else:
        valid = False
        break
print(valid)




# Question_11:

acc = 0
integer = int(input("Enter a number: "))

while integer > 0:
    
    acc = acc * 10 + (integer % 10) 
    integer = integer // 10

print(acc)

"""