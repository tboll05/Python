#Factorial Finder
#Created by Timothy Bollig
#8.6.2021

#This program asks the user for input and then returns the factorial of the input.

while True:
    try:
        num = int(input("Please enter a positive integer."))
        
        if num >= 0:
            break
        else:
            print("Please enter a positive integer.")
            continue

    except ValueError:
        print("You did not enter an integer.  Please try again.")

if num == 0:
    print("Your answer is:",1)

else:
    result = num

    for x in range(1,num):
        result *= x

    print("Your answer is:",result)