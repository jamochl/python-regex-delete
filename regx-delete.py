#!/bin/env python3
# using regex module to parse, and os to delete
import re, os

# regex to match the error files located inside xml
regex = re.compile(r"""
    (?<=Configuration\ <em\ class="placeholder">) # The look behind for the xml error file
    .*?                                         # The error file itself, using non-greedy matching
    (?=</em>)                                   # The look ahead to close the xml tag
""", re.VERBOSE)

# input path of the error log (TODO change if stdin needed)
input_path = './testregex.txt'

# open filestream and read in content
file_input= open(input_path, 'r', encoding='utf-8')
file_text = file_input.read()

# Using compiled regex, send all found matches into a list
file_regexed = regex.findall(file_text)

# Remove duplicate files from the list
clean_file_regexed = list(dict.fromkeys(file_regexed))

# Print all matches
print(">  Files parsed for error")
print(clean_file_regexed)

# ---------------------------------
# FOR TESTING TOUCH ALL FILES FIRST
print(">  Touching files for test")
for file in file_regexed:
    f = open(file, "w")
    f.close()


print(">  Current directory")
print(os.listdir())
# ---------------------------------

# Iterate over list, deleting as we go
for file in clean_file_regexed:
    os.remove(file)


# ---------------------------------
# FOR TESTING DISPLAY dir
print(">  Directory after")
print(os.listdir())
# ---------------------------------
