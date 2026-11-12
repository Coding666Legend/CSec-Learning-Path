#!/bin/python3

#Variables and Methods
quote = "All is fair in love and war."
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #counts characters
print('\n')
name = "Heath" #string
age = 33 #int
gpa = 3.7 #float - has a decimal

print(int(age))
print(int(30.1))
print(int(30.9)) #Will it round? No!

print("My name is " + name + " and I am " + str(age) + " years old.")

age +=1
print(age)

birthday = 1
age += birthday
print(age)
