#Gregori Saarna
#25.10.22
#harjutus05













#õpilased
jrk = 1
opilased = ["Juhan","Kati","Maarja","Jamal","Juan"]
for i in opilased:
    print(f"{jrk}. {i}")
    jrk+=1
#küsi millist tahab muuta INT-korrigeerimine
nr = int(input("Vali nime mida muuta: "))
nr-=1
#milleks muudab 
opilane = input("Milleks muudate uwu: ")
#tee muudatus
del opilased[nr]
opilased.insert(nr, opilased)

print(opilased)
print("-------------------------------------------------------------------")

"""
#nimede lisamine loendisse


nimed = []
for i in range(5):
    nimi = input("lisa nimi loendisse: ")
    nimed.append(nimi)
nimed.sort()    
print(nimed)
print(f"viimati lisatud nimi: {nimed[-1]}")
"""