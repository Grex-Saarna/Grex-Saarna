#Gregori Saarna
#16.11.22
#Iseseisev töö
import random
import math
import datetime
"""
#Kuupäev
def minu (o):
    kuud = [" ","jaan", "veeb","marts","aprl","mai","juuni","juuli","august","sept","okt","novm","dec", ]
    return kuud[o]

def ilus (u):
    print(f"11.{u} 2022")

kp = input("Lisa kp: ")
p,k,a = kp.split(".")
ilus(minu(int(k)))

"""
#Mündid
ho=[]
fail = input("sisestage failinimi: ")
niga = open(fail)
for i in niga:
    ho.append(int(i.strip\n"))
"""
#Tervitused mõtisklustega
def tervitus(o):
    print('Võõrustaja: "Tere!"')
    print(f"Täna {o}. kord tervitada, mõtiskleb võõrustaja")
    print('Külaline: "Tere, suur tänu kutse eest!"')

arv = int(input("Sisestage külaliste arv: "))
for i in range(arv):
    tervitus(i+1)





#Peo eelarve
def eelarve(u):
    k = u*10+55
    return k


inimesed = int(input("Mitu inimest on kutsutud?: "))
print(eelarve(inimesed))
tuleb = int(input("Mitu inimest tuleb?: "))
print(eelarve(tuleb))


#Õunamahla tegemine
def mahlapakkide_arv(o):
    m = round(o*0.4/3)
    return m
x=int(input("Mitu KG õune on? ")) 
print(mahlapakkide_arv(x))


#banner
def banner(a):
    a=a.upper()
    return  a
print("!")
a=int(input("Mitu korda soovite reklaamilauset kuvada? "))
b=input("Mida soovite kuvada? ")
for i in range (a):
    print (b.upper())
    
#Tahvli juurde
k=input("Sisestage failinimi: ")
o=open(k)
opilased=[]
for i in o:
    opilased.append(o)
    
aeg = datetime.datetime.now()

#Jukebox 3.3
jrk = 1
a = input("Sisesta faili nimi: ")
ava = open(a)
for i in ava:
    print(f" {jrk}. {i} ", end="")
    jrk+=1
j = int(input("\nValige laulu järjekorra nr: "))
ava.close()
jrk = 1
ava = open(a)
for i in ava:
    if j==jrk:
        print(f"{i}. {jrk} ", end="")
    jrk+=1
ava.close()
#Sissetulekud
a = input("Sisesta faili nimi: ")
ava = open(a)
for i in ava:
    print(f"{i}, end="")
ava.close()
print("---------------------------------------------------------------")
#Jänesevanemate mure ver. 3
taisarv = int(input("Sisesta ringide arv "))
ring = 0
porgandid = 0
for i in range(taisarv):
    ring +=1
    if ring %2 == 0:
        porgand+=ring
print(f"porgandite koguarv on {porgand}")
print("------------------------------------------------------------------------------------------")
#ÜLIKOOLI VASTUVÕETUD
fail = open("rebased.txt", encoding="UTF-8")
vastused= []
aastad = [2011,2012,2013,2014,2015,2016,2017,2018,2019]
for rida in fail:
    vasuvoetud.append(int(rida))
aasta = int(input("Mis aastat soovid? "))
index= aastad.index(aasta)
print(index)
print(vastused)
file.close()
#Õunad
m= int(input("Mitu pöialpoissi tahad õunu? "))
u=0
for i in range(m):
    n=random.randint(1,2)
    print(n)
    u+=n
summa=14-u
print(f"Lumivalgekesele jäi {summa} ")
#taringud
taringud = int(input("mitu taringut tahad? "))
for i in range(taringud)
    print(random.randint(1,6))
    
    
#Male
nisuterad=0.5
a=int(input("Sisestage täisärv"))
i = 0
while i <a:
    i += 1
    
    nisuterad*=2
print(nisuterad)
#Murelikud lapsevanemad
ringid = int(input("mitu ringi jooksid"))
ring = 0
while ring  ringid:
    ring +=1
    if ring %2 == 0:
        porgand+=ring
print(f"porgandite koguarv on {porgand}")
    
#Aratus
aratus = int(input("mitu inimest on bussis: "))
for i in range(aratus):
    print("tõuse ja sära")
    
#Bussid
inimesed = int(input(" Inimeste arv: "))
kohad = int(input(" kohtade arv: "))
busse_vaja = inimesed/kohad
print(f"Busse on vaja {math.ceil(busse_vaja)}")
jaak = inimesed%kohad
if jaak==0:
    print(f"Viimases bussis on inimesi {kohad}") 
else:
    print(f"Viimases bussis on inimesi {jaak}")
    
#Tervitus
print("Tere Maailm!")
#Aasta liblikas
aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ". aasta liblikas on "
lause = str(aasta)+lause_keskosa+liblikas
print(lause)
#Pilved
pilv = int(input("Kuiu palju on pilvede aluse kõrgus (km)" ))
"""