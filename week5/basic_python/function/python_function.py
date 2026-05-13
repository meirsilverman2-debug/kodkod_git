# Question_1:

def is_it_even(num: int) -> bool:
    """
     Get a number and checks if the number is even.
    """
    
    if num % 2 == 0:
        return True
    
    return False


# result1 = is_it_even(1)

# result2 = is_it_even(2)

# print(result1)
# print(result2)

# Question_2:


def factorial(num: int) -> int:
    """
    Gets a number than return its factorial value.
    """

    sum = 1
    

    for i in range(1, num + 1):
        sum *= i
         
    return sum
    

# result = factorial(4)
# print(result)

# Question_4:

def is_palindrom(text: str) -> bool:
    """
    Receiv a text and tells you if it's a palindrom.
    """

    if text[::-1] == text:
         return True
    
    return False


# palindrom = is_palindrom("anna")
# print(palindrom)

# Question_5(part of question 3):

def sum_digits(num: int) -> int:
    """
    Takes any number and add each digit in it and perform additon on them to return their sum value.
    """

    sum = 0
    while num > 0:

        sum += (num % 10)
        num = num // 10

    return sum

def digital_root(num: int) -> int:
    """
    Unless the number is smaller than 10 it will perform a sum on the digit of thet number again and again.
    """
    
    while num >= 10:

        num = sum_digits(num)

    return num

# dr = digital_root(123)

# print(dr)

# print(1 // 10)

# Question_6:

def how_many_digits(num: int) -> int:

    count_digits = 0

    while num > 0:
        num = num // 10
        count_digits += 1

    return count_digits 

# number = how_many_digits(123)
# print(number) 

# Question_7:

def revers_integer(num):

    save_num = num 
    num = num * -1

    

    revers_num = 0
    while num > 0 :

        revers_num = revers_num * 10 + (num % 10)
        num = num // 10

        if save_num > 0: 
            return revers_num
        
    revers_num *= -1
    return revers_num
    


# rebmun = revers_integer(-1234)
# print(rebmun)


# Question_8:

# def all_zeros_to_the_end(lst:list[int]) -> list[int]:
     
#     zeros = 0
#     for i in lst:

#         if i == 0:
#             zeros += 1

#     for i in range(zeros):
#         lst.remove(0)
#         lst.append(0)

#     return lst

# option_2

def all_zeros_to_the_end(lst:list[int]) -> list[int]:
     
    j = 0

    for _ in range(len(lst)):
        if lst[j] == 0 :
            lst.append(lst.pop(j))
            j -= 1
        j += 1
        
    return lst
             
# numbers = [0, 0, 1, 0, 2, 3, 0]
# new_list = all_zeros_to_the_end(numbers)
# print(new_list)

# Question_9:

def  sum_list_num(lst: list[int]) -> int:

    sum = 0 
    for num in lst:
        sum += num

    return sum

# python_numbers = [4, 7, 2, 9, 1, 5]
# average_num = sum_list_num(python_numbers)
# print(average_num)


def average_of_list(lst: list[int]) -> int:

    average = (sum(lst) / len(lst)) 

    return average    

# python_numbers = [4, 7, 2, 9, 1, 5]
# average_num = average_of_list(python_numbers)
# print(average_num)


def minimum(lst: list[int])-> int:
    """
    Get a list and goes over it and fetches the smallest number inside it.
    """
    smallest = lst[0]

    for num in lst[1:]:
        if num < smallest:
            smallest = num
        
    return smallest

# python_numbers = [4, 7, 2, 9, 1, 5]
# smallest_num = minimum(python_numbers)
# print(smallest_num)


def maximum(lst: list[int]) -> int:
    """
    Receive a list of numbers and fetches the biggest one of them back.
    """
    biggest = lst[0]

    for num in lst[1:]:

        if num > biggest:
            biggest = num
        
    return biggest

# python_numbers = [4, 7, 2, 9, 1, 5]
# biggest_num = maximum(python_numbers)
# print(biggest_num)

# Question_10:

def reverse_a_list(lst: list[int]) -> list[int]:
    """
    Takes a list and revers it.
    """
    new_list = []
    
    j = -1
    
    for _ in range(len(lst)):
        
        new_list.append(lst[j])
        j -= 1
     

    return new_list

# python_original = [1, 2, 3, 4, 5] 

# reversed_list = reverse_a_list(python_original)
# print(reversed_list)

# Question_11:

def list_duplicate_big_no_no(lst: list[int]) -> list[int]:
    """
    Takes down duplicates from a list so you receive it without duplicats but without changing the orignal order.
    """
    unique_num = []
                                                    
    for num in lst:
        if num in unique_num:
            continue
        else:
            unique_num.append(num)    

    return unique_num


# python_items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] 
# unique_list = list_duplicate_big_no_no(python_items)
# print(unique_list)

# Yes at last I finish my homework for today I am so glad and happy.
# This homework was done on Monday on week five by Meir Silverman




