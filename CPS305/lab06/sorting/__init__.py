#Implement the median-of-three method (see Section 5.12 of the textbook) 
# for selecting a pivot value as amodification to quickSort (ame this function mo3_quickSort). 
# Prepare test cases for your mo3_quickSort

def mo3_quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
    #find middle index
    middleindex = median(alist,first,last,(first+last)//2)
    #print(middleindex)
    #swap first element with the pivot value chosen
    alist[first],alist[middleindex] = alist[middleindex],alist[first]
    
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

# Implement median
def median(alist, first, last, middle):
    if alist[first] < alist[last]:
        return last if alist[last] < alist[middle] else int(middle)
    else:
        return first if alist[first] < alist[middle] else int(middle)
    
    
    
#Original Quick Sort
def quickSort(alist):
    quickSortHelper2(alist,0,len(alist)-1)

def quickSortHelper2(alist,first,last):
    if first<last:
        splitpoint = partition2(alist,first,last)
        quickSortHelper2(alist,first,splitpoint-1)
        quickSortHelper2(alist,splitpoint+1,last)


def partition2(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp


    return rightmark

