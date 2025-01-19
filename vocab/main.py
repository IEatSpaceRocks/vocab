import os
import random

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('database.txt', 'r') as file:
    db = file.readlines()

seq = list(range(len(db)))
random.shuffle(seq)

for i in range(len(seq)):
    word1, word2 = db[seq[i]].strip().split(', ')
    print(word1, word2)
    