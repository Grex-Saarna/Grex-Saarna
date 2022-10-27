#Gregori Saarna
#25.10.22
#Harjutus04

#ruutude tabel
print(f"Arv Ruut Kuup")
for i in range (1,11):
    print(f"{i:4} {i**2:4} {1**3:4}")
#pank
konto = 10000
intress = 0.05
periood = 5
for i in range (1,periood+1):
    print(f"{i} {round(konto,2)} {round(konto*intress,2)} {round(konto+konto*intress,2)}")
    konto = konto+konto*intress
print(f"Konto seis:{round(konto,2)}")
print(f"profit:{round(konto-10000,2)}")
#arvamismäng
loop = 1
skoor = 0
while loop==1:
    suvarv = random.randint(1,10)
    print(suvarv)
    for i in range(3):
        valik = int(input("Vali arv 1-10: "))
        if valik == suvaarv:
                  print("Winner")
                  break
            else:
                print("vale")
        loop = int(input("veel (1/0)? "))
print("gameover")
print(f"skoor {skoor}")
#viisikud
for i in range(1,100):
    if i%5==0:
        print(i)
#pisike korrutustabel
arv = 5
for i in range(1,11):
    summa = arv * i
    print(f"{arv}X{i}={summa}")
#paaris v paaritu
for i in range(1,11):
    if i%2==0:
        print(i,"paaris")
    else:
        print(i,"paaritu")
#loto
for i in range(5):
    suv = random.randint(0,9)
    print(suv, end="")
#tsükkel
arv = 5
for i in range (5):
    print("* " * arv)
    arv -=1
    
arv = 1
for i in range (5):
    print("* " * arv)
    #arv = arv + 1
    arv +=1
nr = 5
for m in range(nr):
    print("* "* nr)
#jalka tiim
vanus = 69
sugu = "m"
if vanus>=16 and vanus<=18 and sugu=="m":
    print("Sobib")
else:
    print("nah, ei sobi")
    
    
#Myyk
hind = 20
if hind<=10:
    ale = 0.1
else:
    ale = 0.2
    
summa = hind-hind*ale
print(f"Summa: {summa}£")
#Juubel
vanus = "15.01.2010"
aasta = 2022
p,k,a = vanus.split(".")
tema_vanus = aasta-int(a)
if tema_vanus%5==0:
    print("juubel")
else:
    print("ei ole juubel")
     
#matemaatika
nr1,nr2 = 8,6
tehe = input("vali tehe (* / + -):")
if tehe=="*":
    vastus = nr1 * nr2
elif tehe=="/":
    vastus = nr1 / nr2
else:
    vastus = "n/a"
print(f"{nr1}{tehe}{nr2}={vastus}")
print("----------------")
#RUUT
kas tegu on ruuduga?
a = int(input("Sisesta külg 1: "))
b = int(input("Sisesta külg 2: "))
if a==b:
    print(f"{a} ja {b} moodustavad ruudu")
    
else:
    print(f"{a} ja {b} moodustavad ristküliku")
