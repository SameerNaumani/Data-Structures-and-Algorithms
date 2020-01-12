def bubbleSort(alist):
    #pass through entire list. numpass is which pass we are at
    # range(4,0,-1) because if we use 5 then i+1 is out of range.
    for numpass in range(len(alist)-1, 0, -1):
        #pass 5 times, 4 times, 3 ....
        for i in range(numpass):
            #if number on left side is greater than number on the right side then switch numbers
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

    return alist

        
            
#list []
lists = [1,5,2,6,3,7,4]
bubbleSort(lists)
print(lists)


