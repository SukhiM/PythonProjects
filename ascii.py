#Sukhdeep Singh
#sukhdeep.singh144@myhunter.cuny.edu

mess = input("Enter a phrase: ")

print("letter ASCII two_letter_before")

for c in mess:
    character = c
    ASCII_code_of_character = ord(c)
    two_letter_before_current_character = chr(ASCII_code_of_character - 2) 
    print("%6c %5i %17c"%(character, ASCII_code_of_character, two_letter_before_current_character))