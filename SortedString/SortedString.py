#SortedString
#Created by Timothy Bollig
#9.28.2021

#This program takes a string of words separated by spaces as input and returns a string of the words sorted alphabetically ignoring case.

def sort_words(text):
    
    #split the words of the string into a list.
    unsorted_text_list = text.split()

    #Sort the items (words) in the list
    #Using key = str.casefold ignores case when sorting the words.  Normally, uppercase letters and words would be sorted before lowercase.
    sorted_text_list = sorted(unsorted_text_list, key = str.casefold)
    
    #Concatenate the words of the sorted list into a string with spaces
    sorted_results = ' '.join(sorted_text_list)
    
    return sorted_results