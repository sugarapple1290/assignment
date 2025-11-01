#Task 1
# Score and earned points
Score = 450
earned = 439  

# Update the score using assignment operator
Score += earned

print("The final score of the player is",Score,)




#Task 2


#User Input
employee= input("Enter employee name:")
salary = float(input("Enter base salary:"))
bonuspercentage = float(input("Enter bonus percentage:"))

# Calculate users bonus
bonus_amount = salary * (bonuspercentage / 100)

# Add bonus to salary using assignment operator
salary += bonus_amount


print("The total salary of "+ employee + " is " + str(salary))

if salary > 5000:
    print("High Earner")
else:
    print("Standard Earner")

#Task3


#Total pg and pages Read
total= 500
Read = 50


days = total/ Read

# Print Statement
print("It would take " + str(days) + " days")

#Task 4



# Users inputs
Item_name = input("Enter item name: ")
Item_price = float(input("Enter item price: "))
Quantity = int(input("Enter quantity: "))

# Assignment operator
Total_bill = Item_price * Quantity

# 10% discount if bill > 500
if Total_bill > 500:
    discount = Total_bill * 0.10
    Total_bill -= discount  

# Print statement
print("The final amount for " + Item_name + " is " + str(Total_bill))


#Task5


# Take inputs as strings
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Converting strings to integers
num1 = int(num1)
num2 = int(num2)

# Addition
add = num1
add += num2
print("addition:" + str(add))

# Subtraction
sub = num1
sub-= num2
print("subtraction: " + str(sub))

# Multiplication
multiplication = num1
multiplication *= num2
print("Multiplication: " + str(multiplication))
