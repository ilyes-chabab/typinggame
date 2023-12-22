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
button_rule= pygame.draw.rect(screen , (0,0,230),(400,300,200,50))
rule_text=police.render("Règles",1,(255,255,255))
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
win_sound = pygame.mixer.Sound('sound\win.mp3')
lose_sound = pygame.mixer.Sound('sound\lose.mp3')
fall_sound = pygame.mixer.Sound("fall.mp3")
jump_sound = pygame.mixer.Sound('sound\jump.mp3')
wrong_sound = pygame.mixer.Sound('sound\wrong.mp3')

goku=image_goku_redimensionne
liste=[]
with open("word.txt","r")as file:
    for i in file:
        liste.append(i.rstrip("\n"))
#initialisation des variables
y_background1=0
y_background2=-600
y_cloud0=615
y_cloud1=465
y_cloud2=315
y_cloud3=165
y_cloud4=15
y_cloud5=-135
life=3
score=0
y=0
victory=0
defeat=0
#initialisation des True/False pour les condition
clock=pygame.time.Clock()
running=True
menu=True
Game=False
party=True
image=True
notfinish=True
win=True
lose=True
fail=True
descent=False
rule=False
#fonction pour pouvoir ecrire quelque chose sur l'ecran
def message(size,message,message_rectangle,color):
    font=pygame.font.SysFont("arial",size)
    message = font.render(message,False,color)
    screen.blit(message,message_rectangle) 
