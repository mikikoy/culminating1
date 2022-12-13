import random

# library thatwe use in order to choose
# on random words from a list of words
 
#name = input("What is your name? ")
 
# Here the user is asked to enter the name first
 
import pygame
background_colour = (255,255,255)
X = 600
Y = 400
 
screen = pygame.display.set_mode((X, Y))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()

  
# Initialing Color
color = (255,0,0)
  
# Drawing Rectangle #(x,y, length, width)
#flag_box = pygame.draw.rect(screen, color, pygame.Rect(200, 140, 200, 110))
#flag_box.center = (X // 2, Y // 2)
pygame.display.flip()

#grab elements from the pygame interface
#infoObject = pygame.display.Info()

#create the display surface to grab the size of the pygame screen
#display_surface = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))



canada = pygame.image.load("canadaflag.png")
united_states = pygame.image.load("usaflag.png")
argentina = pygame.image.load("argentinaflag.png")

flag_list = [canada, united_states, argentina]

flag_choice = flag_list.pop(random.randint(0,len(flag_list)-1))
#image = pygame.transform.scale(image, (infoObject.current_w, infoObject.current_h))

image = pygame.transform.scale(flag_choice, (200, 100))
rect = image.get_rect()

rect = rect.move((200, 110))
screen.blit(image, rect)


if flag_choice == canada:
  word = "canada"
  print(word)
elif flag_choice == united_states:
  word = "united_states"
  print(word)
elif flag_choice == argentina:
  word = "argentina"
  print(word)

#display_surface.blit(image, (0, 0)) 

pygame.display.update()
