# function number one:
# I used the chat to help me !!! (mostly to debug and giving input to my code and fixing the bugs in the code)

def load_tasks(filename):
    '''
    :dicts קוראת את הקובץ ומחזירה רשימה של
    [{'id': 1, 'status': 'PENDING', 'desc': 'ללמוד Python'}, ...]
    אם הקובץ לא קיים — מחזירה רשימה ריקה
    '''
    task = []
    keys = ["id", "status", "desc"]
    
    try:
        with open(file=filename, mode="r", encoding="utf-8") as file:
            for line in file.readlines():
                line = line.strip().split("|")
                task.append({keys[0]: line[0], keys[1]: line[1], keys[2]: line[2]})
        return task        
    except Exception as e:
        print(f" Error: {e} !!!")
        return task
        
    
load_tasks("tasks.txt")


# function number two: 
 
def save_tasks(filename, tasks):
    '''
    שומרת את רשימת המשימות לקובץ
    description|status|id :פורמט כל שורה
    '''
    with open(file=filename, mode= "w", encoding="utf-8") as saving_f:
        for d in tasks:
            for v in d.values():
                saving_f.write(f"{v}|")
            saving_f.write("\n")    

# function number three:

def add_task(filename, description):
    '''
    :מוסיפה משימה חדשה עם
    מספר המשימה הבאה = ID -
    - status = 'PENDING'
    הפרמטר שניתן = description -
    '''
    id = 1
    task = load_tasks(filename)

    if task:

        for d in task:
            id += 1
        task.append({"id":id, "status": "PENDING", "desc": description})
        save_tasks(filename, task)  
        return
    
    task.append({"id": 1, "status": "PENDING", "desc": description})

    save_tasks(filename , task)


# function number four:

def complete_task(filename, task_id):
    '''
    DONE-ל PENDING-מ id_task של משימה status משנה את
    לא קיים — מדפיסה הודעת שגיאה ID-אם ה
    '''
    task = load_tasks(filename)

    for d in task:
        if int(d["id"]) == task_id:
            d["status"] = "DONE"
            save_tasks(filename, task)
            return
        
    raise KeyError("Error id does not exists")
    
            
# function number five:

def list_tasks(filename):
    '''
    :מציגה את כל המשימות בפורמט מסודר
    ]✓[ 2 [ 2 |לכת תרתרג 1
    ] [ 3 | לסיים את הפרויקט
    '''
    
    task = load_tasks(filename)

    for d in task:

        if d["status"] == "DONE":
            print(f'{d["desc"]} {d["id"]} [✔]')
        
        else:
            print(f'{d["desc"]} {d["id"]} []')



def main():
    FILENAME = "tasks.txt"
    while True:
        print('\n=== To-Do List Manager ===')
        print('1. Show tasks')
        print('2. Add task')
        print('3. mark task complete')
        print('4. Exit')
        choice = input('Choice: ')

        if choice == '1':
            list_tasks(FILENAME)
        elif choice == '2':
            desc = input('Task description: ')
            add_task(FILENAME, desc)
            print('! The task was added')
        elif choice == '3':
            task_id = int(input('Task id number:'))
            complete_task(FILENAME, task_id)
        elif choice == '4':
            print('!Goodbieeeeee')
            break
        else:
            print('Invalid choice!!!')


if __name__ == '__main__':
    main()
