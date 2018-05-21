list1 = [2,0,3,4,2,3,6,2,3]
dict1 = {}
print (list1)
for a_num in list1:
    if a_num in dict1:
        print(a_num,"is duplicated")
        break
    else:
        dict1[a_num] = True