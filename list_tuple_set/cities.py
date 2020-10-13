# Write a function display(cities) that takes a list of cities as a parameter and 
# print only those cities which are beginning with alphabet ‘M’ only. 

n = int(input('Enter number of cities: '))

cities = list()

for i in range(0, n):
    city = input('Enter name of city '+str(i+1)+': ')
    cities.append(city)

for city in cities:
    if(city.startswith('M')):
        print(city)
