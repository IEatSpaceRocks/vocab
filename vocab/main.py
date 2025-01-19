import os
import random

# Changing the directory to the folder in which the .txt files and main.py are in
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# List the .txt files from the current directory
txt = [file for file in os.listdir() if file.endswith('.txt')]
print(txt)

# Opening the database.txt file in read mode, then reading every line separately to the db variable
with open('database.txt', 'r') as file:
    db = file.readlines()

# Making a list with numbers from 0 to n, where n is the number of wordpairs in the .txt, then shuffling it
seq = list(range(len(db) - 1))
random.shuffle(seq)

# Getting which 2 languages the current .txt file contains
lang1, lang2 = db[0].strip().split(', ')
print(f"Translating {lang1} to {lang2}.\nYou'll see words in {lang1}, type in their correct translation in {lang2}")

# Main loop
for i in range(len(seq)):

    # Adding each word from the wordpairs to separate variables
    word1, word2 = db[seq[i] + 1].strip().split(', ')

    # Printing the first word
    print(word1)

    # The user can input a word. Checking if it's the correct translation or not and telling the user.
    word3 = input()
    if word2 != word3:
        print(f'Wrong! The correct translation was: {word2}')
    else:
        print('Correct!')
    
    