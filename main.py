import sys
import pygame
import random
import time
#init
pygame.init()
screen=pygame.display.set_mode((1000,600))
police=pygame.font.SysFont("arial",30)
button_play= pygame.draw.rect(screen , (0,0,230),(400,380,200,50))
play_text=police.render("Jouer",1,(255,255,255))
fond_namek= pygame.image.load('picture/decor_namek.jpg').convert()
fond_namek_redimensionne=pygame.transform.scale(fond_namek, (1000,600))
fond_space= pygame.image.load('picture/space.webp').convert()
fond_space_redimensionne=pygame.transform.scale(fond_space, (1000,600))
image_cloud= pygame.image.load('picture/nuage_magique.png')
image_cloud_redimensionne=pygame.transform.scale(image_cloud, (400,170))
image_goku= pygame.image.load('picture/goku.webp')
image_goku_redimensionne=pygame.transform.scale(image_goku, (200,300))
image_goku_jump= pygame.image.load('picture/goku_jump.webp')
image_goku_jump_redimensionne=pygame.transform.scale(image_goku_jump, (200,300))

goku=image_goku_redimensionne
liste=[]
with open("word.txt","r")as file:
    for i in file:
        liste.append(i.rstrip("\n"))

y_background1=0
y_background2=-600
y_cloud1=400
y_cloud2=250
y_cloud3=100
y_cloud4=-50
y_cloud5=-200

life=3
score=0
y=0
clock=pygame.time.Clock()
running=True
menu=True
Game=False
party=True
image=True
notfinish=True
win=True
lose=True
def message(size,message,message_rectangle,color):
    font=pygame.font.SysFont("arial",size)
    message = font.render(message,False,color)
    screen.blit(message,message_rectangle)
def cloud_animation(cloud): 
    if y_cloud1 == 700:
        y_cloud1 = -50             
while running:
    
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
        clock.tick(60)
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
    screen.blit(fond_namek_redimensionne,(0,y_background1))
    screen.blit(fond_space_redimensionne,(0,y_background2))   
    screen.blit(image_cloud_redimensionne,(350,y_cloud1))   #y=310
    screen.blit(image_cloud_redimensionne,(350,y_cloud2))    #y=-250
    screen.blit(image_cloud_redimensionne,(350,y_cloud3))    
    screen.blit(image_cloud_redimensionne,(350,y_cloud4))  
    screen.blit(image_cloud_redimensionne,(350,y_cloud5))

    if image:
        screen.blit(image_goku_redimensionne,(375,185))
    else:
        screen.blit(image_goku_jump_redimensionne,(470,50))
        y+=5
        y_cloud1+=5 
        y_cloud2+=5                   
        y_cloud3+=5                    
        y_cloud4+=5
        y_cloud5+=5
        y_background1+=1
        y_background2+=1                      
        if y_cloud1 == 700:
            y_cloud1 = -50
        if y_cloud2 == 700:
            y_cloud2 = -50
        if y_cloud3 == 700:
            y_cloud3 = -50
        if y_cloud4 == 700:
            y_cloud4 = -50
        if y_cloud5 == 700:
            y_cloud5 = -50
        if y==150:
            print(y)
            y=0
            screen.blit(image_goku_redimensionne,(400,200))
            image=True 
            print(image) 
    if notfinish:
        pygame.draw.rect(screen , (0,0,80),(0,50,350,300))        
        message(50,random_word,(160,180,0,0),(255,255,255)) 
        message(50,f"Lettre a écrire : {typing_word.upper()}",(0,250,0,0),(255,255,255))   
        message(50,f"nombre de vie :{life}",(0,50,0,0),(255,255,255))
        message(50,f"Score :{score}",(0,85,0,0),(255,255,255))
    if lose == False:
        message(50,"Perdu ! :(",(400,150,0,0),(255,0,0))
        message(50,"Appuyer sur entrée pour recommencer.",(100,100,0,0),(255,255,255))
    if win == False:
        message(50,"Gagné ! :D",(400,150,0,0),(255,0,0))
        message(50,"Appuyer sur entrée pour recommencer.",(100,100,0,0),(255,255,255))    

    pygame.display.flip()      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if notfinish==False :   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:                   
                    lose=True
                    win=True
                    life=4
                    score=0
                    y_background1=0
                    y_background2=-600
                    y_cloud1=400
                    y_cloud2=250
                    y_cloud3=100
                    y_cloud4=-50
                    y_cloud5=-200
                    party=True                    
                    notfinish=True    
        if notfinish:                 
            if event.type == pygame.KEYDOWN:
                if event.unicode == typing_word or event.unicode.upper() == typing_word.upper():
                    image=True
                    print("succés")
                    num +=1
                    print(len(random_word))
                    print(num)
                    if num == len(random_word):    
                        score+=num
                        print(f"score:{score}")        
                        party=True
                        image=False
                        rock=True
                        print(image)
                        print(f"y_cloud{y_cloud1}")                                  
                    else:                        
                        typing_word=random_word[num]
                elif event.unicode != typing_word or event.unicode.upper() != typing_word.upper(): 
                    life -=1  
                if life==0:
                    lose=False                    
                    notfinish=False
                if score>=5:
                    win=False
                    notfinish=False    
        
            
        
        clock.tick(60)   
        pygame.display.flip()  
pygame.quit()
sys.exit()          