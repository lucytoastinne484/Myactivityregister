from datetime import datetime
from datetime import date
import calendar
import time

time.sleep(3)

changes_1 = date(2023, 6 , 11)
uptade_changes_1 = "Criação do act register"
print(uptade_changes_1)
print(changes_1)
print()
print()
changes_2 = date(2023, 6 , 12)
uptade_changes_2 = "Implementação de calendarios"
print(uptade_changes_2)
print(changes_2)
print()
print()
changes_3 = date(2023, 6 , 13)
uptade_changes_3 = "Implementação do weekheader"
print(uptade_changes_3)
print(changes_3)
print()
print()
changes_4 = date(2023, 6, 14)
update_changes_4 = "Funçoes circadianas"
print(update_changes_4)
print(changes_4)
print()
print()
changes_5 = date(2023, 6 , 16)
print(changes_5)
update_changes_5 = "Ajuste na subclasse Future Activity Hour , Implementação do weekheader , Tranformaçao do ActivityMonth em uma função"
print(update_changes_5)
print()
print()


class activitiesmade:
    def __init__(self):
     pass
    activity_hour = datetime.today()
    print(activity_hour)


print()

class Register (activitiesmade):
    def __init__(self= activitiesmade):
       pass
    activity_registered = input("Bote a atividade que fez hoje:")
    activites_list = activity_registered
    print(activites_list)

print()

class FutureActivity:
   def __init__(self):
      pass
   future_activities = input("ponha o nome da atividade que ira realizar no futuro: ")
   print(future_activities)


print()

#Mudanças na FutureActivity subclasse no dia 16/06/2023#

class FutureActivityHour(FutureActivity):
   def __init__(self = FutureActivity):
      pass
   activity_datetime = str(input("digite a data e tempo da atividade:"))
   print(activity_datetime)
   

print()

class ActivityYearCalendar:
   def __init__(self):
      pass
   calendar.calendar(2023, 6)


print()


#Tranformaçao do ActivityMonth em uma função#

def ActivityMonth():
   print(calendar.prcal(2023, 6))


print()


#Implementação do weekheadr#

def Weekheader():
   print(calendar.weekheader(3))


print()


#Implementation of the Circadian Function at 15/06/2023#

print()

def currentlytime ():
    print("today:", datetime.today())
    print("now:", datetime.now())
    print("utcnow:", datetime.utcnow())


print()


def naptime ():
    print( "Sua hora de deitar e dormir é" ,22, 00, 00)

print()

def waketime ():
    print( "Sua hora de acordar é" , 5, 00, 00)

print()

