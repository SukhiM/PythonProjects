#Sukhdeep Singh
#sukhdeep.singh144@myhunter.cuny.edu

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("demo_boro.csv")

borough = input("Enter a Borough name: ")
output = input("Enter name of output file: ")


dk = df[(df['Borough'] == borough)]
dkk =dk['Total Enrollment']
dk["Grade K-6 Enrollment Fraction"] = (dk['Grade K']+dk['Grade 1']+dk['Grade 2']+dk['Grade 3']+dk['Grade 4']+dk['Grade 5']+dk['Grade 6'])/dk["Total Enrollment"]

print('minimum of total enrollment for ' + str(borough)+ ' is ' + str(dkk.min()) )
print('maximum of total enrollment for ' + str(borough)+ ' is ' + str(dkk.max()))
print('median of total enrollment for '+ str(borough)+ ' is '+ str(dkk.median()))
print('mean of total enrollment for ' + str(borough) +' is '+ str(dkk.mean()))
print('stand deviation of total enrollment for ' + str(borough)+ ' is '+ str(round(dkk.std(),3)))


dk.plot(x = "Year", y = "Grade K-6 Enrollment Fraction") 
plt.show()


fig = plt.gcf()
fig.savefig(output)


print(dk)

