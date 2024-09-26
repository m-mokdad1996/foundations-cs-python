def getEven():

  #Initialize an empty string to store the integers
  list_integers = []

  #Ask the user for the number of elements on the list
  n = int(input("how many integers you want: "))

  for i in range(n):
    integer = int(input("what is the integer you want to add: "))
    list_integers.append(integer)

  #Initialize an empty list to even numbers
  even_list = []

  for integer in list_integers:
    if (integer % 2 == 0): #check if the integer number is even
      even_list.append(integer)
  
  return even_list

#print the result
print(getEven())