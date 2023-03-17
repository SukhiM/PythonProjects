#Sukhdeep singh
#Sukhdeep.singh144@myhunter.cuny.edu


iS = input("Enter a string: ")
num = 0
base = 16
weight = 1
length = len(iS)
iSu = iS.upper()
print(iSu)
cH = [0,1,2,3,4,5,6,7,8,9]
HL = ["A","B","C","D","E","F"]

for i in range(length -1,-1,-1):
    ch = iSu[i]
    if ch.isdigit() and ch >= "0" and ch <= "9":
        num += weight * (ord(ch)-ord('0'))
    elif ch in HL:
        value = ord(ch) - ord('A') + 10 
        num += value * weight
    else:
        print("current letter " + str(ch) + " is not allowed in a hexadecimal string")
        exit()
    weight = weight * base 

print("num = " + str(num))
    