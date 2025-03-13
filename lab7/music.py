import pygame as pg
import datetime as dt
import time
from sys import exit

pg.mixer.init()
pg.init()

W = 500
H = 500

clock = pg.time.Clock()
screen = pg.display.set_mode((W, H))

pg.display.set_caption("Music!")

imgs = [
    pg.transform.scale(pg.image.load("musics/NotLikeUs.jpeg"), (W, H)),
    pg.transform.scale(pg.image.load("musics/UntitledUnmastered.jpg"), (W, H)),
    pg.transform.scale(pg.image.load("musics/DAMN.jpg"), (W, H))
]

playdm = 0
isplaying = False

def play_music():
    global isplaying
    pg.mixer.music.load(f"musics/{str(playdm)}.mp3")
    pg.mixer.music.play()
    pg.mixer.music.set_volume(0.1)
    isplaying = True


def stopIt():
    global isplaying
    pg.mixer.stop()
    isplaying = False

def playnext():
    global playdm
    playdm = (playdm + 1) % 3
    play_music()

def playprev():
    global playdm
    if playdm - 1 < 0:
        playdm = 2
    else:
        playdm = (playdm - 1) % 3
    
    play_music()

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    screen.fill((18,18,18))
    screen.blit(imgs[playdm], (0,0))

    key = pg.key.get_pressed()

    if(key[pg.K_LEFT]):
        playprev()
        time.sleep(0.5)
    elif key[pg.K_RIGHT]:
       playnext()
       time.sleep(0.5)
    elif key[pg.K_SPACE]:
        if isplaying:
            pg.mixer.music.pause()
            isplaying = False
        else:
            pg.mixer.music.unpause()
            isplaying = True
        time.sleep(0.5)
    elif key[pg.K_s]:
        stopIt()
    
    pg.display.update()
   
pg.quit()