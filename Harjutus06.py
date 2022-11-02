#gregori Saarna
#17.10.22
#Harjutus03


#palindroom
def isPalindrome(s):
    return s == s[::-1]
 
s = "PEEP"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")




    
#tundide ajad
algus = "8:30"
lopp = "14:15"

hh1,mm1 = algus.split(":")#teen teksti pooleks
minutid1 = int(hh1)*60+int(mm1)#teisendan minutiteks
hh2,mm2 = lopp.split(":")
minutid2 = int(hh2)*60+int(mm2)

minutid = minutid2-minutid1	#ajavahe
hh = minutid//60#täisarvuline teisendamine
mm = minutid%60 #jääk

print(f"Ajaline vahe {hh}:{mm}")

"""
#emaili kontroll
email = input("Sisesta oma email kontrollimiseks: ")
print("@" in email)



#vandumine - teksti asendamine
v = input("Vannu siia 'Kurat küll!': ")
print(v.lower().replace("kurat","***"))





#korralik nimi
nimi = input("Sisestanimi: ")
puh_nimi = nimi.strip().capitalize()
print("tere,", puh_nimi+"!")
"""
