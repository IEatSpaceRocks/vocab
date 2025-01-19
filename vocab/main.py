import os
import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('database.txt', 'r') as file:
    db = file.readlines()

seq = list(range(len(db) - 1))
print(seq)
random.shuffle(seq)

lang1, lang2 = db[0].strip().split(', ')
print(f'Translating {lang1} to {lang2}.')

for i in range(len(seq)):
    word1, word2 = db[seq[i] + 1].strip().split(', ')
    print(word1, word2)
    