import py
import pygame as pg
import  sys
from Groups import *
from ARMY import *
from HEROS import *
from SKILLS import *
from ITEMS import *
from INVENTORY import *


pg.init()
pg.display.init()
pg.mixer.init()
class Game:

    __background = pg.image.load("image\\bg5.12.jpg")
    __window_width, __window_height = pygame.display.Info().current_w,pygame.display.Info().current_h
    __window_size = (__window_width, __window_height)
    __bgX = -__background.get_height() + __window_height
    __bgX2 = -2 * __background.get_height() + __window_height
    buzzersound=pg.mixer.Sound("sound\\wrong-buzzer-6268.wav")
    entryScreenMusic="sound\\storm-night.ogg"
    runMusic="sound\\Mega Bot Bay.ogg"
    hero_index=0

    def __init__(self):
        self.clock = pg.time.Clock()
        self.font = pg.font.SysFont('ocraextended', 40)
        self.__screen = pg.display.set_mode(self.__window_size,pg.FULLSCREEN)  
        self.score=0
        self.coins=0
        self.bgspeed=0.4
        self.all_sprites = Group()
        self.skills_sprite= Group()
        self.enemies = Group()
        self.hero_bullets = Group()
        self.enemy_bullets =Group()
        self.player = Group()
        self.item_sprite =Group()
        self.drops=Group()
        #sor self.wallet
        self.heroList=Heros.__subclasses__()
        self.Heroparemeters=[(self.__screen.get_width()//2-32,self.__screen.get_height()//2+32),self.__screen, self.all_sprites, self.hero_bullets,self.player,self.enemy_bullets,self.enemies,self.drops]
        self.Hero=self.heroList[self.hero_index](self.Heroparemeters[0],self.Heroparemeters[1],self.Heroparemeters[2],self.Heroparemeters[3],self.Heroparemeters[4],self.Heroparemeters[5],self.Heroparemeters[6],self.Heroparemeters[7])
        self.wallet = Wallet(self.all_sprites,self.__screen,self.font)
        self.army=Army(self.all_sprites,self.enemy_bullets, self.enemies,self.__screen,self.hero_bullets,self.drops,self.wallet)
        self.item1=Speed_of_Shooting(self.bgspeed+0.6,self.all_sprites,self.item_sprite,self.__screen,self.wallet)
        self.item2=Shooting_Power(self.bgspeed+0.6,self.all_sprites,self.item_sprite,self.__screen,self.wallet)
        self.atack_skill=atack_skill(self.all_sprites,self.skills_sprite)
        self.defense_skill=defense_skill(self.all_sprites,self.skills_sprite)
        

    def entry_screen(self):
        pg.mixer.music.load(self.entryScreenMusic)
        pg.mixer.music.play()
        left_icon = pg.image.load("image\\left-arrow.png")
        right_icon = pg.image.load("image\\right-arrow.png")
        font1 = pg.font.SysFont('berlinsansfbkalın', 70)
        game_name = font1.render("Endless Universe Expedition", True, (128, 0, 0))
        game_name_rect = game_name.get_rect(center = (self.__window_width // 2, self.__window_height // 6))
        text_to_start = self.font.render('---Press Enter to Start---', True, (255, 255, 255))
        textRect = text_to_start.get_rect(center = (self.__window_width // 2, self.__window_height // 6 * 5))
        top_score = self.font.render(("TOP SCORE"), True, (128, 1, 1))
        top_scorerect = top_score.get_rect(center = (self.__window_width // 2, self.__window_height // 6 + 164))
        the_score = self.font.render(str(self.updateFile(0)), True, (128, 1, 1))
        the_scorerect = the_score.get_rect(center= (self.__window_width // 2, self.__window_height // 6 +196))
        blit_list=[(text_to_start, textRect),(game_name, game_name_rect),(top_score, top_scorerect),(the_score, the_scorerect),(left_icon, (self.__screen.get_width() // 2 - 160, self.__screen.get_height() // 2 + 32)),(right_icon, (self.__screen.get_width() // 2 + 96, self.__screen.get_height() // 2 + 32))]
        check=True
         
        while check: 
            if not pygame.mixer.music.get_busy():
                pg.mixer.music.play()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        check=False
                        pg.mouse.set_pos(self.__screen.get_width()/2,self.__screen.get_height()/7*6)
                        self.Hero.move()
                        self.run()      
                    elif event.key == pg.K_RIGHT:
                        self.Hero.kill()
                        self.hero_index-=1
                        if self.hero_index<-len(self.heroList):
                            self.hero_index=len(self.heroList)-1
                        self.Hero=self.heroList[self.hero_index](self.Heroparemeters[0],self.Heroparemeters[1],self.Heroparemeters[2],self.Heroparemeters[3],self.Heroparemeters[4],self.Heroparemeters[5],self.Heroparemeters[6],self.Heroparemeters[7])
                    elif event.key == pg.K_LEFT:
                        self.Hero.kill()
                        self.hero_index+=1
                        if self.hero_index==len(self.heroList):
                            self.hero_index=-len(self.heroList)
                        self.Hero =self.heroList[self.hero_index](self.Heroparemeters[0],self.Heroparemeters[1],self.Heroparemeters[2],self.Heroparemeters[3],self.Heroparemeters[4],self.Heroparemeters[5],self.Heroparemeters[6],self.Heroparemeters[7])
                        print(self.player.sprites()) 
            self.update_background(self.bgspeed)
            for i,j in blit_list:
                self.__screen.blit(i,j)
            self.Hero.draw_hero(self.__screen,self.font)
            pg.display.flip()

    def run(self):
        pg.mixer.music.load(self.runMusic)
        pg.mixer.music.play()
        while not self.Hero.hero_death:

            if not pygame.mixer.music.get_busy():
                pg.mixer.music.play()
            dt = self.clock.tick(60)/1000
            self.update_background(self.bgspeed)
            self.handle_events()
            self.run_logic(dt)
            self.draw()
        self.updateFile(self.score)
        self.play_again()

    def handle_events(self):

        for event in pg.event.get():

            if event.type == pg.QUIT:
                return sys.exit()

            elif event.type==pg.KEYDOWN:

                    if event.key==pg.K_e:
                        self.atack_skill.key_check(self.Hero)  

                    elif event.key==pg.K_ESCAPE:
                        self.pause()    
                         
                    elif event.key==pg.K_q:
                        self.defense_skill.key_check(self.Hero)
                    
                    elif event.key==pg.K_1:
                        if self.item1.trigger(self.Hero):
                            self.item1.kill()
                            self.item1=Speed_of_Shooting(self.bgspeed+0.6,self.all_sprites,self.item_sprite,self.__screen,self.wallet)
                        else:
                            self.buzzersound.set_volume(0.2)
                            self.buzzersound.play()
                            
                    elif event.key==pg.K_2:
                        if self.item2.trigger(self.Hero):
                            self.item2.kill()
                            self.item2=Shooting_Power(self.bgspeed+0.6,self.all_sprites,self.item_sprite,self.__screen,self.wallet)
                        else:
                            self.buzzersound.set_volume(0.2)
                            self.buzzersound.play()

    def update_score_coins(self):

        self.score=self.army.send_score(self.score)
        self.bgspeed=1+(self.score//10)**(1/2)
        self.coins=self.army.send_coins(self.coins)
  
    
    def run_logic(self, dt):

        self.all_sprites.update(dt)
        self.update_score_coins()    
        

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
    
    def pause(self):
        x=pg.mouse.get_pos()
        font=pg.font.SysFont('ocraextended', 80)
        text=font.render('PAUSE', True, (255, 255, 255))
        rect=text.get_rect(midbottom=(self.__screen.get_width()//2,self.__screen.get_height()//2-100))
        playAgain=pg.image.load("image\\reloading.png")
        exit=pg.image.load("image\\exit.png")
        playAgainRect=playAgain.get_rect(center=(self.__screen.get_width()/2-100,self.__screen.get_height()/2))
        exitRect=exit.get_rect(center=(self.__screen.get_width()/2+100,self.__screen.get_height()/2))
        self.__screen.blit(text,rect)
        self.__screen.blit(playAgain,playAgainRect)
        self.__screen.blit(exit,exitRect)
        pg.display.flip()
        check=True
        pg.mouse.set_cursor((8, 8),(0, 0),(0, 96, 120, 126, 112, 96, 0, 0),(224,240, 254, 255, 254, 240, 96, 0))
        pg.mouse.set_visible(True)
        while check:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.type == pg.QUIT:
                        sys.exit()
                    if event.key == pg.K_ESCAPE:
                        check=False
                        pg.mouse.set_pos(x)
                        pg.mouse.set_visible(False)
            if pg.mouse.get_pressed()[0]:
                cor=pg.mouse.get_pos()
                if cor[0] in range(exitRect.left,exitRect.right) and cor[1] in range(exitRect.top,exitRect.bottom) :
                    sys.exit()
                elif cor[0] in range(playAgainRect.left,playAgainRect.right) and cor[1] in range(playAgainRect.top,playAgainRect.bottom) :
                    check=False
                    self.__init__()
                    self.entry_screen()
    def play_again(self):
        pg.mixer.music.pause()
        font=pg.font.SysFont('ocraextended', 100)
        text=font.render('GAME OVER', True, (255, 255, 255))
        rect=text.get_rect(midbottom=(self.__screen.get_width()//2,self.__screen.get_height()//2-100))
        playAgain=pg.image.load("image\\reloading.png")
        exit=pg.image.load("image\\exit.png")
        playAgainRect=playAgain.get_rect(center=(self.__screen.get_width()/2-100,self.__screen.get_height()/2))
        exitRect=exit.get_rect(center=(self.__screen.get_width()/2+100,self.__screen.get_height()/2))
        self.__screen.blit(text,rect)
        self.__screen.blit(playAgain,playAgainRect)
        self.__screen.blit(exit,exitRect)
        pg.display.flip()
        pg.mouse.set_cursor((8, 8),(0, 0),(0, 96, 120, 126, 112, 96, 0, 0),(224,240, 254, 255, 254, 240, 96, 0))
        pg.mouse.set_visible(True)
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            if pg.mouse.get_pressed()[0]:
                cor=pg.mouse.get_pos()
                if cor[0] in range(exitRect.left,exitRect.right) and cor[1] in range(exitRect.top,exitRect.bottom) :
                    sys.exit()
                elif cor[0] in range(playAgainRect.left,playAgainRect.right) and cor[1] in range(playAgainRect.top,playAgainRect.bottom) :
                    pg.mouse.set_visible(False  )
                    self.__init__()
                    self.entry_screen()
                    
                
    
    



if __name__ == '__main__':
    pg.mouse.set_visible(False)
    EUE=Game()
    EUE.entry_screen()
    pg.quit()