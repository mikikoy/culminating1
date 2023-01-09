import pygame
from pygame.locals import *
import random
import sqlite3
#notes: add function for adding flags maybe?, add incorrect image, add the correct answer if they lose 

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
white = (255, 255, 255)
black = (0, 0, 0)
gray = (193,205,205)

background_colour = (255,255,255)
X = 600
Y = 400
pygame.init()

def instruction():
  def button(msg,len,l,wid,w):
    smallfont = pygame.font.SysFont('Corbel',35)
    button = smallfont.render(msg , True , gray)
    screen.blit(button, (X/len+l,Y/wid+w))   
    pygame.display.update() 
  
  screen = pygame.display.set_mode((X, Y))
  pygame.display.set_caption('ending')
  screen.fill(background_colour)
  pygame.display.flip()
  intro_bg = pygame.image.load("instructions.png")
  intro_bg = pygame.transform.scale(intro_bg, (X, Y))
  
  color_light = (170,170,170) 
  color_dark = (100,100,100) 


  smallfont = pygame.font.SysFont('Corbel',35) 
  
  exit_button = smallfont.render('X' , True , gray)

    
  while True: 
        
      for ev in pygame.event.get(): 
            
          if ev.type == pygame.QUIT: 
              pygame.quit() 
                
          #checks if a mouse is clicked 
          if ev.type == pygame.MOUSEBUTTONDOWN: 
                
              #if the mouse is clicked on the 
              # button the game is terminated 
              if X/8.5 <= mouse[0] <= X/8.5+20 and Y/10.5 <= mouse[1] <= Y//10.5+20: 
                  intro()
                    
      # fills the screen with a color 
      screen.blit(intro_bg, (0, 0))
        
      # stores the (x,y) coordinates into 
      # the variable as a tuple 
      mouse = pygame.mouse.get_pos() 
        
      # if mouse is hovered on a button it 
      # changes to lighter shade 
      if X/8.5 <= mouse[0] <= X/8.5+20 and Y/10.5 <= mouse[1] <= Y/10.5+20: 
            pygame.draw.rect(screen,color_light,[X/8.5,Y/10.5,20,20]) 
            
      else: 
          pygame.draw.rect(screen,color_dark,[X/8.5,Y/10.5,20,20]) 
        
      # superimposing the text onto our button 
      button("x",8.5,3,10.5,-2.5)
        
      # updates the frames of the game 
      pygame.display.update() 

def intro():
  screen = pygame.display.set_mode((X, Y))
  pygame.display.set_caption('main menu')
  screen.fill(background_colour)
  pygame.display.flip()
  intro_bg = pygame.image.load("intro.png")
  intro_bg = pygame.transform.scale(intro_bg, (X, Y))
  
  color_light = (170,170,170) 
  color_dark = (100,100,100) 

  smallfont = pygame.font.SysFont('Corbel',35) 
    
  # rendering a text written in 
  # this font 
  
  quit_text = smallfont.render('quit' , True , gray) 
  play_text = smallfont.render('play' , True , gray)
  instruction_text = smallfont.render('how to play' , True , gray)
    
  while True: 
        
      for ev in pygame.event.get(): 
            
          if ev.type == pygame.QUIT: 
              pygame.quit() 
                
          #checks if a mouse is clicked 
          if ev.type == pygame.MOUSEBUTTONDOWN: 
                
              #if the mouse is clicked on the 
              # button the game is terminated 
              if X/3 <= mouse[0] <= X/3+200 and Y/3 <= mouse[1] <= Y/3+40: 
                  play()
              elif X/3 <= mouse[0] <= X/3+200 and Y/2 <= mouse[1] <= Y/2+40: 
                  instruction()
                
              elif X/3 <= mouse[0] <= X/3+200 and Y/1.5 <= mouse[1] <= Y/1.5+40: 
                pygame.quit() 
                    
      # fills the screen with a color 
      screen.blit(intro_bg, (0, 0))
        
      # stores the (x,y) coordinates into 
      # the variable as a tuple 
      mouse = pygame.mouse.get_pos() 
        
      # if mouse is hovered on a button it 
      # changes to lighter shade 
      if X/3 <= mouse[0] <= X/3+200 and Y/3 <= mouse[1] <= Y/3+40: 
            pygame.draw.rect(screen,color_light,[X/3,Y/3,200,40]) 
      elif X/3 <= mouse[0] <= X/3+200 and Y/2 <= mouse[1] <= Y/2+40: 
          pygame.draw.rect(screen,color_light,[X/3,Y/2,200,40]) 
      elif X/3 <= mouse[0] <= X/3+200 and Y/1.5 <= mouse[1] <= Y/1.5+40: 
          pygame.draw.rect(screen,color_light,[X/3,Y/1.5,200,40]) 
            
      else: 
          pygame.draw.rect(screen,color_dark,[X/3,Y/3,200,40]) 
          pygame.draw.rect(screen,color_dark,[X/3,Y/2,200,40]) 
          pygame.draw.rect(screen,color_dark,[X/3,Y/1.5,200,40]) 
        
      # superimposing the text onto our button 
      screen.blit(play_text, (X/2-20,Y/3))   
      screen.blit(instruction_text, (X/2-65,Y/2)) 
      screen.blit(quit_text, (X/2-20,Y/1.5)) 
        
      # updates the frames of the game 
      pygame.display.update() 

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
    pygame.display.set_caption('game over')
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
    brazil = pygame.image.load("brazil.png")
    argentina = pygame.image.load("argentinaflag.png")
    colombia = pygame.image.load("colombia.png")
    malaysia = pygame.image.load("malaysia.png")
    pakistan = pygame.image.load("pakistan.png")
    ecuador = pygame.image.load("ecuador.png")
    cuba = pygame.image.load("cuba.png")
    mexico = pygame.image.load("mexico.png")
    spain = pygame.image.load("spain.png")
    flag_list = [canada, brazil, argentina, colombia, malaysia, pakistan, ecuador, cuba, mexico, spain]
    
    flag_choice = flag_list.pop(random.randint(0,len(flag_list)-1))
    
    image = pygame.transform.scale(flag_choice, (200, 100))
    
    if flag_choice == canada:
      word = "canada"
    elif flag_choice == brazil:
      word = "brazil"
    elif flag_choice == argentina:
      word = "argentina"
    elif flag_choice == colombia:
      word = "colombia"
    elif flag_choice == malaysia:
      word = "malaysia"
    elif flag_choice == pakistan:
      word = "pakistan"
    elif flag_choice == ecuador:
      word = "ecuador"
    elif flag_choice == cuba:
      word = "cuba"
    elif flag_choice == mexico:
      word = "mexico"
    elif flag_choice == spain:
      word = "spain"
  
      
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
                if guess.lower() == word:
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

intro()