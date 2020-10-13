# Write a Python program to accept the password from the user and to check the validity of a Password. 
# conditions for password validation : 
# Allows more than 8 characters. 
# The alphabets must be between [a-z] 
# At least one alphabet should be of Upper Case [A-Z] 
# At least 1 number or digit between [0-9]. 
# At least 1 character from [_ or $ ]. 
# Example: If the input is cybE7squ@re , 
# then the result is “Valid Password” 
# If the input is cybErsqu@re, then the result is “Invalid Password”

l, u, p, d = 0, 0, 0, 0
password = input('Please enter you password: ')
password = 'cybErsqu@re'
if (len(password) >= 8): 
    for letter in password: 
  
        # counting lowercase alphabets  
        if (letter.islower()): 
            l+=1            
  
        # counting uppercase alphabets 
        if (letter.isupper()): 
            u+=1            
  
        # counting digits 
        if (letter.isdigit()): 
            d+=1            
  
        # counting special characters 
        if(letter=='@'or letter=='$' or letter=='_'): 
            p+=1           
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)): 
    print("Valid Password") 
else: 
    print("Invalid Password") 