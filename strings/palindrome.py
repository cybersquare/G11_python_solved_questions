#program to find the palindrome of a string
#palindrome ex: 'level', 'malayalam'
string = input("enter your string:") #input your string
string = string.lower() #string converted to lowercase. Because palindrome is not case sensitive.
reverse = string[::-1] #reverse string
if reverse == string: #checks if reversed string is same as original string
    print("The string is a palindrome") #prints if it is same
else:
    print("The string is not a palindrome") #prints if it is not same

    


