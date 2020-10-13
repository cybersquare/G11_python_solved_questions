# Write a python program to input names of ‘n’ employees and their basic . 
# Calculate house rent (30% of basic salary ) , 
# conveyance allowance(1% of basic salary), 
# PF(9% of basic salary) and 
# (gross salary = basic salary + house rent + conveyance allowance - PF). 
# Also display all the details.

# Function to calculate gross salary
def gross_salary(sal):
    salary = sal + 0.3*sal + 0.01*sal + 0.09*sal
    return salary

n = int(input('Eneter the number of employees: '))
employees = [] # employees = list()

# Input details
for i in range(0, n):
    name = input('Enter name of employee '+str(i+1)+ ': ' )
    salary = int(input('Enter salary of employee '+str(i+1)+': ' ))
    emp={'name': name, 'salary': salary}
    employees.append(emp)

# Print details
print('Name\t\t Gross salary\t\t ' )
for emp in employees:
    emp = employees[i]
    print('%s \t\t %.2f'%(emp['name'], gross_salary(emp['salary'])))



