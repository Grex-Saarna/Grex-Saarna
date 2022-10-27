#gregori Saarna
#27.10.2022
#harjutus06


#Minu fail
minu_fail = open("s6pru_l6ustaraamatus.txt", "r")

reformikad = 0
kesk = 0
erakonnad = []

for i in minu_fail.readlines():
    enimi,pnimi,er,palk = i.split(" ")
    if er=="RE":
        reformikad+=1
    elif er=="KE":
        kesk+=1
    if er not in erakonnad:
        erakonnad.append(er)
        
    with open("s6pruse_l6ustaraamatus.txt","a") as fail_sex:
        fail_sex.write(enimi+pnimi"\n")
        
print(f"reformikad kokku: {reformikad}")
print(f"kesksikuid kokku: {kesk}")
print(f"erakondi kokku: {len(erakonnad)}")

minu_fail.close