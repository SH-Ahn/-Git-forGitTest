print("Hello HS")
#Let's python & commit. From Nov 22nd, 2021
#Hoesung's python ryouiki-tenkai Nov 23rd, 2021
def tenkai(yourHp, yourMp, yourPl, Hoesung_Hp, Hoesung_Mp, Hoesung_pythonlev, days, studentHploss, studentMploss, teacherHploss, teacherMploss):
    initial_yourHp = yourHp
    initial_yourMp = yourMp
    initial_HoesungHp = Hoesung_Hp
    initial_HoesungMp = Hoesung_Mp
    while yourPl < Hoesung_pythonlev:
        yourPl = yourPl+(yourHp/1000)*(yourMp/5000)*(Hoesung_Mp/5000)
        yourHp = yourHp- studentHploss
        yourMp = yourMp- studentMploss
        Hoesung_Hp = Hoesung_Hp- teacherHploss
        Hoesung_Mp = Hoesung_Mp- teacherMploss
        if yourHp < studentHploss or yourMp < studentMploss or Hoesung_Hp < teacherHploss or Hoesung_Mp < teacherMploss:
            days = days+1
            yourHp = initial_yourHp
            yourMp = initial_yourMp
            Hoesung_Hp = initial_HoesungHp
            Hoesung_Mp = initial_HoesungMp
            print(f"python-ryouiki Day{days} ends")
            continue 
    if days >= 1: 
        result1=f"Congrats.Your python level is now {yourPl}level"
        result2=f"You worked hard for {days}days"
        result3="Take this sandwich for Hp & Mp recovery"
        print(result1, result2, result3, sep='; ')
def ryouiki(yourHp, yourMp, yourPl):
    Hoesung_Hp = 10000
    Hoesung_Mp = 30000
    Hoesung_pythonlev = 10000
    global days
    studentHploss = 5000
    studentMploss = 5000
    teacherHploss = 5000
    teacherMploss = 5000
    if yourPl <= Hoesung_pythonlev-5000: 
        print("Hoesung: Hey. Life is too short, you need Python!")
        tenkai(yourHp, yourMp, yourPl, Hoesung_Hp, Hoesung_Mp, Hoesung_pythonlev, days, studentHploss, studentMploss, teacherHploss, teacherMploss)
    elif yourPl > Hoesung_pythonlev-5000 and yourPl < Hoesung_pythonlev:
        print("Hoesung: You will never stop. Not in a million years ") 
        print("Hoesung: It's a great opportunity. I'll teach you. The real python")
        tenkai(yourHp, yourMp, yourPl, Hoesung_Hp, Hoesung_Mp, Hoesung_pythonlev, days, studentHploss, studentMploss, teacherHploss, teacherMploss)
    else:
        print("Hoesung: Haha you know python well")


#30/3
#30//3
#30%3


days = 0
yourHp, yourMp, yourPl = input("System: Your Hp, Mp, and python level please?").split()
ryouiki(int(yourHp), int(yourMp), int(yourPl))