DATA221 - Assignment 2

Assignment2_Question1.py
Reads a text file, converts words to lowercase, removes punctuation from the beginning and end of each token, and keeps only tokens with at least two alphabetic characters. The program counts word frequencies using a dictionary and prints the ten most frequent words in descending order.

Assignment2_Question2.py
Reads a text file, converts words to lowercase, removes punctuation from the beginning and end of each token, keeps only tokens with at least two alphabetic characters, and then constructs bigrams. The program counts bigrams frequencies and prints the five most frequent bigrams in descending order.

Assignment2_Question3.py
Identifies near-duplicate lines in a text file. Each line is normalized by converting to lowercase and removing all whitespace and punctuation. Lines that become identical after normalization are grouped together. The program prints the number of near-duplicate sets and displays the first two sets with their original line numbers and text.

Assignment2_Question4.py
Loads student data from a CSV file into a pandas DataFrame and filters for students with high engagement based on study time, internet access, and low absences. The filtered results are saved to a new CSV file, and the program prints the number of students selected and their average grade.

Assignment2_Question5.py
Creates a new categorical column called grade_band based on students’ final grades (Low, Medium, High). The program groups the data by grade band and computes the number of students, average absences, and percentage of students with internet access, then the summary table is saved to a CSV file.

Assignment2_Question6.py
Analyzes crime data by creating a new column that classifies each row as HighCrime or LowCrime based on the violent crime rate. The program groups the data by this classification and calculates the average unemployment rate for each group, then prints the results.

Assignment2_Question7.py
Uses the requests and BeautifulSoup libraries to download and parse a Wikipedia page. The program extracts and prints the page title and the first paragraph from the main content area that contains at least 50 characters.

Assignment2_Question8.py
Scrapes a Wikipedia page to extract all valid section headings (h2 elements) from the main content area. Headings containing certain excluded words are ignored, and the remaining headings are cleaned and saved to a text file, one per line.

Assignment2_Question9.py
Scrapes a Wikipedia page to locate the first table with at least three data rows. The program extracts the table contents, assigns simple column names, and saves the structured data to a CSV file.

Assignment2_Question10.py
Defines a reusable function that searches a text file for lines containing a specified keyword (case-insensitive). The function returns the matching line numbers and text. The program tests the function on a sample file and prints how many matches were found along with the first three results.
