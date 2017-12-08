def change(str1):
    str11 = str1[len(str1)-3:len(str1)]
    if(str11 == "ing"):
        str1=str1+'ly'
      #  print(str1)
    else:
        str1 = str1+'ing'
        
    return str1


def main():
    str = input("Enter String : ")
    if(len(str)<3):
        print(str)
    else:
        print(change(str))
        
if __name__=='__main__':
    main()
    
