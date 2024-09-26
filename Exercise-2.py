def find_divisors():
  n = int(input("please enter a number: "))

# Initialize an empty list to store the divisors
  listDiv = []
 

  for i in range(1, n+1):
    if (n % i == 0): # Check if i is a divisor of num
      listDiv.append(i)
           
  return listDiv

# Call the function and print the result
print(find_divisors())

    

