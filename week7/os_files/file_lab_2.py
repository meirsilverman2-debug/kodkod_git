import os

# CVS basic , File Excercise_2:

# part_A:

# def create_grades_file(filename):
#     students = [
#         ("Dan", [85, 90, 78]),
#         ("MOMO", [92, 88, 95]),
#         ("Yoni", [70, 65, 80]),
#         ("Avi", [100, 95, 98]),
#      ]
    
#     with open(file=filename, mode="w",newline="", encoding="utf=8") as grade_f:
#         for tuple in students:
#             list(tuple[0]) + tuple[1]
#         writer = csv.writer(grade_f) 

#         writer.writerows(students)  
        

# create_grades_file("grades.txt")



def create_grades_file(filename):
    students = [
        ("Dan", [85, 90, 78]),
        ("MOMO", [92, 88, 95]),
        ("Yoni", [70, 65, 80]),
        ("Avi", [100, 95, 98]),
        ("Sara", [60, 72, 68]),

     ]
    
    with open(file=filename, mode="w", encoding="utf=8") as grade_f:
        for line in students:
            name, grades = str(line[0]), str(line[1])
            sentence = name + ", " + grades.strip("[]")
            grade_f.write(sentence + "\n")

create_grades_file("grades.txt")

# part_B:

def calculate_averages(filename):
    '''
מחשבת ממוצע לכל סטודנט ,txt.grades קוראת
{שם: ממוצע} dict :מחזיר
    '''
    averages = {}
#     # כתבו את הקוד כאן
    with open(file=filename, mode="r", encoding="utf=8") as grade_f:

        for line in grade_f.readlines():
            line = line.strip("\n").split(",")
            name = line.pop(0)
            average = sum([int(item) for item in line]) / len(line)
            averages[name] = average

    return averages








results = calculate_averages('grades.txt')
for name, avg in results.items():
    print(f'{name}: {avg:.1f}')

# "calculate_averages(("grades.txt"))

# part_c:

def save_results(averages, output_filename):
    '''
    filename_output: כותבת לקובץ
    שורה ראשונה: כותרת
    שורות הבאות: שם וממוצע, ,ממויין מגבוה לנמוך
    '''

    sorted_averages = {name: average for name, average  in sorted(averages.items(), key= lambda item: item[1], reverse=True )}
    
        
    with open(file=output_filename, mode= "w", encoding="utf=8") as outputfile:
        outputfile.write("=== Student Results ===\n")
        i = 1
        for name, avg in sorted_averages.items():
            outputfile.write(f"{i}. {name}: {avg:.1f}\n")
    
            i += 1
            

averages = calculate_averages('grades.txt')
save_results(averages, 'results.txt')


#    results.txt:
# === Student Results ===
#    1. Avi: 97.7
#    2. MOMO: 91.7
#    3. Dan: 84.3
#    4. Yoni: 71.7
#    5. Sara: 66.7

# part_d: Stats


def stats_calculate(filename, outputfile):

    pass_students = 0

    with open(file=filename, mode="r", encoding="utf=8") as add_file:
        
        # for getting the class average.
        for line in add_file.readlines():
            line = line.strip().split(",")
            if int(line[1]) >= 60: 
                pass_students += 1 
            
            name = line.pop(0)
            class_average = sum([int(grade) for grade in line ]) / len(line)

    with open(file=outputfile, mode="a+", encoding="utf=8") as file2:
        file2.seek(0)
        lines = file2.readlines()
        
        file2.write("=== Statistics ===\n")
        file2.write(f"Lowest: {lines[-1]}")
        file2.write(f"This is the class average: {class_average}\n")
        file2.write(f"passing (>=60): {pass_students}/5\n")


    
    with open(file=outputfile, mode="a+", encoding="utf=8") as file:
        file.seek(0)

        file.readline() # to skip the first line which is just a nice srting

        max_grade = file.readline() # the next line is the best student in the class because it goes from high to low.
        file.write(f"Highest: {max_grade}\n")

        
        


stats_calculate("grades.txt", "results.txt")
        







