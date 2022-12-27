import pygame
from pygame.locals import *
import random

def play():
  def textbox(msg, width, length, color): 
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(msg, True, black, color)
    textRect = text.get_rect()
    textRect.center = (X // width, Y // length)
    screen.blit(text, textRect)
    
  pygame.init()
  white = (255, 255, 255)
  black = (0, 0, 0)
  gray = (193,205,205)
  green = (102,205,0)
  red = (238,44,44)
   
  background_colour = (255,255,255)
  X = 600
  Y = 400
   
  screen = pygame.display.set_mode((X, Y))
  pygame.display.set_caption('guess the flag!')
      
  point = 0
  lives = 5
  
  guess = "click space to edit text..."
  pygame.init()
  font = pygame.font.Font(None, 50)
  
  flag_generator = True
  while flag_generator:
    canada = pygame.image.load("canadaflag.png")
    united_states = pygame.image.load("usaflag.png")
    argentina = pygame.image.load("argentinaflag.png")
    flag_list = [canada, united_states, argentina]
    
    flag_choice = flag_list.pop(random.randint(0,len(flag_list)-1))
    
    image = pygame.transform.scale(flag_choice, (200, 100))
    
    if flag_choice == canada:
      word = "canada"
    elif flag_choice == united_states:
      word = "america"
    elif flag_choice == argentina:
      word = "argentina"
      
    pygame.display.update()
    
    guessing = True
    while guessing and lives > 0:
      for evt in pygame.event.get():
          if evt.type == KEYDOWN:
            if evt.unicode.isalpha():
                guess += evt.unicode
            elif evt.key == K_SPACE:
              guess = guess[:-1000]
            elif evt.key == K_BACKSPACE:
              guess = guess[:-1]
            elif evt.key == K_RETURN:
                if guess == word:
                  point += 1
                  guess = "click space to edit text..."
                  guessing = False
                else:
                  lives -= 1

      if lives == 0:
        print("loser")
        pygame.quit()

      screen.fill((background_colour))
      rect = image.get_rect()
      rect = rect.move((200, 110))
      textbox("Name The Flag", 2, 6, gray)
      textbox("score: "+str(point), 8, 14, gray)
      textbox("lives: "+str(lives), 1.15, 14, gray)
      screen.blit(image, rect,)
      underline = pygame.draw.rect(screen, gray, pygame.Rect(150, 300, 300, 10))
      text = font.render(guess, True, (1, 1, 1))
      text_rect = text.get_rect()
      text_rect.center = (X // 2, Y // 1.45) 
      screen.blit(text, text_rect)    
      pygame.display.flip()

play()