#Sukhdeep Singh
#Sukhdeep.singh144@myhunter.cuny.edu

import turtle

def hexagramRecursion(t, n):
    
    if (n>0):
        t.forward(100)
        t.right(60)
        t.forward(100)
        t.left(120)
        hexagramRecursion(t,n-1)

def main():
    t = turtle.Turtle()
    hexagramRecursion(t,6)

if __name__ == '__main__':
    main()
    
        