#boucle principale        
while running:
    #boucle du menu pour regarder les regles ou jouer directement
    while menu:       
        screen.fill((255,255,140))     
        pygame.draw.rect(screen , (255, 191, 0),(200,200,600,300))      
        pygame.draw.rect(screen , (0,0,230),(400,380,200,50))
        pygame.draw.rect(screen , (0,0,230),(400,295,200,50))
        message(80,"Typing game",(300,35,0,0),(0,0,0))
        message(40,"version dragon ball z",(320,120,0,0),(0,0,200))

        screen.blit(play_text,(475,385))
        screen.blit(rule_text,(475,300))
        #evenement des Boutons Jouer et Regle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.collidepoint(event.pos):
                    menu=False
                    game=True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rule.collidepoint(event.pos):
                    rule=True
        if rule:
            pygame.draw.rect(screen , (255,255,255),(0,0,550,280))
            message(40,"Règles :",(220,0,0,0),(0,0,200))
            message(25,"Le but du jeu est d'écrire les mots affichés.",(0,50,0,0),(0,0,200))
            message(25,"Vous avez 3 vies et si vous vous trompez sur une lettre",(0,75,0,0),(0,0,200))
            message(25,"vous en perdrez une.Au bout de 0 , vous perdez la partie.",(0,100,0,0),(0,0,200))
            message(25,"Chaque lettres entrée rapporte 1 points et au bout ",(0,125,0,0),(0,0,200))
            message(25,"de 50 point , vous gagnez la partie.",(0,150,0,0),(0,0,200))
            message(25,"Bon jeu ! :D",(200,200,0,0),(0,0,200))


        clock.tick(60)
        pygame.display.flip()
    #boucle pour commencer ou recommencer une partie
    while party:
        random_word=random.choice(liste) 
        random_text=police.render(random_word,1,(0,0,0))              
        print(random_word)      
        num=0
        typing_word= random_word[num]
        print(typing_word)
        party=False
    #affichage de toutes les images    
    screen.fill((0,128,80))                 
    screen.blit(fond_namek_redimensionne,(0,y_background1))
    screen.blit(fond_space_redimensionne,(0,y_background2)) 
    screen.blit(image_cloud_redimensionne,(350,y_cloud0))  
    screen.blit(image_cloud_redimensionne,(350,y_cloud1))   
    screen.blit(image_cloud_redimensionne,(350,y_cloud2))    
    screen.blit(image_cloud_redimensionne,(350,y_cloud3))    
    screen.blit(image_cloud_redimensionne,(350,y_cloud4))  
    screen.blit(image_cloud_redimensionne,(350,y_cloud5))
    #condition pour creer une animation du decors lorsque le mot est juste , image est True et lorsqu'il devient false
    #le fond et les nuage(plateforme) sont deplacés vers le bas
    if image:
        screen.blit(image_goku_redimensionne,(375,250))
    else:
        screen.blit(image_goku_jump_redimensionne,(470,115))
        #systeme pour que le decors bouge vers le bas et donner l'impression que le personnage saute
        #(petit bug: lorsque l'on joue trop vite , le decor n'a pas le temps de bien se mettre et ca crée un decalage)
        y+=5
        y_cloud0+=5 
        y_cloud1+=5 
        y_cloud2+=5                   
        y_cloud3+=5                    
        y_cloud4+=5
        y_cloud5+=5
        y_background1+=1
        y_background2+=1
        if y_cloud0 == 765:
            y_cloud0 = -135                      
        if y_cloud1 == 765:
            y_cloud1 = -135
        if y_cloud2 == 765:
            y_cloud2 = -135
        if y_cloud3 == 765:
            y_cloud3 = -135
        if y_cloud4 == 765:
            y_cloud4 = -135
        if y_cloud5 == 765:
            y_cloud5 = -135
        if y==150:
            print(y)
            y=0
            screen.blit(image_goku_redimensionne,(400,200))
            image=True 
            print(image) 
    #tant que le joueur n'a nis perdu ni gagné , le dashboard et le mot a ecrire sont visible
    if notfinish:
        pygame.draw.rect(screen , (0,0,80),(0,50,350,300))    
        message(50,random_word,(425,50,0,0),(0,0,180)) 
        message(28,f"Lettre a écrire : {typing_word.upper()}",(425,100,0,0),(0,0,180))   
        message(50,f"nombre de vie :{life}",(0,50,0,0),(255,255,255))
        message(50,f"Score :{score}",(0,90,0,0),(255,255,255))
        message(50,f"Victoire :{victory}",(0,150,0,0),(255,255,255))
        message(50,f"Défaite :{defeat}",(0,200,0,0),(255,255,255))
    #conditions pour prévenir au joueur s'il a perdu ou gagné 
    if lose == False:
        message(50,"Perdu ! :(",(400,150,0,0),(255,0,0))
        message(50,"Appuyer sur entrée pour recommencer.",(100,100,0,0),(255,255,255))
    if win == False:
        message(50,"Gagné ! :D",(400,150,0,0),(255,0,0))
        message(50,"Appuyer sur entrée pour recommencer.",(100,100,0,0),(255,255,255))    

    pygame.display.flip()  
    #programmation du jeu    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #lorsque le joueur a perdu ou gagné , il doit appuyer sur return(entrée) pour recommencer.Alors ca 
        if notfinish==False :   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:                
                    lose=True
                    win=True
                    life=3
                    score=0
                    y_background1=0
                    y_background2=-600
                    y_cloud1=465
                    y_cloud2=315
                    y_cloud3=165
                    y_cloud4=15
                    y_cloud5=-135
                    party=True                    
                    notfinish=True    
        if notfinish:                 
            if event.type == pygame.KEYDOWN:
                if event.unicode == typing_word or event.unicode.upper() == typing_word.upper():                     
                    fail=True 
                    image=True
                    print("succés")
                    num +=1
                    print(len(random_word))
                    print(num)
                    if num == len(random_word):   
                        jump_sound.play() 
                        score+=num
                        print(f"score:{score}")        
                        party=True
                        image=False
                        rock=True
                        print(image)
                        print(f"y_cloud{y_cloud1}")                                  
                    else:                        
                        typing_word=random_word[num]
                elif fail:
                    if event.unicode.isalpha():
                        if event.unicode != typing_word or event.unicode.upper() != typing_word.upper(): 
                            wrong_sound.play()
                            fall_sound.play()
                            life -=1 
                            message(500,"X",(0,0,0,0),(255,0,0))
                            descent=True
                            fail=False
                if life==0:
                    lose_sound.play()
                    defeat+=1
                    lose=False                    
                    notfinish=False
                if score>=50:
                    win_sound.play()
                    victory+=1
                    win=False
                    notfinish=False
    if descent:#meme systeme que pour que la montée mais cette fois ci le personnage descend si il se trompe sur une lettre
        y-=5
        y_cloud0-=5
        y_cloud1-=5 
        y_cloud2-=5                   
        y_cloud3-=5                    
        y_cloud4-=5
        y_cloud5-=5
        y_background1-=1
        y_background2-=1 
        if y_cloud0 == -135 :
            y_cloud0 = 765                   
        if y_cloud1 == -135:
            y_cloud1 = 765
        if y_cloud2 == -135:
            y_cloud2 = 765
        if y_cloud3 == -135:
            y_cloud3 = 765
        if y_cloud4 == -135:
            y_cloud4 = 765
        if y_cloud5 == -135:
            y_cloud5 = 765
        if y==-150:
            print(y)
            y=0                         
            descent=False
    
             
        clock.tick(60)   
        pygame.display.flip()  
pygame.quit()
sys.exit()          