def mergeSort(alist):
    #The list has to be atleast greater than 1
    if(alist>1):
        middle = alist//2
        leftHalf = alist[:mid]
        rightHalf = alist[mid:]

        #Recursively call merge sort on leftHalf and rightHalf until only 2 items are leftHalf
        mergeSort(leftHalf)
        mergeSort(rightHalf)
        merge(alist,leftHalf,rightHalf,middle)

# Merges two subarrays of arr[]. Makes a copy of the arrays 
# First subarray is arr[l..m] 
# Second subarray is arr[m+1..end] 
def merge(alist,leftHalf,rightHalf,middle):
    #leftHalf_index 
    i = 0
    #right_index 
    j = 0
    #middle_index
    k = 0

    # Go through both copies until we run out of elements in one
    while i < len(leftHalf) and j < len(rightHalf):
        # update midpoint
        if leftHalf[i] <= rightHalf[j]:
            alist[k] = leftHalf[i]
            i = i + 1
        else:
            alist[k] = rightHalf[j]
            





