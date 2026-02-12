#Imports string package.
import string

#Variable holds the name of the file.
file_name = "sample-file.txt"
#Creates list to store valid words.
tokens = []

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
            #Adds word to the end of the list.
            tokens.append(word)

#Creates dictionary to store bigram/frequency pairs.
bigrams_count = {}

#Loops through each valid word in the file.
for i in range(len(tokens) - 1):
    #Creates bigrams.
    pair = tokens[i] + " " +tokens[i + 1]
    #Tf bigram is in the dictionary, increment by one.
    if pair in bigrams_count:
        bigrams_count[pair] += 1
    #Else, add bigram to dictionary with count of one.
    else:
        bigrams_count[pair] = 1

#Finds the 5 most frequent bigrams.
top5 = sorted(bigrams_count.items(), key = lambda item: item[1], reverse = True)[:5]
#Prints back to user.
print(top5)