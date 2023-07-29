from datetime import datetime
from datetime import date
import calendar
import time

#Import da biblioteca math 29/06/2023#




class activitiesmade:
    def __init__(self):
     pass
    activity_hour = datetime.today()
    print(activity_hour)

print()
print("--" * 10 + "--" * 10 )
print()

#A inserção da str method na Register subclasse no dia 21/06/2023#

class Register (activitiesmade):
    def __init__(self= activitiesmade):
       pass
    activity_registered = str(input("Bote a atividade que fez hoje:"))

print()
print("--" * 10 + "--" * 10 )
print()

#Implementação da subclasse Theactivityinprocess no dia 13/07/2023

class Theactivityinprocess(Register):
   def __init__(self):
      pass
   activity_in_process = str(input("Ponha a atividade que esta fazendo agora:  "))
   
print()
print("--" * 10 + "--"*10 )
print()

#Inserção da str na classe Future activity no dia 21/06/2023#

class FutureActivity:
   def __init__(self):
      pass
   future_activities = str(input("ponha o nome da atividade que ira realizar no futuro: "))
 
print()  
print("--" * 10)
print()

class activitiesmade2:
    def __init__(self):
     pass
    activity_hour = datetime.today()
    print(activity_hour)
    print("termino nas operações")



#Mudanças na FutureActivity subclasse no dia 16/06/2023#
# Mudanças na Future ActivityHour , removi a funçao print e botei o str method no dia 21/06/2023#
# Remoção da subclasse Activity Hour#
   
#transformação da ActivityYearCalendar em uma função em 13/07/2023#

def ActivityYearCalendar():
    calendar.prcal(2023, 7)



#Tranformaçao do ActivityMonth em uma função#

def ActivityMonth():
   print(calendar.prcal(2023, 6))




#Implementação do weekheadr#

def Weekheader():
   print(calendar.weekheader(3))



#Implementation of the Circadian Function at 15/06/2023#

print()

def currentlytime ():
    print("today:", datetime.today())
    print("now:", datetime.now())
    print("utcnow:", datetime.utcnow())


#upgrade at naptime function#
def naptime ():
   nap = "22h00"
   print("Quais são as horas?")
   time_now = str(input(""))
   print(time_now)
   
   if time_now == nap:
      print("É sua hora de dormir")
   else:
      print(datetime.now())
   
   
   

print()

def waketime ():
   print("Sua hora de acordar é as 07h00")


print()

#Implemenrtação de Resgister Contacts em 29/06/2023#

def RegisterContacts ():

   contact_dictonary = {"Lucia":11995787990, "Pai":11937570424 , "Tia Natalia":11959806459 , "Center Foto":11974564805 ,
   "CheckoutRH":11988779352 , "Marie":11945857596 , "Mamãe":11970572936 , "Christian":11942979138, "Aninha":11914332428}
   print("If you want a list of your contacts press y if not then press n: ")
   confirm_contactiter = str(input(""))
   
   if confirm_contactiter == "y":
      for contacts in range(contact_dictonary):
         print(contact_dictonary)
   else:
      print("The operation was cancelled")
      
      
   print("Do you want to know if someone is in your contact list?")
   confirm_choice = str(input(""))
   
   if confirm_choice == "y":
      print("Hang in there...")
      time.sleep(5)
   else:
      print("")
      
   print("Okay then please digit the number of the conntact without any character like \"-\" or \".\"  \n if you dont know the name of the contact please digit  0 and you can put the name:")
   
   
   verify_contactnumber =int(input(""))
   
   
   verify_contactname = str(input(""))
   
   if verify_contactnumber in contact_dictonary:
      print(verify_contactnumber, "The number exists")
   if verify_contactnumber  not in contact_dictonary:
      print("Sorry, i couldn't find it...")
   if verify_contactname in contact_dictonary:
      print(verify_contactname, "The name exists")
   if verify_contactname not in contact_dictonary:
      print("The name you put dont exist in the contacts list")
   
         
