#Palindrome
#Created by Timothy Bollig
#9.23.2021

#This program takes a string as input and returns a boolean of whether or not the string is a palindrome

def is_palindrome(text):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for item in text:
        if item in punctuation:
            text = text.replace(item,"")
    text = text.replace(" ","").lower()
    return text == text[::-1]