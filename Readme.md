# VisualMediaProgramming_final
## Jumping Pokemon <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=Python&logoColor=white"/> 
### Jumping game + Shooting game

* **jump to avoid the enemy**<br><br>
  <img src="./assets/jump.jpg" width="300">
* **throw Pockeball to attack the enemy**
  <p><img src="./assets/attack1.jpg" width="300"><img src="./assets/attack2.jpg" width="300"></p>
* **evolve when certain score are met**
  <p><img src="./assets/evolve1.jpg" width="300"><img src="./assets/evolve2.jpg" width="300"></p>
  - three stages of evolution (pichu > pikachu > raich)<br>
  - increased the number of Pokeballs available when evolving<br>
  - adjust difficulty by increasing enemy speed<br><br>
* **add a cloud for the player to step on**
  <p><img src="./assets/cloud1.jpg" width="300"></p>
  - helps player to avoid the enemy or attack the flying enemy

   
### How to play
* press a key to start
* press space key to jump or double jump
* press a to attack the enemy
* ress arrow key to move left and right


### Main skills
* using Sprite-Collision to detect the collision between player, mobs, bulltes
```javascript
hits = pygame.sprite.spritecollide(player, blocks, True, pygame.sprite.collide_rect)
```
* make special collitions detect fuction to detect the cloud and player
```javascript
if not player.meet:
    if player.rect.y+player.height > cloud.rect.y-20
      and player.rect.y+player.height < cloud.rect.y+20:
        if player.rect.x+player.wid/2. > cloud.rect.x-5
           and player.rect.x+player.wid/2. < cloud.rect.x+cloud.width+5:
            player.meet=True
            kx=player.rect.x
            ky=player.rect.y
```
* random enemy spawns every (60-70) ticks
```javascript
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
  ```
* screen scroll
```javascript
ii = 0
while(ii < tiles):
  screen.blit(background, (background.get_width()*ii+ scroll, 0))
  ii += 1
scroll -= 6

if abs(scroll) > background.get_width():
  scroll = 0
```

### Source
* player, enemy, cloud images
  * PNGWing.com
* background images
  * wallpaperflare.com/pokemon-video-games-pixel-art-pixels-sky-architecture-wallpaper-sbkam 
  * moewalls.com/pixel-art/munchlax-sleeping-on-the-field-pixel-live-wallpaper/
* sound
  * gamethemesongs.com/search.php?q=pokemon
  * blog.naver.com/dbsgksdjq0/221441228861
  * m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=sounddownload&logNo=221278719255

## [Playing demo](https://www.youtube.com/watch?v=Qf9bJTcgAkg) <img src="https://img.shields.io/badge/YouTube-FF0000?style=flat&logo=YouTube&logoColor=white"/> 