def donelist():
   print()
   print("Operações secundarias em execução")
   print()
   done_list = ["24/07/2023",
                "",
                "Estudei e codei Java " ,
                "",
                "25/07/2023",
                "", 
                "comprei os vegetais da minha lista",
                "",
                "fui no supermercado no dia ",
                "",
                "fazendo exercicios de JS e PHP ",
                "",
                "fui ao cinema assitir barbie",
                "",
                "descansei um pouco em casa depois de ter assitido barbie"
                "",
                "comecei a baixar o gimp e o inkescape",
                "",
                "Assiti um tutorial de como mexer no Krita"
                "",
                "Cuidei dos gatos",
                "",
                "Desenhei as ideias da minha lore",
                "",
                "26/07/2023",
                "",
                "Andei duas horas e me cansei pra caralho",
                "",
                "Comecei a recitar o mantra de invocação da Kali",
                "",
                "eu editei meu codigo no KanbanActivity,py",
                "",
                "comecei a aprender C#",
                "",
                "Fui carregar meus creditos do crtao de trasnporte",
                "",
                "Fui trabalhar",
                "",
                "Tomei a vacina em comprimido denovo ",
                "",
                "27/07/2023",
                "",
                " tomei minha creatina" ,
                "",
                "tomei café",
                "",
                "fiz uma aula de aerohiit e alguns exercicios fisicos",
                "",
                "comprei o mouse e um caderno pequeno pra anotar o que eu preciso",
                "",
                "fui cortar cabelo",
                "",
                "fui estudar no entanto acabei tendo que sair porque me irritei e irritei ",
                "",
                "por causa disso fui obrigada a ir sair um pouco e me acalmar , apesar disso houve brigas denovo entre meu pai e minha mãe , depois pedi desculpas a ela",
                "",
                "voltei a estudar java por volta das 17h",
                "",
                "fui recitar um mantra antes de dormir",
                "",
                "28/07/2023",
                "",
                "fui andar",
                "",
                "tomei pre treino e achei horrivel....",
                "",
                "tomei tambem whey protein pra ter mais musculo e uma reserva de energia",
                "",
                "estou indo desenvolver coisas em web",
                "",
                "trabalhei",
                "",
                "fiz o ritual diário antes de dormir",
                "",
                "29/07/2023",
                "",
                "tomei creatina e café",
                "",
                "depilei meu corpo com gilete",
                "",
                "fiz meus aquecimentos",
                "",
                "Recitei jai mata kali  jai mata durge kali durge namo namah kali durge namoh namah"
                "",
                "andei",
                "",
                """queria fazer meus  esquema de ganhar de ganhar dinheiro no tik toks 
                mas percebi que não posso gastar energia fisica demais senão me canso muito""",
                "",
                "comprei um creme hidratante",
                "",
                "voltei a editar",
                "",
                "fui trabalhar",
                "",
                "voltei do trabalho",
                "",
                "fiz meu ritual antes de dormir"
                "",
                "dormi"
                ]
   print()
   for done in done_list:
      print(done)
   print()
   
print()
print()   
print()
def goalsinprocess ():
    doing_list = ["Metas sendo feitas",
      "",           
      "Estudando Java, C# e triade web",
      "",
      "Estudando JS e PHP",
      "",
      "criando projetos pesssoais",
      "",
      "melhorar como pessoa",
      "",
      "cuidando do meu corpo agora em diante sem me esquecer",
      "",
      "estudando",
      "",
      "tarbalhando como jovem aprendiz num supermercado",
      "",
      "obtendo xp profissional conforme estou trabalhando",
      "",
      "buscando conhecimento",
      "",
      "meditando usando mantras para parar com vicios como H#nt41 e gula",
      "",
      "tomando medicação",
      "",
      "fazendo exercicios para emagrecer",
      "",
      """Divulgar meus convites do Tik Tok pra todo 
      mundo entrar com o link""",
      "",
      ]
    for goal in doing_list:
        print(goal) 
print()
print() 
print() 


def hastodolist ():   
   has_todolist = ["Lista do que fazer pra alcançar o que quero:",
                   "",
                   "Investir dinheiro em Tesouro Direto, CDB e etc.",
                   "",
                   "comprar uma bomba dágua pra minha mãe usar",
                   "",
                   "comprar um depilador pra me livrar dos pelos do meu corpo"
                   "",
                   "desenhar minhas ideias da minha lore que fiz", 
                   "",
                   "Fazer um exame de DNA na Genera pra descobrir se estou propensa a algo grave",
                   "",
                   "Começar a fazer investimentos denovo",
                   "",
                   "Iniciar um negócio de rifas e presentes ",
                   "",
                   "Divulgar meu negócio de presentes",
                   "",
                   "Ir num psicólogo ou terapeuta",
                   "",
                   "fazer pesquisa de mercado",
                   "",
                   "fazer propaganda sobre minhas rifas",
                   "",
                   "fazer propaganda na net dos meu negócio",
                   "",
                   "fazer publicidade com posters e cartazes sobre meus serviços que irei realizar",
                   "",
                   "analisar a minha empresa usando a matriz SWOT",
                   "",
                   "fazer minha cirurgia de transição",
                   "",
                   "fazer umas apostas de vez em quando",
                   "",
                   "conseguir parcerias tanto pro meu negócio quanto pra conteudo",
                   "",
                   "produzir conteúdo dos produtos que quero vender",
                   "",
                   "Investir em fundos de investimento",
                   "",
                   "investir no Tesouro Selic",
                   "",
                   "Criar conteúdo sobre programação",
                   "",
                   "Divulgar meus convites do Tik Tok pra todo mundo entrar com o link",
                   "",
                   ]
   
   for has in has_todolist:
      print(has)   

