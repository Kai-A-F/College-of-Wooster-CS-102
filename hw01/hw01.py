#Kai Francis

print("Question 1 (1 pt)")
# Print the result of 5 + 2 * 3 - 7 + 2 * 3 - 7. In a comment, explain how the answer was calculated.
print (5 + 2 * 3 - 7 + 2 * 3 - 7)
# I inputted the equation, in return, you get the answer printed
print("Question 2 (2 pts)")
# Print how many groups of 3 you can make from 13 people.
# (HINT: Does it make sense to have a fraction of a person in a group?)
group = 12/4+1
print(group)

print("Question 3 (1 pt)")
# Write a statement to save how much money you will make each month if you are paid $213,157 per year into a variable named profit.
profit = 213157/12
print(profit)

print("Question 4 (1 pt)")
# You are a kind soul who donates $100 to a local charity per month. Update the profit variable from Question 3 with how much
# money you will have after your donation.
# (HINT: profit is your monthly salary)
print(17763-100)

print("Question 5 (4 pts)")
# Write a statement that determines if your varible profit is an even number and print the result of the statement.
# In a comment, explain your answer.
print(profit-100)
num = 17663.083333333332
mod = num % 2
if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")
#based off of the previous problem, all i had to do was enter a if else statement 

print("Question 6 (2 pts)")
# Print a string that is 9 characters long using a string of no more than 3 characters ('aaa' is fine 'abced' is not).
str =('Kai')
print(str*3)

print("Question 7 (1 pts)")
# Print 3 to the power of 10
print (pow(3,10))

print("Question 8 (2 pts)")
# Print the square root of 985647
# (HINT: What is the square root as an exponent?)
sqrt = 985647 ** 0.5
print("square root:", sqrt)

print("Question 9 (1 pts)")
# Using each of the variables below only once,
#   print out: HelloHelloHelloHelloWorld! 
hello = 'Hello'
world = 'World!'
print(hello*4, end = world) 

print("Question 10 (5) pts)")
# Take the name in the variables below and print it out (exactly) as: last, first
# In a comment explain briefly who this person is and why she is important to computer science.
first = "Grace"
last = "Hopper,"
print(last,first)
#Hopper was involved in the creation of the first all-electronic digital computer. She invented the first computer program that translates instructions into codes that computers read directly.