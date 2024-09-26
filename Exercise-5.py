def is_strong_password(p):
  #initialize criteria flags
  hasUpper = False
  hasLower = False
  hasDigit = False
  hasSpecial = False
  specialCharacters = "#?!$"

  #Check each character in the password
  for char in p:
    if 'A' <= char <='Z':
      hasUpper = True
    elif 'a' <= char <= 'z':
      hasLower = True
    elif '0' <= char <= '9':
      hasDigit = True
    elif char in specialCharacters:
      hasSpecial = True 

  # Check if all options are met
  if len(password) >= 8 and hasUpper and hasLower and hasDigit and hasSpecial:
    return "Strong password"
  else:
    return "Weak password"

#taking password from the user
password=input("please enter an password: ")
print(is_strong_password(password))  
