import os
import random

# Changing the directory to the folder in which the .txt files and main.py are in
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Opening the database.txt file in read mode, then reading every line separately to the db variable
with open('database.txt', 'r') as file:
    db = file.readlines()

# Making a list with numbers from 0 to n, where n is the number of wordpairs in the .txt, then shuffling it
seq = list(range(len(db) - 1))
random.shuffle(seq)

# Getting which 2 languages the current .txt file contains
lang1, lang2 = db[0].strip().split(', ')
print(f'Translating {lang1} to {lang2}.')

# Printing out the wordpairs from the .txt separately and in random order
for i in range(len(seq)):
    word1, word2 = db[seq[i] + 1].strip().split(', ')
    print(word1, word2)
    