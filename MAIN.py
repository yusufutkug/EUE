import pygame as pg
import random,sys
from ARMY import *
from HEROS import *
from SKILLS import *
from ITEMS import *
from INVENTORY import *

class Game:
    __background = pg.image.load("bg5.12.jpg")
    __window_width, __window_height = 1536, 864
    __window_size = (__window_width, __window_height)
    __bgX = -__background.get_height() + __window_height
    __bgX2 = -2 * __background.get_height() + __window_height

    def __init__(self):
        self.clock = pg.time.Clock()
        self.__screen = pg.display.set_mode(self.__window_size,pg.FULLSCREEN)
        self.font = pg.font.SysFont('ocraextended', 40)
        self.all_sprites = pg.sprite.Group()
        self.skills_sprite= pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.hero_bullets = pg.sprite.Group()
        self.enemy_bullets = pg.sprite.Group()
        self.player = pg.sprite.Group()
        self.item_sprite =pg.sprite.Group()
        self.wallet_sprite=pg.sprite.Group()
        self.Hero=Tank((self.__screen.get_width()//2-32,self.__screen.get_height()//2+32),self.__screen, self.all_sprites, self.hero_bullets,self.player)
        self.score=0
        self.bgspeed=0.4
        self.army=Army(self.all_sprites,self.enemy_bullets, self.enemies,self.__screen,self.hero_bullets)
        self.done = False
        self.item1=Speed_of_Bullet(self.bgspeed+0.6,self.all_sprites,self.item_sprite,self.__screen)
        self.item2=Shooting_Power(self.bgspeed+0.6,self.all_sprites,self.item_sprite,self.__screen)
        self.atack_skill=atack_skill(self.all_sprites,self.skills_sprite)
        self.defense_skill=defense_skill(self.all_sprites,self.skills_sprite)
        self.entry_music=pg.mixer.music.load("storm-night.ogg")
        self.wallet = Wallet(self.all_sprites,self.wallet_sprite,self.__screen,self.font)


    def entry_screen(self):
        pygame.mixer.music.play
        left_icon = pg.image.load("left-arrow.png")
        right_icon = pg.image.load("right-arrow.png")
        font1 = pg.font.SysFont('berlinsansfbkalın', 70)
        font2 = pg.font.SysFont("niagaraengraved", 40)
        game_name = font1.render("Endless Universe Expedition", True, (128, 0, 0))
        game_name_rect = game_name.get_rect(center = (self.__window_width // 2, self.__window_height // 6))
        text_to_start = self.font.render('---Press Enter to Start---', True, (255, 255, 255))
        textRect = text_to_start.get_rect(center = (self.__window_width // 2, self.__window_height // 6 * 5))
        top_score = self.font.render(("TOP SCORE"), True, (128, 1, 1))
        top_scorerect = top_score.get_rect(center = (self.__window_width // 2, self.__window_height // 6 + 164))
        the_score = self.font.render(str(self.updateFile(0)), True, (128, 1, 1))
        the_scorerect = the_score.get_rect(center= (self.__window_width // 2, self.__window_height // 6 +196))
        blit_list=[(text_to_start, textRect),(game_name, game_name_rect),(top_score, top_scorerect),(the_score, the_scorerect),(left_icon, (self.__screen.get_width() // 2 - 160, self.__screen.get_height() // 2 + 32)),(right_icon, (self.__screen.get_width() // 2 + 96, self.__screen.get_height() // 2 + 32))]
        while True:  
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                         return self.run()
                    elif event.key == pg.K_RIGHT:
                        self.Hero.kill()
                        self.Hero=Ghost((self.__screen.get_width()//2-32,self.__screen.get_height()//2+32),self.__screen, self.all_sprites, self.hero_bullets,self.player)
                    elif event.key == pg.K_LEFT:
                        self.Hero.kill()
                        self.Hero =Tank((self.__screen.get_width()//2-32,self.__screen.get_height()//2+32),self.__screen, self.all_sprites, self.hero_bullets,self.player)
            self.update_background(self.bgspeed)
            for i,j in blit_list:
                self.__screen.blit(i,j)
            self.Hero.draw_hero(self.__screen,self.font)
            pg.display.flip()
    def run(self):
        pygame.mixer.music.load("Mega Bot Bay.ogg")
        pygame.mixer.music.play()
        while not self.Hero.hero_death and not self.done:

            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()
            dt = self.clock.tick(60)/1000
            self.update_background(self.bgspeed)
            self.handle_events()
            self.run_logic(dt)
            self.draw()
        self.updateFile(self.score)
        # self.play_again()

    def play_again(self):
        while True:
            pass

    def handle_events(self):

        for event in pg.event.get():

            if event.type == pg.QUIT:
                self.done = True

            elif event.type==pg.KEYDOWN:

                    if event.key==pg.K_e:
                        pygame.mixer.Sound("mixkit-robot-system-fail-2960.wav").play()
                        self.atack_skill.key_check(True)        
                        self.Hero.keyCheck("e")
                        
                    elif event.key==pg.K_q:
                        self.defense_skill.key_check(True)
                        self.Hero.keyCheck("q")

    def update_score_coins(self):

        self.score=self.army.send_score()
        self.bgspeed=0.4+(self.score//10)**(1/2)
        self.wallet.update_wallet(self.army.send_coins())
    
    def run_logic(self, dt):

        self.all_sprites.update(dt)
        self.army.update()
        self.update_score_coins()
        enemy_Hero=pg.sprite.groupcollide(self.player,self.enemies,False,True)
        hero_bullet=pg.sprite.groupcollide(self.player,self.enemy_bullets,False,True)                
        for hero, enemy_list in enemy_Hero.items():
            for enemy in enemy_list:
                hero.health -= enemy.damage
        for hero, bullet_list in hero_bullet.items():
            for bullet in bullet_list:
                hero.health -= bullet.damage
        if len(self.enemies.sprites())==0:
            self.army.creating_army(self.bgspeed)

    def update_background(self,speed:float):
        self.__screen.blit(self.__background, (0, self.__bgX))
        self.__screen.blit(self.__background, (0, self.__bgX2))
        self.__bgX +=speed/2
        self.__bgX2 +=speed/2
        if self.__bgX >= self.__window_height:
            self.__bgX = -self.__background.get_height() + self.__bgX2 + 2
        elif self.__bgX2 >= self.__window_height:
            self.__bgX2 = -self.__background.get_height() + self.__bgX + 2

    def draw(self):
        score_label= self.font.render(f"SCORE: {self.score}", 1, (255, 255, 255))
        self.__screen.blit(score_label,(0,0))
        self.all_sprites.draw(self.__screen)
        pg.display.flip()

    def updateFile(self, score):
        f = open('top_score.txt', 'r')
        file = f.readlines()
        last = int(file[0])

        if last < int(score):
            f.close()
            file = open('top_score.txt', 'w')
            file.write(str(score))
            file.close()

            return score

        return last

if __name__ == '__main__':
    pg.init()
    pg.mouse.set_visible(False)
    Game().entry_screen()
    pg.quit()