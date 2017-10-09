def flatter(list1,list2=[],count=0):
    if(count==len(list1)):
        return list2
    elif(type(list1[count])==list):
        #return flatter(list1[count],list2) this statement return flattened
        #list only upto first sublist that is found.
        list2=flatter(list1[count],list2)
        return flatter(list1,list2,count+1)
    else:
        list2.append(list1[count])
        return flatter(list1,list2,count+1)


