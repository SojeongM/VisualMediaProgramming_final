import pygame
import sys
import numpy as np
import math
from os import path
MAX_WIDTH = 800
MAX_HEIGHT = 430

pygame.init()
pygame.mixer.init()

fps = pygame.time.Clock()

font_name = pygame.font.match_font('impact')
background = pygame.image.load("assets/wallpaper.jpg")
background_rect = background.get_rect()
background2 = pygame.image.load("assets/wallpaper2.jpg")
background2_rect = background.get_rect()
imgs=['assets/mob1_pixel.png', 'assets/mob2_pixel.png', 'assets/mob3_pixel.png', 'assets/mob4_pixel.png', 'assets/mob5_pixel.png', 'assets/mob6_pixel.png', 'assets/rocket_pixel.png']
player_mini_img = pygame.transform.scale(pygame.image.load('assets/poketball_pixel.png'), (25, 25))

start_sound=pygame.mixer.Sound("snd/아케이트 레트로 고전게임.mp3")
game_sound=pygame.mixer.Sound("snd/Pokemon - Heart Gold and Soul Silver - Ethans Theme.mp3")
level_up_sound=pygame.mixer.Sound("snd/Pokemon Platinum - Level Up.mp3")
game_over_sound=pygame.mixer.Sound("snd/Pokemon Battle Revolution - Battle Loss.mp3")
pew_sound=pygame.mixer.Sound("snd/pew.wav")
bomb_sound=pygame.mixer.Sound("snd/bomb.mp3")
jump_sound=pygame.mixer.Sound("snd/마리오점프.mp3")

all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
clouds = pygame.sprite.Group()

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []
img_dir= path.join(path.dirname(__file__), 'assets/')

for i in range(9):
    filename = 'regularExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join('assets/', filename))
    
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    filename = 'sonicExplosion0{}.png'.format(i)
    img = pygame.image.load(path.join(img_dir, filename))
   
    explosion_anim['player'].append(img)

class Explosion(pygame.sprite.Sprite):
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 75

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

#pikachu
class Player1(pygame.sprite.Sprite):
    def __init__(self, x, y, i, d, j, up, down):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('assets/pikachu_pixel.png')
        self.image=pygame.transform.flip(self.image, True, False)
       
        self.rect = self.image.get_rect()
        self.wid=self.image.get_width()
        self.height=self.image.get_size()[1]
        self.width=MAX_HEIGHT-self.height
        self.rect.x=x
        self.rect.y=y
       
        self.down=down
        self.jump=j
        self.double=d
        self.maxjump=180
        self.maxjump2=self.rect.y-50
        self.dx=0
        self.score=0
        self.life=3
        self.up=up
        self.meet=i
        self.id=1
        self.block_speed=20
    def update(self):
        if self.meet:
            ac=1

        else:
            if self.double:
                self.rect.y -= 30.0

            elif self.up:
                self.rect.y -= 30.0
            
            elif not self.up and not self.down:
                self.rect.y += 20.0

            if self.up and self.rect.y<= self.maxjump and not self.double:
            
                self.up = False
            elif self.rect.y<=self.maxjump2:
            
                self.double=False
            if not self.down and self.rect.y>= self.width:
                self.down = True
                self.rect.y = self.width
                self.jump=0
            
        self.rect.x+=self.dx
        self.score+=1
        
    def shoot(self):
        
        if self.life>0:
            pew_sound.play()
            bullet = Bullet(self.rect.x+self.wid/2, self.rect.y+self.image.get_size()[1]-40)
            all_sprites.add(bullet) 
            bullets.add(bullet)
            self.life-=1
        
             
    def draw(self, screen):
        if self.rect.y==440:
            screen.blit(self.image, (self.rect.x, self.rect.y))
           
        else:
            screen.blit(self.image2, (self.rect.x, self.rect.y))

