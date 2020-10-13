'''Write a program in python to print the Month name for the given month number. 
Input: Enter month number: 5 Output: It’s May'''
#create dictionary to store month no and month name
months = {
'1':'January',
'2' : 'February',
'3' : 'March',
'4' : 'April',
'5' : 'May',
'6' : 'June',
'7' : 'July',
'8' : 'August',
'9' : 'September',
'10' : 'October',
'11' : 'November',
'12' : 'December'
}
monthNo = input("Enter month number: ") #input month no
if monthNo in months:
    print("It's ", months.get(monthNo)) #get the month name by passing entered month number as the key name to the dictionary 
else:
    print("Enter a valid month number")

