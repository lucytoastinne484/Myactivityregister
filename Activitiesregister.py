from datetime import datetime
from datetime import date


changes = date(2023, 6 , 11)
today_date = date.today()
print(changes)
print(today_date)

class activitiesmade:
    def __init__(self):
     pass
     date = str(input("digite o ano da atividade:  "))
     datetime = str(input("Digite o mes da atividade: "))
     activity = str(input("coloque o dia da atividade: "))
     actual_date = date + "/" + datetime + "/" + activity
     print(actual_date)


class Register (activitiesmade):
    def __init__(self= activitiesmade):
       pass
    activity_registered = input("Bote a atividade que fez hoje:")
    activites_list = activity_registered
    print(activites_list)



activitiesmade()
Register()
