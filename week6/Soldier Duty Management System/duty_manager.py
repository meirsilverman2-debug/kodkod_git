from data import soldiers, days, stats


# ============================================================================
# duty_manager.py
# אחריות: לוגיקה עסקית של ניהול תורנויות
# ============================================================================

def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str) -> None:
    """
    מוסיפה תורנות חדשה לחייל.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        day (str): יום בשבוע (sunday/monday/tuesday/wednesday/thursday)
    
    מחזירה:
        None - הפונקציה מוסיפה את התורנות או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        ValueError: אם תורנות עם שם זה כבר קיימת לחייל
        ValueError: אם day לא חוקי (friday/saturday או ערך לא תקין)
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של הוספת תורנות.
    מבצעת בדיקות ומוסיפה תורנות לחייל.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    if day not in days:
        raise ValueError(f"{day} not valid ")
    
    for soldier in soldiers:

        if soldier["id"] == soldier_id and day in days:

            for duty in soldier["duties"]:
                if duty["name"] == duty_name:
                    raise ValueError(f"there is a duty named {duty_name} for this soldier")
        
             
            soldier["duties"].append({"name": duty_name, "day": day, "status": "pending"})
            return None
        
    raise KeyError(f"There isn't a soldier with this {soldier_id} number")
        



def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    """
    מעדכנת את הסטטוס של תורנות.
    
    סוג: לוגיקה עסקית (Business Logic)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
        duty_name (str): שם התורנות
        new_status (str): סטטוס חדש (pending/completed/missed)
    
    מחזירה:
        None - הפונקציה מעדכנת את הסטטוס או זורקת exception
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
        KeyError: אם תורנות עם שם זה לא נמצאה לחייל
        ValueError: אם new_status לא חוקי (לא pending/completed/missed)
    
    למה הפונקציה קיימת:
    לוגיקה עסקית של עדכון סטטוס.
    מבצעת בדיקות ומעדכנת את הסטטוס.
    זורקת exceptions במקרה של שגיאה במקום להחזיר False.
    """
    if new_status  not in stats:
        raise ValueError(f"{new_status} is not valid!!")
    
    for soldier in soldiers:
        if soldier["id"] == soldier_id:
            
            for duty in soldier["duties"]:
                if duty["names"] == duty_name:
                    duty["status"] = new_status
                    return None
                raise KeyError(f"There is not any duty that much {duty_name}")
    raise KeyError(f"There is not a soldier with {soldier_id}")

            

def get_soldier_duties(soldier_id: int) -> list:
    """
    מחזירה את רשימת התורנויות של חייל.
    
    סוג: גישה לנתונים (Data Access)
    
    מקבלת:
        soldier_id (int): מספר אישי של החייל
    
    מחזירה:
        list: רשימת תורנויות (מילונים)
              רשימה ריקה אם אין תורנויות
    
    זורקת:
        KeyError: אם חייל עם id זה לא נמצא במערכת
    
    למה הפונקציה קיימת:
    גישה מבוקרת לתורנויות של חייל.
    מפרידה בין הנתונים לבין הגישה אליהם.
    זורקת exception אם החייל לא קיים (במקום להחזיר רשימה ריקה).
    """
    for soldier in soldiers:
        if soldier["id"] == soldier_id:
            
            
                if soldier["duties"]:
                    return soldier["duties"]
                return []
        
    raise KeyError(f"A soldier with {soldier_id} does not exists in the data base")
                
