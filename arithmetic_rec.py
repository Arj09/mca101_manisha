def increment(num):
    num=num+1
    return num


def pred(num,i=0):
    x=increment(i)
    if num == 0 or num == 1:
        return 0
    elif x==num:
        return i
    else:
        i=x
        return pred(num,i)


def add(num1,num2):
    if num2==0:
        return num1
    else:
        return add(increment(num1),pred(num2))
    

def mult(num1,num2):
    if num2==1 :
        return num1
    elif num2==0 :
        return 0
    else:
       
       return add(num1,mult(num1,pred(num2)))
    

def subt(num1,num2):
    if num1 > num2 :
        
        if num2==0:
            return num1
        else:
            return subt(pred(num1),pred(num2))
    else:
        return subt(num2,num1)
    

def divide(num1,num2,count=0):

     if num1 < num2:
        return count
     else:
        count=count+1
        return divide(subt(num1,num2),num2,count)

def remainder(num1,num2):
    if num1 < num2:
        return num1
    else:
        
        return remainder(subt(num1,num2),num2)
    
        
    
