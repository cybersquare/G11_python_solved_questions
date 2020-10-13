'''Write a program to count the number of words in a given String. 
Input: Hello this is my world Output: Number of Words = 5'''
string = input("Enter the string: ") #input string
# spilt function splits a string into a list where each word is a list item:
#then len function returns length of the list, that means, we get the words count
res = len(string.split()) 
# printing result 
print ("The number of words in string are : ", res) 
