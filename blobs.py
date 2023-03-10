#Sukhdeep Singh
#Sukhdeep.singh144@myhunter.cuny.edu

import turtle				#Import the turtle drawing package

turtle.colormode(255)		#Allows colors to be given as 0...255
tess = turtle.Turtle()		#Create a turtle
tess.shape("turtle")
tess.penup()		#Make it turtle shaped
tess.left(90)
tess.forward(300)
tess.left(180)
tess.pendown()			#Move her backwards, to give more space to draw

#For 0,10,20,...,250
for i in range(0,255,10):
     tess.forward(10)		#Move forward
     tess.pensize(i)		#Set the drawing size to be i (larger each time)
     tess.color(0,i,0)		#Set the red channel to be i (brighter each time)
     
for j in range(255,0,-10):
        tess.forward(10)
        tess.pensize(j)
        tess.color(0,j,0)


t=turtle.Turtle()
t.shape("turtle")
t.penup()
t.backward(100)
t.left(270)
t.pendown()

for j in range(0,255,10):
     t.forward(10)		#Move forward
     t.pensize(j)		#Set the drawing size to be i (larger each time)
     t.color(0,j,j)	
     
