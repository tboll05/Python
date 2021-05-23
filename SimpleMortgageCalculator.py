#Created by Timothy Bollig
#5.23.21

#Simple Mortgage Calculator Program
#This program calculates the monthly payments for a fixed term mortgage over given Nth terms at a given interest rate.

#Fixed Term Mortgage means that the loan has a fixed interest rate for the entire term of the loan

#Mortgage Payment Formula
#https://www.wallstreetmojo.com/mortgage-formula/

# Monthly Payment = P * r ((1+r)**n) / (((1+r)**n) - 1)

# P = Outstanding loan amount / Principal
# r = interest rate
# n = Total number of months for repayment


##########################################################################################################################
#Function that takes in principal loan amount, interest rate, and length of loan and returns the monthly payment amount.
##########################################################################################################################
def calculate_monthly_payment(principal, interest_rate, months):
    interest_rate /= 12.0
    
    monthly_payment = principal * (interest_rate * (1 + interest_rate)**months) / ((1 + interest_rate)**months - 1)
    
    return round(monthly_payment,2)


#Accept user input for variables
principal = input("Enter the Principal amount of the loan as a whole number: ")
interest_rate = input("Enter annual interest rate as a whole number: ")
months = input("Length of the loan in months as a whole number: ")

#Input validation to ensure user input integers for variables.
#Please note, if they did enter a float, casting will cause this to round down to the nearest number.
#I may revisit this code later for a better solution.
try:
    principal = int(principal)
except ValueError:
    principal = float(principal)
    principal = int(principal)
    
try:
    interest_rate = int(interest_rate)
    #Convert interest rate to a decimal (I.E. 7 becomes 0.07).
    interest_rate /= 100
except ValueError:
    interest_rate = float(interest_rate)
    interest_rate = int(interest_rate)
    #Convert interest rate to a decimal (I.E. 7 becomes 0.07).
    interest_rate /= 100
    
try:
    months = int(months)
except ValueError:
    months = float(months)
    months = int(months)
    
#Calculate monthly payment using created function.
monthly_payment = calculate_monthly_payment(principal, interest_rate, months)

#Format variables to currency for print out.
principal = "${:,.2f}".format(principal)
interest_rate = "{:.0%}".format(interest_rate)
monthly_payment = "${:,.2f}".format(monthly_payment)

print()
print()
print("Principal Loan Amount: " + principal)
print("Annual Interest Rate: " + interest_rate)
print("Length on Loan in Months: " + str(months))
print()
print("Total Expected Monthly Payments: " + monthly_payment)