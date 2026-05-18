# Tuples Exercises:

# exercise_1:

def sum_a_tuple(t: tuple) -> int:
    sum = 0
    for i in t:
        sum += i
    return sum

# result = sum_a_tuple((1, 2, 3, 4, 5))
# print(result)


# exercise_2:

def max_n_from_a_tuple(t: tuple) -> int:
    highest = t[0] 
    for num in t:
        if num > highest:
            highest = num
        else:
            continue
    return highest

# result = max_n_from_a_tuple((3, 7, 2, 8, 5))
# print(result)


# exercise_3:

def count_occurrences(t: tuple, value: int) -> int:
    count = 0
    for num in t:
        if num == value:
            count += 1
        else:
            continue
    return count

# result = count_occurrences((1, 2, 3, 2, 4, 2), value = 2)
# print(result)

# exercise_4:
# v_1:
def reverse_a_tuple(t: tuple) -> tuple:

    r_tuple = []

    for num in t:
        r_tuple.insert(0, num)

    return tuple(r_tuple)

# result = reverse_a_tuple((1, 2, 3, 4))
# print(result)

# v_2:

def reverse_a_tuple(t: tuple) -> tuple:
    r_tuple = ()
    i = -1
    for _ in range(len(t)):
        r_tuple += (t[i],)
        i -= 1
    return r_tuple

# result = reverse_a_tuple((1, 2, 3, 4))
# print(result)

# exercise_5:

def swap_pairs(t: tuple) -> tuple:
    tuple = ()
    for num in range(0, len(t), 2):
        tuple += (t[num + 1], t[num])
    return tuple


# result = swap_pairs((1, 2, 3, 4, 5, 6))
# print(result)


# exercise_6:

def highest_and_lowest_of_a_tuple(t: tuple) -> tuple:
    highest = 0
    lowest = t[0]
    tuple = ()
    for num in t:
        if num > highest:
            highest = num
        elif num < lowest:
            lowest = num
        else:
            continue
    tuple += (lowest, highest)
    return tuple

# result = highest_and_lowest_of_a_tuple((4, 1, 7, 3, 5))
# print(result)

# exercise_7:

def distance_between_points(t1: tuple, t2: tuple) -> int:
    x1, y1 = t1
    x2, y2 = t2

    return (((x2 - x1)** 2) + ((y2 - y1)** 2)) ** 0.5

# result = distance_between_points((0, 0), (3, 4))
# print(result)

# exercise_8:

def merge_and_sort_tupels(t1: tuple , t2:tuple) -> tuple:
    t = t1 + t2
    t = list(t)
    for _  in range(len(t)):
        for j in range(len(t) -1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1]  =  (t[j + 1], t[j])

    return tuple(t)        

# result =merge_and_sort_tupels( (3, 1, 4), (1, 5, 9))
# print(result)

# exercise_9:

def frequency_table_of_a_tuple(t1: tuple) -> tuple:
    t1 = list(t1)
    items_count = []
    tuple = ()

    for i in range(len(t1)):
        if t1.count(t1[i]) not in items_count or t1[i] not in items_count:
            items_count.append(t1.count(t1[i]))
            items_count.append(t1[i])
            
        else:
            continue

    for i in range(0, len(items_count), 2):
            tuple += (items_count[i], items_count[i + 1]),

    return tuple
    # return items_count    


# result = frequency_table_of_a_tuple(("a", "b", "a", "c", "b", "a"))
# print(result)


# exercise_10:

def rotate_a_tuple(t1: tuple, k: int) -> tuple:
    k = k % len(t1)
    
    return t1[-k: ] + t1[:-k]



result = rotate_a_tuple( (1, 2, 3, 4, 5), k = 2)
print(result)



