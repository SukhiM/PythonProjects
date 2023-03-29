#Sukhdeep Singh
#sukhdeep.singh144@myhunter.cuny.edu


import matplotlib.pyplot as plt
import numpy as np
 
choiceL = int(input("Enter 1 to get top left corner\n"+ "Enter 2 to get middle portion"))
if (choiceL == 1):
    print("Your choice: " + str(choiceL))
    inF =input("Enter file name: ")
    img = plt.imread(inF)
    height = img.shape[0]
    width = img.shape[1]
    img2 = img[:height//2:, :width//2]
    outF = input("Enter output file names:")
    plt.imsave(outF, img2)
elif (choiceL == 2):
    print("Your choice: " + str(choiceL))
    inR =input("Enter file name: ")
    imgR = plt.imread(inR)
    heightR = imgR.shape[0]
    WidthL = imgR.shape[1]
    imgR2 = imgR[heightR//4:heightR//4*3, WidthL//4:WidthL//4*3]
    outR= input("Enter output file name: ")
    plt.imsave(outR, imgR2)
else:
   print("Your Choice: " + str(choiceL))
   print("wrong choice")
   exit()


    





