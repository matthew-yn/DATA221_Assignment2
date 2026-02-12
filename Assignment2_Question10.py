def find_lines_containing(filename, keyword):
    """
    Returns a list of (line_number, line_text) for lines that contain ←↩
    keyword
    (case-insensitive). Line numbers start at 1.
    """
    #Creates list to store matches.
    results = []
    #Opens the file.
    with open(filename) as file:
        #Counter to track line number.
        line_number = 1
        #Loops through each line in the file.
        for line in file:
            #Checks if keyword appears in the line.
            if keyword.lower() in line.lower():
                #Adds line number and text to results.
                results.append((line_number, line.strip()))
            #Increments line tracker.
            line_number += 1
    #Returns results list.
    return results

#Test function using sample-file.txt and lorem.
matches = find_lines_containing("sample-file.txt", "lorem")
#Prints number of matches found to user.
print("Matches found:", len(matches))
#Prints first three matches to user.
for item in matches[:3]:
    print(item)