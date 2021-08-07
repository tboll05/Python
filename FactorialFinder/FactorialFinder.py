#Factorial Finder
#Created by Timothy Bollig
#8.6.2021

#This program asks the user for input and then returns the factorial of the input.

while True:
    try:
        num = int(input("Please enter an integer."))
        break

    except ValueError:
        print("You did not enter an integer.  Please try again.")

result = num

for x in range(1,num):
    result *= x

print(result)