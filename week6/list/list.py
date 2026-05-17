# List Exercise: Sunday_week_six
# exercise_1:

def sum_list(arr:list[int]) -> int:
    sum = 0
    for i in arr:
        sum += i
    return sum

# result = sum_list([1, 2, 3, 4, 5])
# print(result)

# exercise_2:

def max_list_item(lst: list[int]) -> int:
    highest = lst[0]
    
    for i in lst:
        if i > highest:
            highest = i
        else:
            continue
    return highest

# result = max_list_item([3, 7, 2, 8, 5])
# print(result)


# exercise_3:

def appearances_in_a_list(lst: list[int], num: int) -> int:
    num_appear = 0
    for i in lst:
        if i == num:
            num_appear += 1
        else:
            continue
    return f" {num} appears {num_appear} in the list."

# result = appearances_in_a_list([1, 2, 3, 2, 4, 2], 2)
# print(result)

# exercise_4:

def reverse_a_list(arr: list[any]) -> list[any]:

    reverse_arr = []
    i = -1

    for _ in range(len(arr)):
        reverse_arr.append(arr[i])
        i -= 1
    
    return reverse_arr

# result = reverse_a_list([1, 2, 3, 4])
# print(result)

# exercise_5:

# def remove_duplicates(lst: list[any]) -> list[any]:
    j = 1
    

    for i in range(len(lst)):
        if i < len(lst):
            if lst[i] == lst[j]:
                lst.remove(i)
                j += 1
            else:
                continue
        return lst

def remove_duplicates(lst : list[any]) -> list[any]:
    uniqu_list = []

    for item in lst:
        if item in uniqu_list:
            continue
        else:
            uniqu_list.append(item)

    return uniqu_list


# result = remove_duplicates([1, 2, 2, 3, 1, 4, 3])
# print(result)

# exercise_6:
# ver.1
"""
def second_highest_value(arr: list[int]) -> int:

    
    second_highest = 0
    highest = 0
    
    for num in arr:   
        if num > highest:
            highest = num 

    for num in arr:
        if num == highest:
            continue
        else:
            if num > second_highest:
                second_highest = num

    if second_highest != 0:
        return second_highest
    return None
"""
# ver.2
def second_highest_value(arr: list[int]) -> int:

    
    second_highest = int()
    highest = 0
    
    for num in arr:   
        if num > highest:
            highest = num 

    for num in arr:
        if num != highest and num > second_highest:
            second_highest = num
        
    if second_highest != 0:
        return second_highest
    return None
    
# result = second_highest_value([7, 0, 7, 7])
# print(result)

# result2 = second_highest_value([10, 10, 10])
# print(result2)


# exercise_7:

def marge_two_sorted_list(lst1: list[int], lst2: list[int]) -> list[int]:

    lst1.extend(lst2)
    sorted_list = []
    first_num = lst1[0]
    sorted_list.append(first_num)

    for num in lst1:
        if num < sorted_list[0]:
            sorted_list.insert(0, num)
        elif num > sorted_list[-1]:
            sorted_list.append(num)
        else:

            for i in range(len(sorted_list) -1):
                if sorted_list[i] < num < sorted_list[i + 1]:
                    sorted_list.insert(i + 1, num)
                    break
        
    return sorted_list



# result = marge_two_sorted_list([1, 3, 5], [2, 4, 6])
# print(result)

# result1 = marge_two_sorted_list([6, 7, 8, 2], [1, 9])
# print(result1)

# exercise_8:

def rotate_a_list(lst: list[int], k: int) -> list[int]:
    for i in range(k):
         num = lst.pop()
         lst.insert(0, num)

    return lst


result = rotate_a_list([1, 2, 3, 4, 5], k = 7)
print(result)


"""
YESSSS I finished my homework for Sunday on week six I am so happy I hope I did right, and 
for the two greatest teachers ever I wish you all the best day you are both amazing teachers and people
and I appreciate it a lottttt!!!!
"""




