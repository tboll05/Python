#Author: Timothy Bollig
#Date 9/21/2021
#This program takes in an integer as input and then returns a list of the prime factorization for that number.

def find_prime_factors(number):
    remaining = number
    increment = 2
    factors = []
    
    while True:
        
        #Check if increment evenly divides into number input; will be 0 if it does
        if remaining % increment == 0:
            factors.append(increment)
            remaining = remaining / increment
            
            #Will equal 1 when you reach the last prime factor 
            #This is because the last number to evenly divide into the remaining with be itsself divided by itself (7/7 = 1)
            if remaining == 1:
                break
        
        #It does not divide evenly.
        else:
            increment += 1
            
    return(factors)