from pygame import *

mixer.init()
font.init() #підключаємо шрифти
#створи вікно гри
WIDTH = 900
HEIGHT = 600
window = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Лабіринт")
clock = time.Clock()

mixer.music.load("jungles.ogg")
mixer.music.set_volume(0.5) #задаємо гучність музики
# mixer.music.play() 

win_sound = mixer.Sound("money.ogg")
kick_sound = mixer.Sound("kick.ogg")

font1 = font.SysFont("Impact", 50)
result = font1.render("", True, (255,0,0))

#класи для наших спрайтів
class GameSprite(sprite.Sprite):
   def __init__(self, image_name, x, y, width, height):
      super().__init__()
      self.img = transform.scale(image.load(image_name), (width, height))
      self.rect = self.img.get_rect()
      self.rect.x = x
      self.rect.y = y
      self.width = width
      self.height = height
   
   def draw(self):
      window.blit(self.img, self.rect)

class Player(GameSprite):
   def __init__(self):
      super().__init__("hero.png", 200, 200, 75, 75)
      self.speed = 5
      self.hp = 100

   def update(self):
      keys = key.get_pressed()
      if keys[K_LEFT] and self.rect.x > 0:
         self.rect.x -= self.speed
      if keys[K_RIGHT] and self.rect.x < WIDTH - self.width:
         self.rect.x += self.speed
      if keys[K_UP] and self.rect.y > 0:
         self.rect.y -= self.speed
      if keys[K_DOWN] and self.rect.y < HEIGHT - self.height:
         self.rect.y += self.speed

class Enemy(GameSprite):
   def __init__(self, x, y):
      super().__init__("cyborg.png", x,  y, 75, 75)
      self.speed = 3
      self.direction = "left"

   def update(self):
      if self.rect.x <= WIDTH - 300:
         self.direction = "right"
      if self.rect.x >=  WIDTH - 100:
         self.direction = "left"
         
      if self.direction == "left":
         self.rect.x -= self.speed
      else:
         self.rect.x += self.speed

class Wall(sprite.Sprite):
   def __init__(self, x, y, width, height, color = (255, 113, 31)):
      super().__init__()
      self.img = Surface((width, height)) #створюємо зображення прямокутника
      self.rect = self.img.get_rect() #створюємо прямокутну область
      self.img.fill(color) #задаємо колір поверхні (стіни)
      self.rect.x = x
      self.rect.y = y
      self.width = width
      self.height = height
   
   def draw(self):
      window.blit(self.img, self.rect)

class Treasure(GameSprite):
   def __init__(self):
      super().__init__("treasure.png", WIDTH - 120, HEIGHT - 100, 75, 75)
      
bg_image = transform.scale(image.load("background.jpg"), (WIDTH, HEIGHT))
player = Player()
cyborg = Enemy( WIDTH - 150, HEIGHT - 200)
gold = Treasure()

wall1 = Wall(x = 50, y = 50, width = 20, height = 200)
wall2 = Wall(x = 200, y = 300, width = 300, height = 20)
walls = [wall1, wall2]

run = True
finish = False
FPS = 60
while run:
   for e in event.get():
      if e.type == QUIT:
         run = False

   if not finish:

      player.update() #запускаємо рух гравця
      cyborg.update()

      if sprite.collide_rect(player, gold):
         result = font1.render("Ти переміг!", True, (255,0,0))
         finish = True
         win_sound.play()
      
      if sprite.collide_rect(player, cyborg):
         result = font1.render("Ти програв!", True, (255,0,0))
         finish = True
         kick_sound.play()

      window.blit(bg_image, (0,0))
      for w in walls:
         w.draw()
         if sprite.collide_rect(player, w):
            result = font1.render("Ти програв!", True, (255,0,0))
            finish = True
            kick_sound.play()

      player.draw()
      cyborg.draw()
      gold.draw()
   else:
      window.blit(result, (200, 200))
   display.update()
   clock.tick(FPS)
