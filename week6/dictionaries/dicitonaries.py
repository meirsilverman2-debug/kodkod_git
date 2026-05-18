# Dicitonaries_Exercises:

# exercise_1:

def dictionary_sum_of_values(d: dict) -> int:
    sum = 0
    for v in d.values():
        sum += v
    
    return sum

# result = dictionary_sum_of_values( {"a": 1, "b": 2, "c": 3})
# print(result)

# exercise_2:

def dictionary_key_with_max_value(d: dict) -> str|int|tuple|float:
    max_value = 0
    max_key = " "
    for key in d:
        if d[key] > max_value:
            max_value = d[key]
            max_key = key

    return max_key

# result = dictionary_key_with_max_value({"a": 3, "b": 7, "c": 5})
# print(result)

# exercise_3:

def count_characters(string: str) -> dict:
    d = {letter: string.count(letter) for letter in string}

    return d

# result = count_characters("banana")
# print(result)

# exercise_4:

def invert_a_dicitionary(d: dict) -> dict:

    d2 = {v: k for k, v in d.items()}
    return d2

# result = invert_a_dicitionary( {"a": 1, "b": 2, "c": 3})
# print(result)

# exercise_5:

def marge_two_dictionaries(d1: dict, d2: dict) -> dict:
    d1.update(d2)   
    return d1

# result = marge_two_dictionaries({"a": 1, "b": 2}, {"b": 20, "c": 30})
# print(result)

# exercise_6:

def dict_filterd_by_value(d: dict, threshold) -> dict:
    d1 = {k: v for k, v in d.items() if v > threshold}

    return d1

# result = dict_filterd_by_value( {"a": 1, "b": 5, "c": 3, "d": 8}, threshold = 3 )
# print(result)

# exercise_7:

def dict_group_by_first_letter(lst: list[str]) ->  dict:
    d = {}
    for i in range(len(lst)):
        if lst[i][0]  not in d:
            d[lst[i][0]] = []
            d[lst[i][0]].append(lst[i])
        else:
            d[lst[i][0]].append(lst[i])
        
    return d

# result = dict_group_by_first_letter( ["apple", "ant", "banana", "berry", "cherry"])
# print(result)

# exercise_8:

def word_frequncy_dict(string: str) -> dict:
    
    d = {word: string.count(word) for word in string.split()}

    return d

# result = word_frequncy_dict( "the cat sat on the mat")
# print(result)

# exercise_9:

def common_keys(d1: dict, d2: dict) -> list[str]:
    lst = list(d1.keys() & d2.keys())

    return lst

# result = common_keys( {"a": 1, "b": 2, "c": 3}, {"b": 9, "c": 8, "d": 7})
# print(result)


# exercise_10:

def most_frequent_value(d: dict) -> any:
    cuont = 0
    prevalent = []
    lst = list(d.values())

    for value in lst:

        if lst.count(value) > cuont: 
            cuont = lst.count(value)
            prevalent = [value]

        elif lst.count(value) == cuont and value not in prevalent : 
            prevalent.append(value)
    # print(type(lst)) # for checking the type of d.values() to see that it cannot use .count()
    if len(prevalent) > 1:
        return prevalent
    else:
        return  prevalent[0]

result = most_frequent_value({"a": 1, "b": 2, "c": 1, "d": 3, "e": 1})
print(result)


    