# Repeatedly calls generate and score while 100% of the letters do not match the target string
# If the letters are not correct then it will generate a whole new string.
# To make it easier to follow the program's progress it prints out the best
# string generated so far and its score every 10000 number of tries.

import turtle
import random

# modify width
# modify color so when branch length get very short make it green
# modify angle so that it is chosen at random between 15 and 45
# modify branchLen recursively so that you subtract by a random len each time


def tree(branchLen,t):
    if branchLen > 10:
        width = branchLen/10
        t.width(width)

        rightA = random.randrange(15,45) #Random angle generator
        leftA = random.randrange(15,45)
        leftLen = random.randrange(10,15) #Random length generator
        rightLen = random.randrange(10,15)

        t.forward(branchLen)
        t.right(rightA)
        tree(branchLen - rightLen,t)
        t.width(width - 1)
        t.left(rightA + leftA)
        tree(branchLen - leftLen, t)
        t.width(width - 1)
        t.right(leftA)
        if (branchLen > 25):
            t.color("brown")
        if (branchLen < 25):
            t.color("green")
        t.backward(branchLen)



def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()

#main()


#1
def power(x,n,acc=1):
    if(n==0):
        return 1 
    elif(n == 1):
        return x*acc
    else:
        return x * power(x, n - 1,acc)
        
#print(power(2,5))

#2
def powerH(x,n, acc = 1):

    if n == 0:
        return acc

    if n == 1:
        return acc * x

    elif n % 2 != 0:
        return powerH(x*x, (n - 1) // 2, acc * x)

    else:
        return powerH(x*x, n // 2, acc)

#print(powerH(2,5))


#3
def C(n,k):
    assert n>=0, "Does not work for n<0"
    assert k>=0 and k<=n, "Undefined for these values k<0 , k>n"
    if k == 0 or k ==n:
        return 1
    else:
        return C(n-1,k-1) + C(n-1,k)

#print(C(4,2))
#print(C(2,1))
#print(C(5,2))
#print(C)