print()
print()
print()

def shortgoals():
   short_goals = ["Metas de curto prazo:",
      "",
      "Investir dinheiro em Tesouro Direto, CDB e etc.",
      "",
      "comprar uma bomba dágua pra minha mãe usar",
      "",
      "desenhar minhas ideias da minha lore que fiz",
      "",
      "comprar um depilador pra me livrar dos pelos do meu corpo",
      "",
      "comprar creme hidratante para minha pele",
      ]
   
   for short in short_goals:
      print(short)
print()      
shortgoals()
print() 
def mediumtimegoals():
   med_goals = ["metas de médio prazo",
            "",
            """Fazer um exame de DNA na Genera
            pra descobrir se estou propensa a algo grave""",
            "",
            "analisar a minha empresa usando a matriz SWOT",
            "",
            "fazer publicidade com posters e cartazes sobre meus serviços que irei realizar",
            "",
            "fazer propaganda na net dos meu negócio",
            "",
            ]
   for med in med_goals:
      print(med)
 
print() 
print() 
print()  
mediumtimegoals()
print()   
print()
print()
print() 
print()


def longtimegoals ():
   long_goals = ["metas de longo prazo",
                 "",
                 "Criar conteúdo sobre programação",
                 "",
                 "produzir conteúdo dos produtos que quero vender",
                 "",
                 "Divulgar meu negócio de presentes",
                 "",
                 "fazer minha cirurgia de transição",
                 "",
                 "conseguir parcerias tanto pro meu negócio quanto pra conteudo",
                 "",
                 "fazer propaganda sobre minhas rifas",
                 "",
                 "Iniciar um negócio de rifas e presentes ",]
   for long in long_goals:
      print(long)
 
print()  
print()  
longtimegoals() 
print()
print()  
print()  
def TierList():
   print("Define in the code what medias do you rank? based in the system a-f")
   print()
   dictonary_fudidoprakrai = {
      "TED2":"Rank C",
      "TED1":"rank C", 
      "Persona3Portable":"Rank S", 
      "SpaceJam o Legado":"Rank E",
      "Espetacular Spiderman":"Rank B",
      "The Boys":"Rank E",
      "BOF3 PSP Port":"Rank B",
     "She-ra reboot":"Rank B",
    "Danganronpa 1":"Rank B",
    "Danganronpa 2":"Rank D",
    "Crisis Core FFVII":"Rank S",
    "Persona 2 IS":"Rank A",
    "Persona 2 EP":"Rank A",
    "Persona 1 Remake":"Rank F",
    "Celeste":"Rank C",
    "Pizza Tower":"Rank C",
    "Megaman X4": "Rank A",
    "Megaman X5": "Rank D",
    "Megaman X6": "Rank E",
    "Megaman X7":"Rank F",
    "Megaman X Maverick Hunter": "Rank A",
    "Steins Gate PSP Release":"Rank B",
    "Idol Showdown":"Rank C",
    "The Murder of the Sonic the Hedgegog":"Rank B ",
    "Chrono Trigger":"Rank S",
    "FFVIII": "Rank C",
    "FFVII":"Rank A",
    "FFIX":"Rank S",
    "Kingdom Hearts Birth by Sleep":"Rank S" ,
    "FFT War of Lions":"Rank C",
    "Barbie (2023)":"Rank A",
    "BOF 4": "Rank D",
    "Guilty Gear Accent Core Plus":"Rank C" ,
    "Blazblue Continum Shift":"Rank B",
    "Tekken 6": "Rank B",
    "Street Fighter Alpha PSP": "Rank  C",
    "Minecraft(any version)": "Rank D",
    "FNF": "Rank D",
    "Cyberpunk 2077": "Rank D",
    "Mario Kart DS": "Rank B ",
    "Nascar PS2": "Rank B ",
    "Hot Shot Tennis": "Rank B",
    "Astro Boy the Video Game": "Rank B",
    "Mid Night Club DLC PS2": "Rank B "}
   print()
   dictonary_fudidoprakrai = list(dictonary_fudidoprakrai)
   for medias in dictonary_fudidoprakrai:
      print(medias)
 
print() 
print()   
print()
TierList()  
print()   
print()
print()
print(datetime.now())
   

      
      

         
      
      


      