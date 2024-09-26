def reverseString(s):
  reversed_str = ""

  for word in s:
    reversed_str = word + reversed_str

  return reversed_str

#taking input from user
user = input("please enter any word:")
print("Reversed string: ", reverseString(user))
