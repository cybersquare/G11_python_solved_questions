'''Write a program in python to print the following pattern from a given String: Input: CBSE 
Output: 
C 
BB 
SSS 
EEEE'''

str = input("Enter your string: ") #input string
i = 0 #initialize variable i
while i < len(str): #checks if i is less than the string size
    #print the first letter once
    if i == 0: 
        print(str[i])
    #print other letters  i+1 times
    else:
        print(str[i] * (i+1))
    i = i + 1

    
