import pygame
from pygame.locals import *
import random

def play():
  def checking():
    if guess == word: 
      print("correct")
      play()
    if guess != word:
      print("guess again")

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
  pygame.display.set_caption(' guess the flag! ')
      
  canada = pygame.image.load("canadaflag.png")
  united_states = pygame.image.load("usaflag.png")
  argentina = pygame.image.load("argentinaflag.png")
  
  flag_list = [canada, united_states, argentina]
  
  flag_choice = flag_list.pop(random.randint(0,len(flag_list)-1))
  
  image = pygame.transform.scale(flag_choice, (200, 100))
  rect = image.get_rect()
  rect = rect.move((200, 110))
  
  
  if flag_choice == canada:
    word = "canada"
  elif flag_choice == united_states:
    word = "america"
  elif flag_choice == argentina:
    word = "argentina"
  
  pygame.init()
  screen = pygame.display.set_mode((X, Y))
  guess = "click space to edit text..."
  font = pygame.font.Font(None, 50)
  while True:
      for evt in pygame.event.get():
          if evt.type == KEYDOWN:
            if evt.unicode.isalpha():
                guess += evt.unicode
            elif evt.key == K_SPACE:
              guess = guess[:-1000]
            elif evt.key == K_BACKSPACE:
                guess = guess[:-1]
            elif evt.key == K_RETURN:
                checking()
            elif evt.type == QUIT:
              break
      screen.fill((background_colour))
      textbox("Name The Flag", 2, 6, gray)
      screen.blit(image, rect,)
      box = pygame.draw.rect(screen, gray, pygame.Rect(150, 300, 300, 10))
      block = font.render(guess, True, (1, 1, 1))
      text_rect = block.get_rect()
      text_rect.center = (X // 2, Y // 1.45) 
      screen.blit(block, text_rect)
      pygame.display.flip()

play()