#Imports string package.
import string

#Variable holds the name of the file.
file_name = "sample-file.txt"
#Creates a dictionary to store word/frequency pairs.
word_count = {}

#Opens the file in read mode.
with open(file_name, "r") as file:
    #Reads entire file, converting to lowercase, and splits into words.
    words = file.read().lower().split()
    #Loops through each word in the file.
    for word in words:
        #Removes punctuation.
        word = word.strip(string.punctuation)

        #Counter for alphabetic characters in the word.
        letter_count = 0
        #Loops through each character in the word.
        for char in word:
            #Checks if the character is a letter.
            if char.isalpha():
                letter_count += 1

        #Keeps words with at least two letters.
        if letter_count >= 2:
            #If word exists in dictionary, increment by one.
            if word in word_count:
                word_count[word] += 1
            #Else, add the word to dictionary with count of one.
            else:
                word_count[word] = 1

#Finds the 10 most frequent words from file.
top10 = sorted(word_count.items(), key = lambda item: item[1], reverse = True)[:10]
#Prints back to user.
print(top10)