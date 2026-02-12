#Imports string package.
import string

#Variable to store name of the file.
file_name = "sample-file.txt"
#Creates a dictionary to store normalized lines.
lines_dict = {}

#Opens the file.
with open(file_name, "r") as file:
    #Loops through each line of the file and keeps track of line number.
    for num, line in enumerate(file, start = 1):

        #Removes line breaks and spaces.
        stripped = line.strip()

        #Skips empty lines.
        if stripped == "":
            continue

        #Converts line to lowercase.
        clean = stripped.lower()
        #Removes spaces.
        clean = clean.replace(" ", "")
        #Removes punctuation.
        clean = clean.translate(str.maketrans("", "", string.punctuation))

        #If clean line exists in dictionary, add to list.
        if clean in lines_dict:
            lines_dict[clean].append((num, stripped))
        #Else creates a new entry.
        else:
            lines_dict[clean] = [(num, stripped)]

#Creates list to store duplicate lines.
duplicate_lines = []

#Loops through dictionary values.
for v in lines_dict.values():
    #If one line appears more than once, add to list.
    if len(v) > 1:
        duplicate_lines.append(v)

#Prints number of near duplicate lines.
print("Number of near duplicate lines:", len(duplicate_lines))

#Prints first two near duplicate lines to user.
for s in duplicate_lines[:2]:
    print()
    for line_num, text in s:
        print(f"{line_num}: {text}")