grades = {
"1": {"name": "Moshe", "grade": 88},
"2": {"name": "Yaakov", "grade": 75},
"3": {"name": "David", "grade": 92},
}
top_student ={}
top_student = 0

for k in grades.keys():
    if grades[k]["grade"] > top_student:
        top_student = grades[k]["grade"]
        d  = grades[k] 
print(d)