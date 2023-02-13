import pygame as pg
import time
import _thread

padoru1 = pg.image.load('./img/padoruDireita-removebg-preview.png')
if padoru1 == None:
    print("Erro ao carregar")
    quit()
padoru2 = pg.image.load('./img/padorunyan-removebg-preview.png')
if padoru2 == None:
    print("Erro ao carregar")
    quit()
song = './song/padoru.mp3'

padoru1_x = 0
padoru1_y = 0

branco = (255,255,255)

padoru2_x = 510
padoru2_y = 310

ball_x = 300
ball_y = 200
sentidoX = 0
sentidoY = 0

score1 = 0
score2 = 0

def bola(tamanho, width, height):
    global ball_y
    global ball_x
    global sentidoX
    global sentidoY
    global score1
    global score2

    while True:
        if sentidoX == 0:
            ball_x += 5
        else:
            ball_x -= 5

        if ball_x <= (padoru1_x+70) and ball_y >=padoru1_y and ball_y <= (padoru1_y+90):
            sentidoX = 0
        if ball_x >= ((padoru2_x+20)-tamanho) and ball_y >=padoru2_y and ball_y <= (padoru2_y+90):
            sentidoX = 1

        if ball_x <= 0:
            pg.mixer.music.play()
            score2 += 1
            print("Gol!")
            print("Placar: " + str(score1) + " x " + str(score2))
            ball_x = 300
            ball_y = 300
        if ball_x >= (screen_width-tamanho):
            pg.mixer.music.play()
            score1 += 1
            print("Gol!")
            print("Placar: " + str(score1) + " x " + str(score2))
            ball_x = 300
            ball_y = 300

        if sentidoY == 0:
            ball_y -= 5
        else:
            ball_y += 5
        
        if ball_y <= 0:
            sentidoY = 1
        if ball_y >= (height-tamanho):
            sentidoY = 0
        

        time.sleep(0.05)

screen_width = 600
screen_height = 400

pg.init()
pg.display.set_caption('PADORU PONG')
pg.mixer.music.load(song)
pg.display.set_icon(padoru2)

screen = pg.display.set_mode((screen_width, screen_height))

clock = pg.time.Clock()
done = False

_thread.start_new_thread(bola, (20,screen_width, screen_height))
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    pressed = pg.key.get_pressed()   
    if pressed[pg.K_w] and padoru1_y >= 0: 
        padoru1_y -= 5
    if pressed[pg.K_s] and padoru1_y <= screen_height-90: 
        padoru1_y += 5

    if pressed[pg.K_UP] and padoru2_y >= 0: 
        padoru2_y -= 5
    if pressed[pg.K_DOWN] and padoru2_y <= screen_height-90: 
        padoru2_y += 5


    screen.fill(branco)

    screen.blit(padoru1,(padoru1_x,padoru1_y))
    screen.blit(padoru2,(padoru2_x,padoru2_y))   
    pg.draw.rect(screen, (0,0,0), pg.Rect(ball_x,ball_y,20,20))

    pg.display.flip()
    clock.tick(100)