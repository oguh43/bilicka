"""
x = int(input("X > "))
y = int(input("Y > "))
if x==0 or y==0:
    print("Err, invalid input")
    __import__("sys").exit()
print("1" if x > 0 and y > 0 else "2" if x < 0 and y > 0 else "3" if x < 0 and y < 0 else "4")

"""
from datetime import date, datetime


today = datetime.today()

birthday = datetime.strptime(input("Birthday? (DD.MM.YYYY)"),"%d.%m.%Y")

print(type(today-birthday))



