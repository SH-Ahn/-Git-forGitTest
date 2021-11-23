print("Hello HS")
# 나 SH 원신 레벨 132 	#Let's python & commit. From Nov 22nd, 2021
#Hoesung's python ryouiki-tenkai Nov 23rd, 2021
def tenkai(yourHp, yourMp, yourPl, Hoesung_pythonlev, days):
    
    Hoesung_Hp = 10000
    Hoesung_Mp = 30000

    studentHploss = 5000
    studentMploss = 5000
    teacherHploss = 5000
    teacherMploss = 5000
    
    initial_yourHp = yourHp
    initial_yourMp = yourMp
    initial_HoesungHp = Hoesung_Hp
    initial_HoesungMp = Hoesung_Mp

    while yourPl < Hoesung_pythonlev:
        yourPl += (yourHp/1000) * (yourMp/5000) * (Hoesung_Mp/5000)
        yourHp -= studentHploss
        yourMp -= studentMploss
        Hoesung_Hp -= teacherHploss
        Hoesung_Mp -= teacherMploss

        if yourHp < studentHploss or yourMp < studentMploss or Hoesung_Hp < teacherHploss or Hoesung_Mp < teacherMploss:
            days = days+1
            yourHp = initial_yourHp
            yourMp = initial_yourMp
            Hoesung_Hp = initial_HoesungHp
            Hoesung_Mp = initial_HoesungMp

            if days % 20 == 0:
              print(f"python-ryouiki Day{days} ends")

        if yourPl > 10000:
          yourPl = 10000

    if days >= 1: 
        result1=f"Congrats.Your python level is now {int(yourPl)} level"
        result2=f"You worked hard for {days} days"
        result3="Take this sandwich for Hp & Mp recovery"
        print(result1, result2, result3, sep='\n')

def area(yourHp, yourMp, yourPl):

    Hoesung_pythonlev = 10000

    global days

    if yourPl <= Hoesung_pythonlev-5000: 
        print("Hoesung: Hey. Life is too short, you need Python!")
        tenkai(yourHp, yourMp, yourPl, Hoesung_pythonlev, days)
    elif Hoesung_pythonlev-5000 < yourPl < Hoesung_pythonlev:
        print("Hoesung: You will never stop. Not in a million years \n Hoesung: It's a great opportunity. I'll teach you. The real python") 
        tenkai(yourHp, yourMp, yourPl, Hoesung_pythonlev, days)
    else:
        print("Hoesung: Haha you know python well")

days = 0

student_hp, student_mp, student_python_level = map(int, input("System: Your Hp, Mp, and python level please?").split())

area(student_hp, student_mp, student_python_level)
