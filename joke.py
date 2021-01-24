import pygame as pg

FPS = 30

pg.init()
skreen = pg.display.set_mode((640, 480))
clock = pg.time.clock()

running = True
while running:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == QUIT:
            running = False
            
pg.quit()
