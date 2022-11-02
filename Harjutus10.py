#Gregori Saarna
#02.11.22
#Harjutus10
import re


#kuva normaalsed aadressid
import re

fh = open("lorem.txt")
for line in fh:
    if re.search("^[Z-Z0-9]+[A-Z]{1}", line):
         print(line,end="")

print("--------------------------")

#kuva normaalsed paroolid
         
import re

fh = open("lorem.txt")
for line in fh:
    if re.search("^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$", line):
         print(line,end="")  
