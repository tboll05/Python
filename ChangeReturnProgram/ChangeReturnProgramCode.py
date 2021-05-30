#Created by Timothy Bollig
#5.30.21

#This program takes in the cost of an item and the amount of money given by the customer.
#It calculates how much change is due and how to break this down into Quarters, Dimes, Nickels, and Pennies.
#It displays these totals to the user.

#Take in the cost of an item
cost = float(input("Enter the cost of an item: "))

#Take in the amount of money being used to pay for item
money_given = float(input("Enter amount of money given: "))

#Calculate how much change is due
change_due = money_given - cost

#Break change into whole quarters
quarters = int(change_due // 0.25)
remaining_change = round(change_due - (quarters * 0.25),2)

#Break down remaining change into whole dimes
dimes = int(remaining_change // 0.10)
remaining_change = round(remaining_change - (dimes * 0.10),2)

#Break down remaining change into whole nickels
nickels = int(remaining_change // 0.05)
remaining_change = round(remaining_change - (nickels * 0.05),2)

#Break down remaining chnage into pennies
pennies = int(remaining_change * 100)

#Print output
print("Cost of item: ${:,.2f}".format(cost))
print("Money given: ${:,.2f}".format(money_given))
print("Change due: ${:,.2f}".format(change_due))
print()
print("Quarters:",quarters)
print("Dimes:",dimes)
print("Nickels:",nickels)
print("Pennies:",pennies)