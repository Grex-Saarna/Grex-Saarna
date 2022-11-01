#Gregori Saarna
#01.11.22
#harjutus07
import math

def kuup(a):
    print(f"kuubi ruumala on {a**3}")

def koonus(r, h):
    print(f"koonuse ruumala on {round((math.pi*r**2)*h/3,2)}")
    
def kera(v):
    print(f"kera ruumala on (round{4/3*math.pi*(v**2))}")

def silinder(r,h):
    print(f"Silindri ruumala on (round{math.pi*(r**2)*h)}")



print("************************************************* LEIAME RUUMALA ******************************************************")
loop = 1


while loop==1:
    print("Vali kujund : \n1.kuup \n2.Kera \n3.Koonus \n4.Silinder")
    kujund = int(input("Lisa number mis kujundit tahad, 1-4: "))
    if kujund==1:
        x = int(input("Sisesta kuubi külje pikkus: "))
        kuup(x)
    elif kujund==2:
        v = int(input("Sisesta kera raadius: "))
        kera(v)
    elif kujund==3:
        r = int(input("Sisesta koonuse põhja raadius: "))
        h = int(input("Sisesta koonuse kõrgus: "))
        koonus(r, h)
    elif kujund==4:
        r = int(input("Sisesta silindri ruumala: "))
        h = int(input("Sisesta silindri kõrgus: "))
        silinder(r,h)
        
        print("*********************************** YO vali mis kujundit tahad **************************************************")





"""
#oma funktsiooni loomine parameetriga
def tervita(a="unknown", b="ge"):
    if b=="et":
        print(f"Tere {a}")
    elif b=="en":
        print(f"Hi {a}")
    else:
        print(f"(Hallo {a}")
#funktsiooni väljakutsumine
tervita("mario", "et")
"""