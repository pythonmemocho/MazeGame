import pygame as pg

WIDTH  =  475
HEIGHT =  475

CHIP_SIZE = 25
PLAYER_SIZE = 15
CLOCK = pg.time.Clock()
FPS = 60

SCREEN = pg.display.set_mode((WIDTH,HEIGHT))
pg.display.set_caption('MAZE')
    
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)