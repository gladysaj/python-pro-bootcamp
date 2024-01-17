#Day 1: Working with variables in python to manage data

print("Hello Python!")

#creating multiple lines
print("Hello World!\nHello Gladys!\n")

#string concatenation
print("Hello" + " " + "Glad")

#fixing the code exercise
print("Day 1 - String Manipulation")
print("String Concatenation is done with the " + '"+"' + " sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#getting user input / function
input("What is your name? ")
print("Hello " + input("What is your name? "))

#multiplying inputs
num1 = int(input())
num2 = int(input())
print(num1 * num2)

# Provide any name in the input to count the length of the name.
# That value can be accessed using the input() function.
name = input()
print(len(name))

#python variables - switching values
a = input()
b = input()

ax = b
bx = a

a = ax 
b = bx
# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
