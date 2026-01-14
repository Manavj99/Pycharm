# Manav Jaiswal
# Assignment Day 1 and Day 2

# Personal Information
# •	Create variables to store:
# o	Your name
# o	Your age
# o	Your favorite number
# •	Print all the values in a single sentence.

name = "Manav"
age = 26
favorite_number = 7
print("My name is", name, "and I am", age, "years old and my favorite number is", favorite_number)  


# ________________________________________
# 2. Simple Calculations
# •	Create two variables with numbers.
# •	Print:
# o	Their sum
# o	Their difference
# o	Their product

a = 26
b = 15
print("The sum of", a, "and", b, "is", a+b)
print("The difference of", a, "and", b, "is", a-b)
print("The product of", a, "and", b, "is", a*b)
# 1. Student Profile
# A school wants to store student information in a program.
# •	Create variables for:
# o	Student name
# o	Grade
# o	Age
# •	Print a sentence displaying the student’s details.

student_name = "Manav"
grade = "A"
age = 26
print("The student's name is", student_name, "and the grade is", grade, "and the age is", age)
# ________________________________________
# 2. Shopping Bill Calculator
# A customer buys items from a store.
# •	Store the price of 3 different items in variables.
# •	Calculate and print the total bill amount.

item1_price = 10
item2_price = 20
item3_price = 30
total_bill = item1_price + item2_price + item3_price
print("The total bill amount is", total_bill)
# ________________________________________
# Loop Practice
# 3. Counting Numbers
# •	Use a for loop to print numbers from 1 to 10.

for i in range(1, 11):
    print(i)

# ________________________________________
# 4. Even Numbers
# •	Use a loop to print all even numbers between 1 and 20.

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# ________________________________________
# 5. Multiplication Table
# •	Ask the user to enter a number.
# •	Use a loop to print the multiplication table for that number (from 1 to 10).

number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number, "x", i, "=", number*i)

# 3. Daily Step Counter
# A fitness app tracks steps taken each day.
# •	Use a for loop to print the day number from 1 to 7.
# •	Display a message like:
# Day 1: 5,000 steps

for i in range(1, 8):
    print("Day", i, ": 5,000 steps")
# ________________________________________
# 4. Classroom Attendance
# A teacher wants to mark attendance for 10 students.
# •	Use a loop to print:
# Student 1: Present
# Student 2: Present
# ...

for i in range(1, 11):
    print("Student", i, ": Present")

# ________________________________________
# 5. Multiplication Table (Shop Prices)
# A shop owner wants to calculate the total cost when buying multiple quantities of an item.
# •	Ask the user for the price of one item.
# •	Use a loop to display the cost for quantities from 1 to 10.

price = int(input("Enter the price of the item: "))
for i in range(1, 11):
    print("The cost of", i, "items is", price*i)

# ________________________________________
# While Loop Practice
# 6. Sum of Numbers
# •	Use a while loop to calculate the sum of numbers from 1 to 50.
# •	Print the final sum.

sum = 0
for i in range(1, 51):
    sum += i
print("The sum of numbers from 1 to 50 is", sum)

# ________________________________________
# 7. Password Checker
# •	Set a correct password in a variable.
# •	Ask the user to enter a password.
# •	Keep asking until the correct password is entered.
# •	Print a success message.

correct_password = "123456"
password = input("Enter the password: ")
while password != correct_password:
    password = input("Enter the password: ")
print("Password is correct")

# ________________________________________
# 8. Number Guessing Game
# •	Store a secret number in a variable.
# •	Ask the user to guess the number.
# •	Use a loop until the correct number is guessed.
# •	Print how many attempts it took.

secret_number = 7
guess = int(input("Enter a number: "))
guess_count = 0
while guess != secret_number:
    guess = int(input("Enter a number: "))
    guess_count += 1
print("You guessed the number in", guess_count, "attempts")

# ________________________________________
# 6. Saving Money Tracker
# A person saves money daily.
# •	Start with ₹0 saved.
# •	Add ₹50 every day using a while loop.
# •	Stop when savings reach ₹1,000.
# •	Print the total days required.

savings = 0
day = 0
while savings < 1000:
    savings += 50
    day += 1
print("It took", day, "days to save ₹1,000")

# ________________________________________
# 7. Login System
# A website requires users to log in.
# •	Store a correct username and password in variables.
# •	Ask the user to enter them.
# •	Use a while loop until correct credentials are entered.
# •	Print a welcome message.

correct_username = "Manav"
correct_password = "123456"
username = input("Enter the username: ")
password = input("Enter the password: ")
while username != correct_username or password != correct_password:
    username = input("Enter the username: ")
    password = input("Enter the password: ")
print("Welcome to the website")

# ________________________________________
# Mini Project
# 8. Electricity Bill Calculator
# An electricity company calculates bills monthly.
# •	Ask the user for units consumed.
# •	Use variables and conditions:
# o	First 100 units → ₹5/unit
# o	Next 100 units → ₹7/unit
# •	Print the total bill.

units = int(input("Enter the units consumed: "))
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = 100 * 5 + (units - 100) * 7
print("The total bill is", bill)


