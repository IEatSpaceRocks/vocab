import os
import random
import pygame

# Initialize Pygame
pygame.init()

# Constants
SCALE = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (128, 128, 128)
SCREEN = pygame.display.set_mode((SCALE, SCALE))

writing = False
writingcolour = BLACK
check = False


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

word1, word2 = database[sequence[0] + 1].strip().split(', ')

class Rectangle():

    def __init__(self, x, y, width, height):
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)
        self.hitbox = pygame.Rect(int(x), int(y), int(width), int(height))

    def draw_rectangle(self, colour):

        pygame.draw.rect(SCREEN, colour, self.hitbox)


class Text(Rectangle):

    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height)
        self.text = text
        self.hitbox = pygame.Rect(x, y, width, height)

    def draw_text(self, colour, textcolour, font):

        FONT = pygame.font.Font(None, int(font))
        pygame.draw.rect(SCREEN, colour, self.hitbox)
        SCREEN.blit(FONT.render(self.text, True, textcolour), FONT.render(self.text, True, textcolour).get_rect(center = self.hitbox.center))



background = Rectangle(0, SCALE/5, SCALE, SCALE)
setting = Rectangle(SCALE/30, SCALE/30, SCALE/30*4, SCALE/30*4)
customize = Rectangle(SCALE/30*25, SCALE/30, SCALE/30*4, SCALE/30*4)
language1 = Text(SCALE/30*6, SCALE/30, SCALE/30*18, SCALE/30*2, lang1)
language2 = Text(SCALE/30*6, SCALE/30*3, SCALE/30*18, SCALE/30*2, lang2)
line = Rectangle(0, SCALE/30*6, SCALE, SCALE/30)
word1 = Text(SCALE/30, SCALE/30*8, SCALE/30*28, SCALE/30*6, word1)
word3 = Text(SCALE/30, SCALE/30*15, SCALE/30*28, SCALE/30*6, '')
correct = Text(SCALE/30*2, SCALE/30*22, SCALE/30*11, SCALE/30*4, 'Correct!')
play = Rectangle(SCALE/30*15, SCALE/30*22, SCALE/30*4, SCALE/30*4)
left = Text(SCALE/30*21, SCALE/30*22, SCALE/30*7, SCALE/30*2, 'Words left:')
number = Text(SCALE/30*21, SCALE/30*24, SCALE/30*7, SCALE/30*2, str(len(sequence)))
end = Text(SCALE/30, SCALE/30*27, SCALE/30*5, SCALE/30*2, 'END')
scoretext = Text(SCALE/30*7, SCALE/30*27, SCALE/30*8, SCALE/30*2, 'SCORE:')
score = Text(SCALE/30*15, SCALE/30*27, SCALE/30*8, SCALE/30*2, '0/0')
percentage = Text(SCALE/30*25, SCALE/30*27, SCALE/30*5, SCALE/30*2, '100%')



def screen_update():

    SCREEN.fill(BLACK)
    background.draw_rectangle(PURPLE)
    setting.draw_rectangle(PURPLE)
    customize.draw_rectangle(PURPLE)
    language1.draw_text(WHITE, GRAY, SCALE/12)
    language2.draw_text(GRAY, WHITE, SCALE/12)
    line.draw_rectangle(BLUE)
    word1.draw_text(BLACK, WHITE, SCALE/6)
    word3.draw_text(writingcolour, BLUE, SCALE/6)
    correct.draw_text(WHITE, BLACK, SCALE/10)
    play.draw_rectangle(BLUE)
    left.draw_text(WHITE, BLACK, SCALE/120*7)
    number.draw_text(BLUE, WHITE, SCALE/12)
    end.draw_text(WHITE, BLACK, SCALE/12)
    scoretext.draw_text(BLACK, WHITE, SCALE/12)
    score.draw_text(WHITE, BLACK, SCALE/12)
    percentage.draw_text(BLACK, WHITE, SCALE/12)
    pygame.display.flip()

running = True
while running:

    # If the player closes the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if word3.hitbox.collidepoint(event.pos) and check == False:
                writing = not writing
            else:
                writing = False
            writingcolour = WHITE if writing else BLACK
            if end.hitbox.collidepoint(event.pos):
                running = False
            elif play.hitbox.collidepoint(event.pos):
                word3.text = ''
                check = False
        if event.type == pygame.KEYDOWN:
                if writing:
                    if event.key == pygame.K_RETURN:
                        print(word3.text)
                        word3.text = word2
                        check = True
                        writingcolour = BLACK
                    elif event.key == pygame.K_BACKSPACE:
                        word3.text = word3.text[:-1]
                    else:
                        word3.text += event.unicode

        
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