#pichu
class Player0(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('assets/pichu_pixel1.png') 
        self.image=pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.wid=self.image.get_width()
        self.height=self.image.get_size()[1]
        self.width=MAX_HEIGHT-self.height
        self.rect.x=60
        self.rect.y=self.width
        self.up=False
        self.down=True
        self.jump=0
        self.double=False
        self.maxjump=180
        self.maxjump2=self.rect.y-50
        self.dx=0
        self.score=0
        self.life=1
        self.up=False
        self.meet=False
        self.id=0
        self.block_speed=15

    def update(self):
        if self.meet:
            ac=1

        else:
            if self.double:
                self.rect.y -= 30.0

            elif self.up:
                self.rect.y -= 30.0
            
            elif not self.up and not self.down:
                self.rect.y += 20.0

            if self.up and self.rect.y<= self.maxjump and not self.double:
            
                self.up = False
            elif self.rect.y<=self.maxjump2:
            
                self.double=False
            if not self.down and self.rect.y>= self.width:
                self.down = True
                self.rect.y = self.width
                self.jump=0
            
        self.rect.x+=self.dx
        self.score+=1
        
    def shoot(self):       
        if self.life>0:           
            bullet = Bullet(self.rect.x+self.wid/2, self.rect.y+self.image.get_size()[1]-20)
            all_sprites.add(bullet) 
            bullets.add(bullet)
            self.life-=1
            pew_sound.play()
        
             
    def draw(self, screen):
        if self.rect.y==440:
            screen.blit(self.image, (self.rect.x, self.rect.y))
           
        else:
            screen.blit(self.image2, (self.rect.x, self.rect.y))

#raichu
class Player2(pygame.sprite.Sprite):
    def __init__(self, x, y, i, d, j, up, down):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load('assets/raichu_pixel.png')
        self.image=pygame.transform.flip(self.image, True, False)
    
        self.rect = self.image.get_rect()
        self.wid=self.image.get_width()
        self.height=self.image.get_size()[1]
        self.width=MAX_HEIGHT-self.height
        self.rect.x=x
        self.rect.y=y
    
        self.down=down
        self.jump=j
        self.double=d
        self.maxjump=180
        self.maxjump2=self.rect.y-50
        self.dx=0
        self.score=0
        self.life=5
        self.up=up
        self.meet=i
        self.id=2
        self.block_speed=25

    def update(self):
        if self.meet:
            ac=1

        else:
            if self.double:
                self.rect.y -= 30.0

            elif self.up:
                self.rect.y -= 30.0
            
            elif not self.up and not self.down:
                self.rect.y += 30.0

            if self.up and self.rect.y<= self.maxjump and not self.double:
            
                self.up = False
            elif self.rect.y<=self.maxjump2:
            
                self.double=False
            if not self.down and self.rect.y>= self.width:
                self.down = True
                self.rect.y = self.width
                self.jump=0
            
        self.rect.x+=self.dx
        self.score+=1
        
    def shoot(self):
        
        if self.life>0:
            
            bullet = Bullet(self.rect.x+self.wid/2, self.rect.y+self.image.get_size()[1]-20)
            all_sprites.add(bullet) 
            bullets.add(bullet)
            self.life-=1
            pew_sound.play()
        
             
    def draw(self, screen):
        if self.rect.y==440:
            screen.blit(self.image, (self.rect.x, self.rect.y))
           
        else:
            screen.blit(self.image2, (self.rect.x, self.rect.y))
#poketball
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/poketball_pixel.png')
        self.image=pygame.transform.scale(self.image, (30, 30))
        self.image=pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = 40

    def update(self):
        self.rect.x += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.centerx > MAX_WIDTH:
            self.kill()       

class Block(pygame.sprite.Sprite):
    def __init__(self, img, speed) : 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.height = self.image.get_size()[1]
        if img == 'assets/mob5_pixel.png' or img =='assets/mob6_pixel.png' :
            self.rect.y = 130
        else:
            self.rect.y = MAX_HEIGHT - self.height
        self.rect.x = MAX_WIDTH
        self.speed=speed
        self.k=9
    def update(self):
        self.rect.x -= self.speed
        if self.k==0:
            self.kill()     
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

#발판
class Cloud(pygame.sprite.Sprite):
    def __init__(self) : 
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('assets/cloud.jpg')
        self.rect = self.image.get_rect()
        self.width=self.image.get_size()[0]
        self.height = self.image.get_size()[1]
        self.rect.x = MAX_WIDTH
        self.rect.y = 233
        self.speed=23
    def update(self):
        self.rect.x -= self.speed  
        if self.rect.x <=0:
            self.rect.x=MAX_WIDTH   
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

def draw_text(surf, text, size, x, y, color):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_lives(surf, x, y, lives, img):
    for i in range(lives):
        img_rect = img.get_rect()
        img_rect.x = x - 30 * i
        img_rect.y = y
        surf.blit(img, img_rect)

def show_go_screen(screen):
    screen.blit(background, background_rect)
    start_sound.play()
    draw_text(screen, "Jumping Pokemon", 64, MAX_WIDTH / 2, MAX_HEIGHT / 4, (51, 102, 153))
    draw_text(screen, "Arrow keys for move, Space to Jump!", 22,
              MAX_WIDTH / 2, MAX_HEIGHT / 2, (0,51, 102))
    draw_text(screen, "Press a key to begin", 18, MAX_WIDTH / 2, MAX_HEIGHT * 3 / 4-70, (51, 51, 51))
    pygame.display.flip()
    waiting = True
    while waiting:
        fps.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
#main 함수
def makePygame(name):
    pygame.init()
    pygame.display.set_caption("20191585_final")

    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    
    alltime=0
    
    score=0
    
    player=Player0()
    k=np.random.randint(0, len(imgs))
    block=Block(imgs[k], player.block_speed)
    all_sprites.add(player)
    all_sprites.add(block)
    done=False
    cloud=Cloud()
    
    newblock_time=np.random.randint(50, 60)
    kx=0
    ky=0
    scroll = 0
    start=True

    tiles = math.ceil(MAX_WIDTH / background.get_width()) + 1
    game_sound.play()
    while True:
        alltime+=1
        screen.fill((255, 255, 255))
        player.dx=0
        if start:
            game_sound.stop()
            show_go_screen(screen)
            start = False
            start_sound.stop()
            game_sound.play()
        elif done==True:
            game_sound.stop()
            screen.blit(background2, background2_rect)
          
            draw_text(screen, "game over", 64, MAX_WIDTH / 2, MAX_HEIGHT / 4, (102, 153, 204))
            draw_text(screen, str(score), 18, MAX_WIDTH/ 2, MAX_HEIGHT / 4+100,(153, 204, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
        else:         
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_SPACE: #jump
                        if player.meet:
                            player.meet=False
                            player.double=True
                            player.rect.x+=30
                            
                            player.maxjump2=player.rect.y-50
                            jump_sound.set_volume(0.5)
                            jump_sound.play()
                            
                        if not player.double and player.jump==1:
                            player.double=True
                            player.maxjump2=player.rect.y-100
                            jump_sound.set_volume(0.5)
                            jump_sound.play()
                        if player.down:
                            jump_sound.set_volume(0.5)
                            jump_sound.play()
                            player.up = True
                            player.down = False

                        player.jump+=1
                        player.dx=15
                  
                    if event.key == pygame.K_LEFT: #move left
                        player.dx = -15
                    elif event.key == pygame.K_RIGHT: #move right
                        player.dx = 15
                    elif event.key == pygame.K_a: #shooting
                        player.shoot()
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        player.dx = 0
            

            if player.id==0 and player.score>=200: #진화 조건1
                all_sprites.remove(player)
                new_x=player.rect.x
                if not player.meet:
                    new_y=player.rect.y-25
                else:
                    new_y=player.rect.y
                i=player.meet
                d=player.double
                j=player.jump
                up=player.up
                down=player.down
                player.kill()
                player=Player1(new_x, new_y,  i, d, j, up, down)
                all_sprites.add(player)
                level_up_sound.play()
            
            if player.id==1 and player.score>=400: #진화 조건 2
                all_sprites.remove(player)
                new_x=player.rect.x
                if not player.meet:
                    new_y=player.rect.y+5
                else:
                    new_y=player.rect.y
                i=player.meet
                d=player.double
                j=player.jump
                up=player.up
                down=player.down
                player.kill()
                player=Player2(new_x, new_y,  i, d, j, up, down)
                all_sprites.add(player)
                level_up_sound.play()

            blocks.add(block)
            
            #화면 끝까지 간 mob들 삭제 및 자동 생성
            for re in blocks:
                if re.rect.x <=0:
                    #cloud 위에 있을 시 날라다니는 mob 생성x
                    if player.meet:
                        k=np.random.randint(0, len(imgs)-2)
                    else:
                        k=np.random.randint(0, len(imgs))

                    re.kill()
                    all_sprites.remove(re)
            
                    block=Block(imgs[k],player.block_speed)
                    all_sprites.add(block)
                
            #몹들과 포켓볼 간의 충돌 감지
            hits = pygame.sprite.groupcollide(blocks, bullets, True, pygame.sprite.collide_mask)
            
            for hit in hits:
                hit.kill()
                all_sprites.remove(hit)
                expl = Explosion(hit.rect.center, 'lg')
                all_sprites.add(expl)
                hit.rect.x=0
                player.score += 100
                score+=100
                bomb_sound.play()
                
            #플레이어와 몹들 간 충돌 감지
            hits = pygame.sprite.spritecollide(player, blocks, True, pygame.sprite.collide_rect)
         
            if hits:
                for hit in hits:
                    expl = Explosion(player.rect.center, 'lg')
                    all_sprites.add(expl)
                    hit.kill()
                    all_sprites.remove(hit)
                    hit.rect.x=0
                
                done=True
                game_over_sound.play()

  
            #newblock_time(60~70 사이)가 지날 때마다 몹 생성
            if alltime%newblock_time==0:
                k=np.random.randint(0, len(imgs))
               
                newblock=Block(imgs[k], player.block_speed)
                blocks.add(newblock)
                newblock_time=np.random.randint(60, 70)
                alltime=0
                all_sprites.add(newblock)
                if not player.meet:
                    cloud=Cloud() 
                    clouds.add(cloud)
                    all_sprites.add(cloud)

            #발판 올라감 감지
            if not player.meet:
                if player.rect.y+player.height > cloud.rect.y-20 and player.rect.y+player.height < cloud.rect.y+20:
                    if player.rect.x+player.wid/2. > cloud.rect.x-5 and player.rect.x+player.wid/2. < cloud.rect.x+cloud.width+5:
                        player.meet=True
                        kx=player.rect.x
                        ky=player.rect.y

            #발판 올라갔을 때 player 이동 업데이트
            if player.meet:
                player.rect.x=kx
                player.rect.y=ky
                kx-=cloud.speed
                ky=cloud.rect.y-player.height
                if player.rect.x<=0:
                    kx+=MAX_WIDTH
            else:
                #플레이어가 올라가 있지 않은 발판이 화면 끝에 닿았을 때 자동 삭제
                for c in clouds:
                    if c.rect.x<=20 :
                        c.kill()
                        clouds.remove(c)
                        all_sprites.remove(c)
            
                
            all_sprites.update()

            #총 합 점수 업데이트        
            score+=1

            #화면 자동 이동
            ii = 0
            while(ii < tiles):
                screen.blit(background, (background.get_width()*ii+ scroll, 0))
                ii += 1

            scroll -= 6
  
   
            if abs(scroll) > background.get_width():
                scroll = 0
    
        
            all_sprites.draw(screen)
            draw_text(screen, str(score), 18, MAX_WIDTH/ 2, 10, (51, 102, 153))
            draw_lives(screen, MAX_WIDTH - 30, 5, player.life, player_mini_img)  
        
        pygame.display.update()
        fps.tick(10)


if __name__ == '__main__':
    makePygame('my pygame')
