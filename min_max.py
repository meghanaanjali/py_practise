#func for finding min no

def min_no (numlist):
    min = numlist[0]
    for val in numlist :
        if val < min :
            min = val
    return min
    
#func for finding max no

def max_no (numlist):
    max = numlist[0]
    for val in numlist :
        if val > max :
            max = val
    return max

list1 = [4,5,7,-1,18,9]
print ("List = ", list1)
print ("Min = ", min_no(list1))
print ("Max = ", max_no(list1))
