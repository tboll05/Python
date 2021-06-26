#First version of a statistics program.  Reads in data from a CSV file and then calculates and displays the summary statistics of the data set.
#Desired improvements include: allowing user input of file name, reading in from different file types, visualizing the data, using the Normal Distribution class, etc.

import csv, statistics

data = []

with open('SampleData.csv') as file:
    for value in csv.reader(file):
        data.append(float(value[0]))

while True:
    data_set_type = input("Enter Sample or Population for the type of data.")
    
    if data_set_type.lower() == 'sample' or data_set_type.lower() == 'population':
        break
        
mean = statistics.mean(data)
median = statistics.median(data)
mode = statistics.multimode(data)

#Check for no mode
mode_check = len(data)
if len(mode) == mode_check:
    mode = "No Mode"

#Check data set type to determine variance and standard deviation formulas
if data_set == "sample":
    standard_deviation = statistics.stdev(data)
    variance = statistics.variance(data)
else:
    standard_deviation = statistics.pstdev(data)
    variance = statistics.pvariance(data)

#Print statements
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
print("Standard Deviation:", round(standard_deviation,2))
print("Variance:", round(variance,2))