#Gregori Saarna
#23.11.2022

#3. Täringud
#kuvatakse korrektne arusaadav küsimus ja hiljem vastus
#kasutaja võistleb kahe täringuga arvuti vastu
#kasutaja teeb pakkumise ning suurima täringupunktisumma võitja saab laual oleva raha endale
#kogu looming salvestatakse tekstifaili
#kood kommenteeritud
import random

def xd():
    r = int(input("Sisestage panus millega sisened lauda: "))
    m = int(input("Sisesta zentoonide arv: "))
    p1 = random.randint(1, 12)
    p2 = random.randint(1, 12)
    print(p1,p2)
    print(r,m)
    
    if p1 > p2:
        print("Võitsid kõik laual olevad zetoonid endale")
        print(f"Kontol on {r+(m*2)}")
    
    elif p1 == p2:
        print("VIIK, said oma zetoonid tagasi")
        print(f"Kontol on {r}")
        
    else:
        print("Kaotasid kõik panustatud zetoonid ära")
        print(f"Kontol on {r-m}")
    



xd()