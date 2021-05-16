#This was a little side project that involved unzipping a file and reading directions on what to do.
#Once you unzip the file, you read the text using Python and learn that you have to search multiple file for a single phone number.
#In order to do this you have to use the os module and regular expressions for pattern matching.
#Some of the code has been altered to reflect a more streamlined approach based on the solution from Jose Portilla, the instructor of the Udemy course.

#Import needed modules.
import re, os, shutil

#Unzip instructions file that exists within the same directory.
shutil.unpack_archive('unzip_me_for_instructions.zip','puzzle_instructions','zip')

#Open the file in python to read it.
#Method based on Jose's code.
with open('extracted_content/Instructions.txt') as f:
    content = f.read()
    print(content)

#Iterate through all files in the extracted files and check each line for something matching the pattern of a phone #.
#When a match is found, append this to results.
#My original method.
results = []
pattern = r'\d{3}-\d{3}-\d{4}'

#full_path = 'C:\\Users\\bolli\\Advanced Python Bootcamp\\Advanced Python Udemy\\Advanced Module Puzzle\\puzzle_instructions\\extracted_content'
for folder, sub_folders, files in os.walk(os.getcwd()+'\\extracted_content'):
    for f in files:
        file_path = folder + '\\' + f
        file = open(file_path, 'r')
        for line in file:
            match = re.search(pattern,line)
            if match != None:
                results.append(match.group() + ' in ' + file.name)

results



#Open the file in python to read it.
#My original method.

#file = open('puzzle_instructions\\extracted_content\\Instructions.txt', 'r')

#for line in file:
#    line = line.rstrip('\n')
#    print(line)


#Method for search through text to find the pattern.  Based on Jose's code.

#def search (file, pattern = r'\d{3}-\d{3}-\d{4}'):
#    f = open(file,'r')
#    text = f.read()
#    if re.search(pattern,text):
#        return re.search(pattern,text)
#    else:
#        pass


#Jose's method for searching through the files.
#results = []

#for folder, sub_folders, files in os.walk(os.getcwd()+'\\extracted_content'):
#    for f in files:
#        full_path = folder + '\\' + f
#        results.append(search(full_path))