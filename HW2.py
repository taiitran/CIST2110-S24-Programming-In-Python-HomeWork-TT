# HW2.py
# Author: Tai Tran


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:

# If the age is less than 13, print "You are a child."
# If the age is between 13 and 19, print "You are a teenager."
# If the age is 20 or older, print "You are an adult."

age = input("Enter your age: ")
if int(age) < 13:
    print("You are a child.")
elif 13 <= int(age) <= 19:
    print("You are a teenager.")
else:
    print("You are an adult.")


# Question 2:
# Write some code to display the following pattern using a for or while loop:
# 1
# 12
# 123
# 1234
# 12345
    
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# Question 3:
# Write some code that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:

# The highest number.
# The lowest number.
# The average of all the numbers.

# Hint 1: You will need to use a for loop and a counter variable to keep track of the total sum of the numbers.
# Hint 2: You will need to use an if statement to keep track of the highest and lowest numbers.
    
total = 0
highest = 0
lowest = 0

for i in range(10):
    number = int(input("Enter a number: "))
    total += number
    if number > highest:
        highest = number
    if number < lowest:
        lowest = number
print("The highest number is", highest)
print("The lowest number is", lowest)
print("The average of all the numbers is", total / 10)



# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement

vowel = input("Write a string: ")
vowel = vowel.lower()
count = 0
for i in vowel:
    if i in "aeiou":
        count += 1
print("The number of vowels in the string is", count)

