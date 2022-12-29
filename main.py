import pygame
from pygame.locals import *
import random
import sqlite3

def Select (cursor, query, args=()):
 cursor.execute(query, args)
 records = cursor.fetchall()
 return records

sqliteConnection = sqlite3.connect('Highscore.db')
cursor = sqliteConnection.cursor()
  
cursor.execute('''SELECT count(name)
                 FROM sqlite_master
                 WHERE type='table'
                 AND name='Highscore';''')

if not cursor.fetchone()[0]==1:

  cursor.execute('''CREATE TABLE Highscore (
                             highscore INTEGER NOT NULL);''')
  sqliteConnection.commit()
  print("Highscore table created")
  
  recordsToInsert = ['0']
  
  cursor.executemany("""REPLACE INTO Highscore
                       (highscore)
                       VALUES (?);""", recordsToInsert)
  
  sqliteConnection.commit()

cursor.execute("""SELECT * from Highscore""")

sqlite_select_query = """SELECT highscore from Highscore"""

def play():
  def textbox(msg, width, length, color): 
    font = pygame.font.SysFont('Corbel', 35)
    text = font.render(msg, True, black, color)
    textRect = text.get_rect()
    textRect.center = (X // width, Y // length)
    screen.blit(text, textRect)

  def ending_screen():
    color_light = (170,170,170) 
    color_dark = (100,100,100) 
    
    screen = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('ending')
    screen.fill(background_colour)
    pygame.display.flip()
    ending_bg = pygame.image.load("ending.png")
    ending_bg = pygame.transform.scale(ending_bg, (X, Y))
  
    smallfont = pygame.font.SysFont('Corbel', 35) 
      
    quit_text = smallfont.render('quit' , True , gray) 
    play_text = smallfont.render('play again' , True , gray) 
      
    while True: 
          
        for ev in pygame.event.get(): 
              
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                  
            #checks if a mouse is clicked 
            if ev.type == pygame.MOUSEBUTTONDOWN: 
                  
                #if the mouse is clicked on the 
                # button the game is terminated 
                if X/3 <= mouse[0] <= X/3+200 and Y/2 <= mouse[1] <= Y/2+40: 
                  play()
                  
                elif X/3 <= mouse[0] <= X/3+200 and Y/1.5 <= mouse[1] <= Y/1.5+40: 
                  pygame.quit() 
                      
        # fills the screen with a color 
        screen.blit(ending_bg, (0, 0))
          
        # stores the (x,y) coordinates into 
        # the variable as a tuple 
        mouse = pygame.mouse.get_pos() 
          
        # if mouse is hovered on a button it 
        # changes to lighter shade 
        if X/3 <= mouse[0] <= X/3+200 and Y/2 <= mouse[1] <= Y/2+40: 
            pygame.draw.rect(screen,color_light,[X/3,Y/2,200,40]) 
        elif X/3 <= mouse[0] <= X/3+200 and Y/1.5 <= mouse[1] <= Y/1.5+40: 
            pygame.draw.rect(screen,color_light,[X/3,Y/1.5,200,40]) 
              
        else: 
            pygame.draw.rect(screen,color_dark,[X/3,Y/2,200,40]) 
            pygame.draw.rect(screen,color_dark,[X/3,Y/1.5,200,40]) 
          
        # superimposing the text onto our button 
        screen.blit(play_text, (X/2-55,Y/2)) 
        screen.blit(quit_text, (X/2-20,Y/1.5))
        s = [(point)]
        cursor.execute("""REPLACE INTO Highscore
             (highscore)
             VALUES (?);""", s)
        sqliteConnection.commit()
        records = Select(cursor, sqlite_select_query)
        high_score = (max(records)) 
        textbox("highscore: "+str(*high_score), 2, 2.6, gray)
          
        # updates the frames of the game 
        pygame.display.update() 
    
  pygame.init()
  black = (0, 0, 0)
  gray = (193,205,205)

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
        s = [(point)]
        cursor.execute("""REPLACE INTO Highscore
             (highscore)
             VALUES (?);""", s)
        sqliteConnection.commit()
        records = Select(cursor, sqlite_select_query)
        high_score = (max(records)) 
        ending_screen()
        
      records = Select(cursor, sqlite_select_query)
      high_score = (max(records)) 
      screen.fill((background_colour)) 
      main_bg= pygame.image.load("main_bg.png")
      main_bg = pygame.transform.scale(main_bg, (X, Y))
      screen.blit(main_bg, (0, 0))
      
      rect = image.get_rect()
      rect = rect.move((200, 110))
      textbox("Guess The Flag", 2, 6, gray)
      textbox("score: "+str(point), 8, 14, gray)
      textbox("lives: "+str(lives), 1.15, 14, gray)
      screen.blit(image, rect,)
      underline = pygame.draw.rect(screen, gray, pygame.Rect(150, 300, 300, 10))
      text = font.render(guess, True, (1, 1, 1))
      text_rect = text.get_rect()
      text_rect.center = (X // 2, Y // 1.45) 
      screen.blit(text, text_rect)    
      pygame.display.flip()
      pygame.display.update()

play()