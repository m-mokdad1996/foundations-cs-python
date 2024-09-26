def getFactorial(s):
 factorial_number = 1 
 for i in range(1, s+1):
   factorial_number *= i
 return factorial_number

n =int(input("please enter a number"))
print(getFactorial(n))



  
