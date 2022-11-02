#Gregori Saarna
#Iseseisev töö
#02.11.22
import math

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
"""
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