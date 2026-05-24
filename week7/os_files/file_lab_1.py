import os


# File_excercise_1:

file = "diary.txt"

with open(file= file, mode="w", encoding="utf=8") as create_f:

    create_f.write(" Today was a busy day:2024-01-15  \n")
    create_f.write(" I learned about file handling in python: 2024-01-16 \n")
    create_f.write("I have finshed the first excercise:2024-01-17 \n")

    print(f"{create_f} was created how wonderful")

with open(file= file, mode= "r", encoding="utf=8") as read_f:
    content = read_f.read()
    print(content)

# excercise_2:

def add_entry(filename, date, content):
    
    if safe_read_diary():
        safe_read_diary()
        with open (file=filename, mode="a", encoding="utf=8") as file_a:
            file_a.write(content + date)
    else:
        print
add_entry(file, ":2024-01-18", "It is a wonderful day I finished excercise one" )

# excercise_3:

def search_diary(filename, keyword):
    lst = []
    with open(file= filename, mode= "r", encoding="utf+8") as file:
        for line in file.readlines():
            if keyword in line:
               lst.append(line.strip())
    print(lst)

search_diary(file, "I")


def  safe_read_diary(filename):
    if not os.path.exists(filename):
        print("ERROR file does not exist!!")
        return None
    else:
        add_entry()

    