def min_no (numlist):
    min = numlist[0]
    for val in numlist :
        if val < min :
            min = val
    return min

list1 = [4,5,7,-1,18,9]
print ("List = ", list1)
print ("Min = ", min_no(list1))