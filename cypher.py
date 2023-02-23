#Sukhdeep Singh
#Sukhdeep.singh144@myhunter.cuny.edu

PC = input("Enter a word: ")
newint = input("Enter a non-negative int to shift: ")
newPC = " "

for i in PC:

    offset = ord(i) - ord('A') + int(newint)
    wrap = offset % 26
    newChar = chr(ord('A') + wrap)
    newPC = newPC + newChar

    
print("Your word in code is", newPC)