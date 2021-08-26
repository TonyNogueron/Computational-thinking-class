from pygame import *
import sys, random

init()
screen = display.set_mode((800,600))

cielo = image.load("cielo.jpg")
cielo = transform.scale(cielo, (800,600))

disparo = image.load("disparo.png")
disparo = transform.scale(disparo, (196 // 2, 60 // 2))

nave = image.load("nave.png")
nave = transform.scale(nave, (174, 129))


pajaro = image.load("pajaro.png")
pajaro = transform.scale(pajaro, (1104//8,749//8))

avesX = []
avesY = []


for i in range(6):
    avesX.append(random.randint(801, 2000))
    avesY.append(random.randint(20,500))
    
    

xCielo = 0
xCielo1 = 800

xNave = 50
yNave = 250

xDisparo = 1000
yDisparo = 1000

xPajaro = random.randint(801, 1600)
yPajaro = random.randint(20,500)

speedNave = 1.4

while True:
    screen.fill((255,255,255))
    for e in event.get():
        if e.type == QUIT: sys.exit()
        if e.type == KEYDOWN and e.key == K_p and xDisparo > 800:
            xDisparo = xNave + 75
            yDisparo = yNave + 86
    
    screen.blit(cielo,(xCielo,0))
    screen.blit(cielo,(xCielo1,0))
    
#Movimiento
    if yNave < 0:
        yNave = 0
    if yNave + 129 > 600:
        yNave = 600 -129
    if key.get_pressed()[K_w]:
         yNave = yNave - speedNave
    if key.get_pressed()[K_s]:
         yNave = yNave + speedNave
    if xNave < 10:
        xNave = 10
    if  xNave + 174 > 800:
        xNave = 800 - 174
    if key.get_pressed()[K_a]:
         xNave = xNave - speedNave
    if key.get_pressed()[K_d]:
         xNave = xNave + speedNave
         
    screen.blit(nave, (xNave, yNave))    
    screen.blit(disparo, (xDisparo, yDisparo))
    
    for i in range(6):
        screen.blit(pajaro, (avesX[i], avesY[i]))
        avesX[i] = avesX[i] - 0.6
        if avesX[i] < -150:
            avesX[i] = (random.randint(801, 2000))
            avesY[i] = (random.randint(20,500))
            
    naveRect = Rect(xNave, yNave, nave.get_width(), nave.get_height())
    disparoRect = Rect(xDisparo, yDisparo, disparo.get_width(), disparo.get_height())
    
    
    for i in range(6):
        aveRect = Rect(avesX[i],avesY[i], pajaro.get_width(), pajaro.get_height())
        if disparoRect.colliderect(aveRect):
            avesX[i] = (random.randint(801, 2000))
            avesY[i] = (random.randint(20,500))
    

    
    
    
    if xCielo < -800:
        xCielo = 800
    if xCielo1 < -800:
        xCielo1 = 800
        
    xCielo = xCielo-0.4
    xCielo1 = xCielo1-0.4
    xDisparo = xDisparo + 2.4
    
    
    
    xPajaro = xPajaro - 0.6
    
    
    
    display.flip()
    
    