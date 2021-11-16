import pygame
pygame.init()  
pygame.display.set_caption("sprite sheet")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

#MAP: 1 is grass, 2 is brick
map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0],
       [0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0],
       [0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0],
       [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0 ,0, 0, 0, 0],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1, 1, 1, 1]]

brick = pygame.image.load('brick.png') #load your spritesheet
background = pygame.image.load('bg.png') #load your spritesheet
slime = pygame.image.load('slime.png') #load your spritesheet
dirt = pygame.image.load('dirt.png') #load your spritesheet
Samus = pygame.image.load('samus.png') #load your spritesheet
Samus.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)
Samus2 = pygame.image.load('samus2.png') #load your spritesheet
Samus2.set_colorkey((0, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)
clouds = pygame.image.load('cloud.png') #load your spritesheet
clouds.set_colorkey((255, 0, 255)) #this makes bright pink (255, 0, 255) transparent (sort of)

#player variables
phealth = 10
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform

#player2
phealth2 = 10
xpos2 = 500 #xpos of player
ypos2 = 200 #ypos of player
vx2 = 0 #x velocity of player
vy2 = 0 #y velocity of player
keys2 = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround2 = False #this variable stops gravity from pulling you down more when on a platform
RowNum2 = 0 #for left animation, this will need to change for other animations
frameNum2 = 0
ticker2 = 0
direction2 = DOWN

#animation variables 
frameWidth = 84
frameHeight = 79
RowNum = 0 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
direction = DOWN

while not gameover:
    clock.tick(60) #FPS
    
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_a:
                keys[LEFT]=True
            elif event.key == pygame.K_d:
                keys[RIGHT]=True
            elif event.key == pygame.K_w:
                keys[UP]=True
            if event.key == pygame.K_LEFT:
                keys2[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys2[RIGHT]=True
            elif event.key == pygame.K_UP:
                keys2[UP]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                keys[LEFT]=False
            elif event.key == pygame.K_d:
                keys[RIGHT]=False
            elif event.key == pygame.K_w:
                keys[UP]=False
            if event.key == pygame.K_LEFT:
                keys2[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys2[RIGHT]=False
            elif event.key == pygame.K_UP:
                keys2[UP]=False
          

    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        RowNum = 1
        direction = LEFT
    #RIGHT MOVEMENT
    elif keys[RIGHT] == True:
        vx = 3
        RowNum = 2
        direction = RIGHT
    #turn off velocity
    else:
        vx = 0
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
    
    
        
    xpos+=vx #update player xpos
    ypos+=vy

    #player 2
    #LEFT MOVEMENT
    if keys2[LEFT]==True:
        vx2=-3
        RowNum2 = 1
        direction2 = LEFT
    #RIGHT MOVEMENT
    elif keys2[RIGHT] == True:
        vx2 = 3
        RowNum2 = 2
        direction2 = RIGHT
    #turn off velocity
    else:
        vx2 = 0
        #JUMPING
    if keys2[UP] == True and isOnGround2 == True: #only jump when on the ground
        vy2 = -8
        isOnGround2 = False
        direction2 = UP
    
    
        
    xpos2+=vx2 #update player xpos
    ypos2+=vy2
    
    
    #COLLISION
    
    #collision with feetsies
    if map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]>0:
        isOnGround = True
        vy=0

    elif map[int((ypos+frameHeight)/50)][int((xpos+frameWidth/2)/50)]==-1:
        isOnGround = True
        vy-=10
        
    else:
        isOnGround = False
        
    #bump your head, ouch!
    if map[int((ypos)/50)][int((xpos+frameWidth/2)/50)]!=0:
        vy=0
        
    #left collision (it's extra long because we check both head and feets(well, knees) for left collision
    if map[int((ypos+frameHeight-10)/50)][int((xpos)/50)]>0 or map[int((ypos)/50)][int((xpos)/50)]>0 and direction == LEFT:
        xpos+=3
        
    #right collision needed here
    if map[int((ypos+frameHeight-10)/50)][int((xpos+frameWidth)/50)]>0 or map[int((ypos)/50)][int((xpos+frameWidth)/50)]>0 and direction == RIGHT:
        xpos-=3 

    if map[int((ypos+frameHeight-10)/50)][int((xpos+frameWidth)/50)]==-1 or map[int((ypos)/50)][int((xpos+frameWidth)/50)]==-1 and direction == RIGHT:
        xpos-=3
        vx-=20


    if map[int((ypos+frameHeight-10)/50)][int((xpos)/50)]==-1 or map[int((ypos)/50)][int((xpos)/50)]==-1 and direction == LEFT:
        xpos+=3
        vx+=20

    #stop moving if you hit edge of screen (will be removed for scrolling)
    if xpos+frameWidth > 800:
        xpos-=3
    if xpos<0:
        xpos+=3

    
    #stop falling if on bottom of game screen
    if ypos > 800-frameHeight:
        isOnGround = True
        vy = 0
        ypos = 800-frameHeight
    
    #gravity
    if isOnGround == False:
        vy+=.2 #notice this grows over time, aka ACCELERATION


    #player 2 COLLISION
    
    #collision with feetsies
    if map[int((ypos2+frameHeight)/50)][int((xpos2+frameWidth/2)/50)]>0:
        isOnGround2 = True
        vy2=0

    elif map[int((ypos2+frameHeight)/50)][int((xpos2+frameWidth/2)/50)]==-1:
        isOnGround2 = True
        vy2-=10
        
    else:
        isOnGround2 = False
        
    #bump your head, ouch!
    if map[int((ypos2)/50)][int((xpos2+frameWidth/2)/50)]!=0:
        vy2=0
        
    #left collision (it's extra long because we check both head and feets(well, knees) for left collision
    if map[int((ypos2+frameHeight-10)/50)][int((xpos2)/50)]>0 or map[int((ypos2)/50)][int((xpos2)/50)]>0 and direction2 == LEFT:
        xpos2+=3
        
    #right collision needed here
    if map[int((ypos2+frameHeight-10)/50)][int((xpos2+frameWidth)/50)]>0 or map[int((ypos2)/50)][int((xpos2+frameWidth)/50)]>0 and direction2 == RIGHT:
        xpos2-=3 

    if map[int((ypos2+frameHeight-10)/50)][int((xpos2+frameWidth)/50)]==-1 or map[int((ypos2)/50)][int((xpos2+frameWidth)/50)]==-1 and direction2 == RIGHT:
        xpos2-=3
        vx2-=20


    if map[int((ypos2+frameHeight-10)/50)][int((xpos2)/50)]==-1 or map[int((ypos2)/50)][int((xpos2)/50)]==-1 and direction2 == LEFT:
        xpos2+=3
        vx2+=20

    #stop moving if you hit edge of screen (will be removed for scrolling)
    if xpos2+frameWidth > 800:
        xpos2-=3
    if xpos2<0:
        xpos2+=3

    
    #stop falling if on bottom of game screen
    if ypos2 > 800-frameHeight:
        isOnGround2 = True
        vy2 = 0
        ypos2 = 800-frameHeight
    
    #gravity
    if isOnGround2 == False:
        vy2+=.2 #notice this grows over time, aka ACCELERATION
    

        
    #ANIMATION-------------------------------------------------------------------
        
    # Update Animation Information

    if vx != 0: #animate when moving
        ticker+=1
        if ticker%8==0: #only change frames every 10 ticks
          frameNum+=1
        if frameNum>9: 
           frameNum = 0

    #player 2

    if vx2 != 0: #animate when moving
        ticker2+=1
        if ticker2%8==0: #only change frames every 10 ticks
          frameNum2+=1
        if frameNum2>9: 
           frameNum2 = 0
  
    # RENDER--------------------------------------------------------------------------------
    # Once we've figured out what frame we're on and where we are, time to render.
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear

    screen.blit(background, (0,0), (0, 0, 800, 800))

    for i in range (2):
       screen.blit(clouds, (i*800/2,0), (0, 0, 800, 800))
       #screen.blit(trees, (i*800+offset/2,0), (0, 0, 800, 800))
    
    #draw map
    for i in range (16):
        for j in range(16):
            if map[i][j]==1:
                screen.blit(dirt, (j*50, i*50), (0, 0, 50, 50))
            if map[i][j]==2:
                screen.blit(brick, (j*50, i*50), (0, 0, 50, 50))
            if map[i][j]==-1:
                screen.blit(slime, (j*50, i*50), (0, 0, 50, 50))
        
    
    screen.blit(Samus, (xpos, ypos), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight)) 
    screen.blit(Samus2, (xpos2, ypos2), (frameWidth*frameNum2, RowNum2*frameHeight, frameWidth, frameHeight))
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()

