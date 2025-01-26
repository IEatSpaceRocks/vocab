import os
import random
import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 600
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
FONT = pygame.font.Font(None, 50)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))


class Object():

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(x, y, width, height)

    def draw_object(self, colour):

        pygame.draw.rect(SCREEN, colour, self.hitbox)


class Text(Object):

    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height)
        self.text = text
        self.hitbox = pygame.Rect(x, y, width, height)

    def draw_text(self, colour, textcolour):

        pygame.draw.rect(SCREEN, colour, self.hitbox)
        SCREEN.blit(FONT.render(self.text, True, textcolour), FONT.render(self.text, True, textcolour).get_rect(center = self.hitbox.center))

# Changing the directory to the folder in which the .txt files and main.py are in
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# List the .txt files from the current directory
files = [file for file in os.listdir() if file.endswith('.txt')]
print(files)

# Opening the database.txt file in read mode, then reading every line separately to the db variable
with open('database.txt', 'r') as file:
    database = file.readlines()

# Making a list with numbers from 0 to n, where n is the number of wordpairs in the .txt, then shuffling it
sequence = list(range(len(database) - 1))
random.shuffle(sequence)

# Getting which 2 languages the current .txt file contains
lang1, lang2 = database[0].strip().split(', ')
print(f"Translating {lang1} to {lang2}.\nYou'll see words in {lang1}, type in their correct translation in {lang2}")


background = Object(0, HEIGHT/5, WIDTH, HEIGHT)
setting = Object(WIDTH/30, HEIGHT/30, WIDTH/30*4, HEIGHT/30*4)
customize = Object(WIDTH/30*25, HEIGHT/30, WIDTH/30*4, HEIGHT/30*4)
language1 = Text(WIDTH/30*6, HEIGHT/30, WIDTH/30*18, HEIGHT/30*2, lang1)
language2 = Text(WIDTH/30*6, HEIGHT/30*3, WIDTH/30*18, HEIGHT/30*2, lang2)
line = Object(0, HEIGHT/30*6, WIDTH, HEIGHT/30)
word1 = Object(WIDTH/30, HEIGHT/30*8, WIDTH/30*28, HEIGHT/30*6)
word2 = Object(WIDTH/30, HEIGHT/30*15, WIDTH/30*28, HEIGHT/30*6)
correct = Object(WIDTH/30*2, HEIGHT/30*22, WIDTH/30*11, HEIGHT/30*4)
play = Object(WIDTH/30*15, HEIGHT/30*22, WIDTH/30*4, HEIGHT/30*4)
left = Text(WIDTH/30*21, HEIGHT/30*22, WIDTH/30*7, HEIGHT/30*2, 'Words left:')
number = Object(WIDTH/30*21, HEIGHT/30*24, WIDTH/30*7, HEIGHT/30*2)
end = Text(WIDTH/30, HEIGHT/30*27, WIDTH/30*5, HEIGHT/30*2, 'END')
scoretext = Text(WIDTH/30*7, HEIGHT/30*27, WIDTH/30*8, HEIGHT/30*2, 'SCORE:')
score = Text(WIDTH/30*15, HEIGHT/30*27, WIDTH/30*8, HEIGHT/30*2, '0/0')
percentage = Text(WIDTH/30*25, HEIGHT/30*27, WIDTH/30*5, HEIGHT/30*2, '100%')



def screen_update():

    SCREEN.fill(BLACK)
    background.draw_object(PURPLE)
    setting.draw_object(PURPLE)
    customize.draw_object(PURPLE)
    language1.draw_text(WHITE, GRAY)
    language2.draw_text(GRAY, WHITE)
    line.draw_object(BLUE)
    word1.draw_object(BLACK)
    word2.draw_object(BLACK)
    correct.draw_object(WHITE)
    play.draw_object(BLUE)
    left.draw_text(WHITE, BLACK)
    number.draw_object(BLUE)
    end.draw_text(WHITE, BLACK)
    scoretext.draw_text(BLACK, WHITE)
    score.draw_text(WHITE, BLACK)
    percentage.draw_text(BLACK, WHITE)
    pygame.display.flip()

running = True
while running:

    # If the player closes the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen_update()

    pygame.time.Clock().tick(10)

'''
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
    
'''