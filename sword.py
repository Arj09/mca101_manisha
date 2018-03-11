def sword(n,last=0):
    if (len(n)==1):
        return n[0]
    else:
        rem=len(n)
        lastel=n[-1]
        if last==0:
            print("first will not killed")
            for i in range(1,(rem//2)+1) :
                n.pop(i)
        else:
            print("first will be killed")
            if rem%2!=0:
                for i in range(0,(rem//2)+1) :
                    #print("x")
                    n.pop(i)
            else:
                for i in range(0,(rem//2)) :
                    #print("x")
                    n.pop(i)
                
            
        print(n)
        #rem=len(n)
        if(lastel==n[-1]):
            last=1
        else:
            last=0
        sword(n,last)
people=int(input("enter te no of people in circular: "))
list1=[x for x in range(1,people+1)]
sword(list1)
