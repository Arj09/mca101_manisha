def myIncrement(number):
    '''
    Objective        : To compute the increment of given number.
    Input Variables  :
             number  : The number inputted by user.
    Return value     : Incremented value of given number.   
    '''
    #Approach        : Return number+1
    return number+1

tempNumber=0
def myPredecessor(value):
    '''
    Objective        : To find the predecessor of given value.
    Input Variables  :
             value   : integer - The number inputted by user.
    Return value     : Predecessor value of given number.   
    '''
    #Approach        : Use recursion.

    if value==0 or value==1:
        return 0
    else:
        if value==myIncrement(tempNumber):
            return tempNumber
        else:
            myIncrement(tempNumber)
            
            
