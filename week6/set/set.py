# Set_Exercises:

# execise_1:

def remove_duplicates(arr: list) -> list:

    uniqu = set(arr)

    return list(uniqu)

# result = remove_duplicates([1, 2, 2, 3, 1, 4, 3])
# print(result)

# execise_2:

def count_uniqu(arr: list) -> int:
    uniqu = set(arr)
    sum_unique = 0

    for _ in uniqu:
        sum_uniqu += 1

    return sum_uniqu

# result = count_uniqu( [1, 2, 2, 3, 1, 4])
# print(result)

# execise_3:

def common_elemnts(arr1: list, arr2: list) -> list:
    set1, set2 = set(arr1), set(arr2)

    return list(set1 & set2)

# result = common_elemnts( [1, 2, 3, 4], [3, 4, 5, 6])
# print(result)

# execise_4:

def elments_in_only_one(arr1: list, arr2: list) -> list:
    set1, set2 = set(arr1), set(arr2)
    lst = list(set1 ^ set2)

    return lst.sort()

# result = elments_in_only_one([1, 2, 3, 4], [3, 4, 5, 6])
# print(result)

# execise_5:

def is_subset(arr1: list, arr2: list) -> bool:
    set1, set2 = set(arr1), set(arr2)
    subset = True

    for item in set1:
        if item in set2:
            subset = True
        else:
            subset = False 

    return subset
    
# result = is_subset([1, 2, 3], [1, 2, 3, 4, 5])
# print(result)

# result2 = is_subset([1, 2, 6], [1, 2, 3, 4, 5])
# print(result2)


# execise_6:

def uniqu_characters(string: str) -> bool:
    distinct = True

    if len(set(string)) == len(string):
        distinct = True

    elif len(set(string)) != len(string):
        distinct = False
    
    return distinct

# result = uniqu_characters("abcdef")
# print(result)

# result2 = uniqu_characters("hello")
# print(result2)


# execise_7:

def first_repeated_elment(arr: list) -> int|None:
    memory_set = set()

    for i in range(len(arr)):
        if arr[i] in memory_set:
            return arr[i]
        else:
            memory_set.add(arr[i])

    return None

# result = first_repeated_elment([1, 2, 3, 2, 4, 1])
# print(result)

# result2 = first_repeated_elment([1, 2, 3, 4])
# print(result2)



# execise_8:

def distinct_words(string: str) -> int:
    string = string.lower() # (case-insensitive).
    set1 = set(string.split())
    sum_unique = 0

    for _ in set1:
        sum_unique += 1

    return sum_unique

# result =distinct_words( "The cat and the dog and the bird")
# print(result)


# execise_9:

def pair_sum_exists(arr: list[int], target: int) -> bool:
    memory_set = set()
    missing = 0

    for i in range(len(arr)):
        missing = target - arr[i] 
       
        if missing in memory_set:
            return True
        memory_set.add(arr[i])

    return False

# result = pair_sum_exists( [3, 1, 4, 7, 2], target = 6)
# print(result)
        
# result2 = pair_sum_exists( [3, 1, 4, 7, 2], target = 100)
# print(result2)


# execise_10:

def symmetric_difference_without_operetors(arr1: list, arr2: list) -> list:
    set1, set2 = set(arr1), set(arr2)
    lst = []

    for item in set1:
        if item in set2:
            continue
        else:
            lst.append(item)
    
    for item in set2:
        if item in set1:
            continue
        else:
            lst.append(item)
    lst = sorted(lst)
    return lst

result = symmetric_difference_without_operetors([1, 2, 3, 4], [3, 4, 5, 6])
print(result)
