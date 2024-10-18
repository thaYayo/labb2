# In a company the monthly salary of an employee is calculated by: 
# the minimum wage 400$ per month, plus 20$ multiplied by the number of years employed, plus 30$ for each child they have.

# Create a program that:

# Reads the number of years employed
# Reads the number of children the employee has
# Prints the total amount of salary the employee makes
# Output: "The total amount is 560$. 400$ minimum wage + 100$ for 5 years experience + 60$ for 2 kids"'

employedyears = int(input("Enter amount of years epmloyed: "))
amountchildren = int(input("Enter how many children you have: "))
yearsraise = employedyears * 20
childrenbonus = amountchildren * 30 
wage = 400 + childrenbonus + yearsraise

print(f"The total wage is {wage}$. 400$ minimum wage + {yearsraise}$ for {employedyears} years experience + {childrenbonus}$ for {amountchildren} kids")