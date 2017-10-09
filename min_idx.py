''' program to find index of minimum element in a sublist
given upper bound an lower bound'''
def min_index(list1,lower,upper,count):
    if(lower==upper):
        return count
    elif(list1[lower]>list1[lower+1]):
        count=lower+1
        return min_index(list1,lower+1,upper,count)
    else:
        return min_index(list1,lower+1,upper,count)


def minIndex(list1,lower,upper):
    return min_index(list1,lower=0,upper=len(list1)-1,count=lower)




