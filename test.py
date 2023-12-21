import sys
import pygame
import random
import time
pygame.init()
screen=pygame.display.set_mode((1000,600))
police=pygame.font.SysFont("arial",30)
button_play= pygame.draw.rect(screen , (0,0,230),(400,380,200,50))
play_text=police.render("Jouer",1,(255,255,255))
clock= pygame.time.Clock()
fond_namek= pygame.image.load('picture/decor_namek.jpg').convert()
fond_namek_redimensionne=pygame.transform.scale(fond_namek, (1000,600))
image_rock= pygame.image.load('picture/rock.png')
image_rock_redimensionne=pygame.transform.scale(image_rock, (400,250))
image_goku= pygame.image.load('picture/goku.webp')
image_goku_redimensionne=pygame.transform.scale(image_goku, (200,300))
image_goku_jump= pygame.image.load('picture/goku_jump.webp')
image_goku_jump_redimensionne=pygame.transform.scale(image_goku_jump, (200,300))

goku=image_goku_redimensionne
liste=[]
with open("word.txt","r")as file:
    for i in file:
        liste.append(i.rstrip("\n"))

y_background=0
y_rock1=0
y_rock2=-250
order=1
y=0

running=True
menu=True
Game=False
party=True
image=True
def message(size,message,message_rectangle,color):
    font=pygame.font.SysFont("arial",size)
    message = font.render(message,False,color)
    screen.blit(message,message_rectangle)
while running:
    y_rock1 +=3
    while menu:
        screen.fill((255,255,140))
        pygame.draw.rect(screen , (255, 191, 0),(200,100,600,400))      
        pygame.draw.rect(screen , (0,0,230),(400,380,200,50))
        screen.blit(play_text,(475,385))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.collidepoint(event.pos):
                    menu=False
                    game=True
        clock.tick(10)
        pygame.display.flip()

    while party:
        random_word=random.choice(liste) 
        random_text=police.render(random_word,1,(0,0,0))              
        print(random_word)
        num=0
        typing_word= random_word[num]
        print(typing_word)
        party=False
    screen.fill((0,128,80))                 
    screen.blit(fond_namek_redimensionne,(0,y_background))
    screen.blit(image_rock_redimensionne,(0,y_rock1))   #y=310
    screen.blit(image_rock_redimensionne,(350,y_rock2))    #y=-250

    if image:
        screen.blit(image_goku_redimensionne,(450,200))
    else:
        screen.blit(image_goku_jump_redimensionne,(500,180))   
    message(50,random_word,(445,180,0,0),(0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.unicode == typing_word:
                image=True
                print("succés")
                num +=1
                print(len(random_word))
                print(num)
                if num == len(random_word):
                    order+=1
                    y_background+=50
                    party=True
                    image=False
                else:                        
                    typing_word=random_word[num] 
            
        
            
        pygame.display.flip()  
pygame.quit()
sys.exit()          