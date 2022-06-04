
import pygame as pg
screen=pg.display.set_mode((500,300))
animated=[pg.Surface((1,screen.get_height())),pg.Surface((1,screen.get_height())),pg.Surface((1,screen.get_height())),pg.Surface((3,screen.get_height())),pg.Surface((3,screen.get_height())),pg.Surface((9,screen.get_height())),pg.Surface((9,screen.get_height())),pg.Surface((9,screen.get_height())),pg.Surface((9,screen.get_height())),pg.Surface((50,screen.get_height())),pg.Surface((30,screen.get_height())),pg.Surface((30,screen.get_height())),pg.Surface((50,screen.get_height())),pg.Surface((50,screen.get_height())),pg.Surface((30,screen.get_height())),pg.Surface((30,screen.get_height())),pg.Surface((9,screen.get_height())),pg.Surface((9,screen.get_height())),pg.Surface((3,screen.get_height())),pg.Surface((1,screen.get_height()))]
current_animated=0
size = (8, 8)
hotspot = (0, 0)
xormask = (0, 96, 120, 126, 112, 96, 0, 0)
andmask = (500,240, 254, 255, 254, 240, 96, 0)

expected_length = 4
expected_cursor = pg.cursors.Cursor(size, hotspot, xormask, andmask)
pg.mouse.set_cursor(expected_cursor)
while True:
        screen.fill((255,0,0))
        pg.display.flip()
