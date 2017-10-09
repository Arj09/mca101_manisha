def palindrome1(list1,i,j):
   
      
      if(i==j or i==j+1):
          print("list is palindrome")
          return True
      elif(list1[i]==list1[j]):
          return palindrome1(list1,i+1,j-1)
      else:
          print("list is not a palindrome")
          return False
def palindrome(list1):
    return palindrome1(list1,0,len(list1)-1)

