# function number one:
# I used the chat to help me !!! (mostly to debug and giving input to my code and fixing the bugs in the code)

def load_tasks(filename):
    '''
    :dicts קוראת את הקובץ ומחזירה רשימה של
    [{'id': 1, 'status': 'PENDING', 'desc': 'ללמוד Python'}, ...]
    אם הקובץ לא קיים — מחזירה רשימה ריקה
    '''
    tasks = []
    keys = ["id", "status", "desc"]
    d = {}
    try:
        with open(file=filename, mode="r", encoding="utf-8") as file:
            for line in file.readlines():
                line = line.strip().split("|")

                d = zip(keys, line)
                tasks.append(dict(d))
        
        return tasks
            
    except Exception as e:
        print(f" Error: {e} !!!")
        return tasks
        
    
result = load_tasks("tasks2.txt")
print(result)

# function number two: 

def save_tasks(filename, tasks):
    '''
    שומרת את רשימת המשימות לקובץ
    description|status|id :פורמט כל שורה
    '''
    count = 0
    with open(file=filename, mode= "w", encoding="utf-8") as saving_f:
        for d in tasks:
            for v in d.values():
                if count <= 2: 
                    saving_f.write(f"{v}|")
                saving_f.write(f"{v}")
                count += 1
            saving_f.write("\n")
            count = 0

save_tasks("tasks2.txt", result)