# Repeatedly calls generate and score while 100% of the letters do not match the target string
# If the letters are not correct then it will generate a whole new string.
# To make it easier to follow the program's progress it prints out the best
# string generated so far and its score every 10000 number of tries.

from __future__ import division
import random 
import matplotlib.pyplot as plt


def generate(lenS, lenA, alphabet):
    result = ""
    for i in range(lenS):
        # Choose a random item from a range (randrange). This will pick a random index from alphabet
        result = result + alphabet[random.randrange(lenA)]
    
    return result

def generateOne():
    alphabet= list("abcdefghijklmnopqrstuvwxyz ")
    result = ""
    result = alphabet[random.randrange(len(alphabet))]
    return result

def calcScore(string, goal):
    numSame = 0
    if goal == 0:
        return
    for i in range(len(goal)):
        if string[i] == goal[i]:
            numSame = numSame + 1
    
    return (float(numSame)/len(goal)) * 100


def monkeyTypist():
    target = list("methinks it is like a weasel")
    lenS = len(target)
    alphabet= list("abcdefghijklmnopqrstuvwxyz ")
    lenA=len(alphabet)
    epoch = 0
    
    # Generate original string and get the score
    bestStr = generate(lenS, lenA, alphabet)
    bestScore = calcScore(bestStr, target)
    
    print("String   Score  Try")
 
   # While loop        
    while bestScore <= 100:
        #if best Score is achieved print out the score and which try
        if bestScore == 100:
            x = epoch
            y = bestScore
            plt.scatter(x,y)
            print("%s    %f" % ("".join(bestStr),bestScore),  epoch)
            break    
       
        #Lock in characters that already match
        newStr = ""
        for i in range(lenS):
            if bestStr[i] == target[i]:
                newStr += bestStr[i]
            else:
                newStr += generateOne()
        
                
        #newStr = generate(lenS, lenA, alphabet)
        newScore = calcScore(newStr, target)
        
        if newScore > bestScore:
            bestScore = newScore
            bestStr = newStr
            
        
        #if epoch == 100000:
         #   print("%s    %f" % ("".join(bestStr),bestScore))
          #  epoch = 0
            
        # Check score every 100 tries
        if epoch % 100 == 0:
            x = epoch
            y = bestScore
            plt.scatter(x,y)
            print("%s    %f" % ("".join(bestStr),bestScore),  epoch)
        
        epoch = epoch + 1
    
    plt.xlabel("Iterartion")
    plt.ylabel("Score")
    plt.show()

    