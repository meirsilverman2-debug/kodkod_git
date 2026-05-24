from soldier_manager import add_soldier, get_all_soldiers, remove_soldier
from duty_manager import add_duty_to_soldier, update_duty_status, get_soldier_duties
from data import soldiers

"""
מערכת ניהול תורנויות חיילים
"""

# ============================================================================
# main.py
# אחריות: תפריט ראשי, קלט מהמשתמש, ניתוב לפונקציות
# ============================================================================

def show_menu() -> None:
    """
    מציגה את התפריט הראשי למשתמש.
    
    מקבלת: כלום
    מחזירה: כלום (מדפיסה לקונסול)
    
    למה הפונקציה קיימת:
    הפרדה בין הצגת התפריט לבין הלוגיקה העסקית.
    אם נרצה לשנות את התצוגה, נשנה רק כאן.
    """
    print("=============================================")
    print("WELCOM TO THE SOLDIER MANAGING PROGRAM MENUE:")
    print("'1'. for adding a soldier")
    print("'2'. for removing a soldier")
    print("'3' to review the entier list of soldiers")
    print("'4' for adding a duty per soldier")
    print("'5' for upsating duty status per soldier")
    print("'6' to review all of the duties per soldier ")
    print("'7' to exit")
    print("============================================")


def get_user_choice() -> str:
    """
    מקבלת בחירה מהמשתמש.
    
    מקבלת: כלום
    מחזירה: מחרוזת המייצגת את בחירת המשתמש
    
    למה הפונקציה קיימת:
    הפרדת קבלת קלט מהמשתמש מהלוגיקה של עיבוד הבחירה.
    מאפשר להחליף את שיטת הקלט בעתיד (למשל, GUI).
    """
    choice = (input("Please enter your choice: "))
    return choice


def handle_add_soldier() -> None:
    """
    מטפלת בתהליך הוספת חייל חדש.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    מפרידה בין הקלט/פלט לבין הלוגיקה העסקית.
    main.py אחראי על אינטראקציה עם המשתמש,
    soldier_manager.py אחראי על הלוגיקה.
    """
    soldier_id = int(input("Please enter a soldier ID number: "))
    name = input("Please enter a name: ")
    add_soldier(soldier_id, name)
    print("a soldier was added")

def handle_remove_soldier() -> None:
    """
    מטפלת בתהליך הסרת חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    soldier_id = int(input("Please enter a soldier ID number: "))
    remove_soldier(soldier_id)
    print("the soldier was removed")
    



def handle_view_soldiers() -> None:
    """
    מטפלת בתהליך הצגת כל החיילים.
    קוראת לפונקציה המתאימה ומציגה את התוצאה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין קבלת הנתונים לבין הצגתם.
    """
    get_all_soldiers()
    print("You have been abale to view the entier list of soldiers")


def handle_add_duty() -> None:
    """
    מטפלת בתהליך הוספת תורנות לחייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    soldier_id = int(input("Please enter a soldier ID number: "))
    duty_name = input("Please enter a duty name: ")
    day = input("Please enter a day: ")
    add_duty_to_soldier(soldier_id, duty_name, day)
    print(f"A {duty_name} was added to duties")
    



def handle_update_duty_status() -> None:
    """
    מטפלת בתהליך עדכון סטאטוס תורנות.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    soldier_id = int(input("Please enter a soldier ID number: "))
    duty_name = input("Please enter a duty name: ")
    new_status = input("Please enter astatus from these options(missed, pending, or completed: )")
    update_duty_status(soldier_id, duty_name, new_status)


def handle_view_soldier_duties() -> None:
    """
    מטפלת בתהליך הצגת תורנויות של חייל.
    מקבלת קלט מהמשתמש וקוראת לפונקציות המתאימות.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    הפרדה בין UI לבין לוגיקה עסקית.
    """
    soldier_id = int(input("Please enter an ID number: "))
    duties_list = get_soldier_duties(soldier_id)
    print(duties_list)
    print(f"You have benn able to view all of the duties that belongs to {soldier_id}")

def main() -> None:
    """
    הפונקציה הראשית של התוכנית.
    מריצה לולאה ראשית שמציגה תפריט, מקבלת בחירה ומפעילה פעולה.
    
    מקבלת: כלום
    מחזירה: כלום
    
    למה הפונקציה קיימת:
    נקודת הכניסה לתוכנית. מנהלת את הזרימה הראשית.
    """
    choice = " "
    while choice != "7":

        show_menu()

        choice = get_user_choice()


        if choice == "1":
            handle_add_soldier()

        elif choice == "2":
            handle_remove_soldier()

        elif choice == "3":
            handle_view_soldiers()

        elif choice == "4":
            handle_add_duty()

        elif choice == "5":
            handle_update_duty_status()
        
        elif choice == "6":
            handle_view_soldier_duties()

    print(" program outtt...")
main()