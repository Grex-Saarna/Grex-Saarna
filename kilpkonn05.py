#Gregori Saanra
#11.10.22
#harjutus02
import math



#kytusekulu arvutamine
km  = 400
L = 26
v = L/(km/100)
print(v)





#arvusüsteemid
a = int(input("sisesta täisarv: "))
print("2ndsysteemis:", bin(a))
print("16ndsysteemis:", hex(a))







#ajateisendus
aeg = int(input("sisesta minutid: "))
tunnid = aeg // 60 #täisarvuline jagamine
minutid = aeg % 60 #jääk
print("Vastus:",minutid,":",tunnid)





#hypotenuus
a,b = 16,9
c = round(math.sqrt(pow(a,2) + b**2),2)
print("Kolmunrga hüpo on:",c)




#rulluisutaja
kiirus = 29.9
aeg = 24
vastus = round(kiirus/60*aeg)
print("sportlane jõuab",vastus,"km")



#pitsa
#4.73 kogu summa
kogus = 3
hind = 12.90
tip = 0.1
summa =(hind+hind*tip)/kogus
print(kogus,"Iga tyyp maksab",summa,"eurot")



#toote hind
hind = 36.75
ale = 0.4
kogus = 3
summa = round((hind-hind*ale)*3,2)
print(kogus,"toote summa on",summa,"eurot")



#kolmnurga ümbermõõt
a,b,c = 5,5,5
p = a + b + c
print("kolmnurga ümbermõõt on: ", p)