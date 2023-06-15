from datetime import datetime
from datetime import date
import calendar

changes_1 = date(2023, 6 , 11)
uptade_changes_1 = "Criação do act register"
print(uptade_changes_1)
print(changes_1)


changes_2 = date(2023, 6 , 12)
uptade_changes_2 = "Implementação de calendarios"
print(uptade_changes_2)
print(changes_2)


changes_3 = date(2023, 6 , 13)
uptade_changes_3 = "Implementação do weekheader"
print(uptade_changes_3)
print(changes_3)


changes_4 = date(2023, 6, 14)
update_changes_4 = "Funçoes circadianas"
print(update_changes_4)
print(changes_4)




class activitiesmade:
    def __init__(self):
     pass
    activity_hour = datetime.today()
    print(activity_hour)


class Register (activitiesmade):
    def __init__(self= activitiesmade):
       pass
    activity_registered = input("Bote a atividade que fez hoje:")
    activites_list = activity_registered
    print(activites_list)



class FutureActivity:
   def __init__(self):
      pass
   future_activities = input("ponha o nome da atividade que ira realizar no futuro")
   print(future_activities)

class FutureActivityHour(FutureActivity):
   def __init__(self = FutureActivity):
      pass
   activity_year = str(input("digite o ano da atividade:"))
   activity_month = str(input("Digite o mes da atividade: "))
   activiy_day = str(input("Digite o dia da atividade: "))
   activity_hour = str(input("Digite a hora que a atividade sera realizada: "))
   activity_minute = str(input("Digite os minutos da atividade"))
   activity_datetime = activity_year + "/"  + activity_month + "/" + activiy_day , activity_hour + ":" + activity_minute
   print(activity_datetime)
   


class ActivityYearCalendar:
   def __init__(self):
      pass
   calendar.prcal(2023)


class ActivityMonth:
   def __init__(self):
      pass
   print(calendar.month(2023 , 6))

class Activityweekheader:
   def __init__(self):
      pass
   print(calendar.weekheader(1))


#Implementation of the Circadian Function at 15/06/2023#


def currentlytime ():
    print("today:", datetime.today())
    print("now:", datetime.now())
    print("utcnow:", datetime.utcnow())


def naptime ():
    print( "Sua hora de deitar e dormir é" ,22, 00, 00)

def waketime ():
    print( "Sua hora de acordar é" , 5, 00, 00)

currentlytime()
naptime()
waketime()

