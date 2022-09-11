from pygame import *
import pygame_menu 

init()

mixer.init()
font.init()

WIDTH = 1000
HEIGHT = 800
window = display.set_mode((WIDTH,HEIGHT ))
display.set_caption('maze')

mixer.music.load('jungles.ogg')
mixer.music.set_volume(0)
mixer.music.play()

font.init()

font1 = font.SysFont('Impact', 50)
result = font1.render('', True,(255,0,0))

win_soud = mixer.Sound("money.ogg")
kick_soud =  mixer.Sound("roblox-oof-gamespecificat ions.com_.ogg")

font1 = font.SysFont('Impact', 50)
result = font1.render('', True,(255,0,0))

run = False 
clock = time.Clock()
game = False  
finish = False
FPS = 60

def start_game():
    global game, run
    #game = True
    run = True
    menu.disable()

menu = pygame_menu.Menu('maze',400, 300, theme = pygame_menu.themes.THEME_BLUE)
menu.add.button('Game', start_game)
menu.add.button('exit', pygame_menu.events.EXIT)
menu.mainloop(window)


class GameSprite(sprite.Sprite):
    def __init__(self, image_name,x,y, widht, height):
        super().__init__()
        self.img = transform.scale (image.load(image_name),( widht, height))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.widht = widht
        self.height = height

    def draw(self):
        window.blit(self.img, self.rect)

class Player(GameSprite):
    def __init__(self):
        super().__init__('hero.png', 40, 30 , 70, 70)
        self.speed = 5
        self.hp = 100

    def update(self):
        keys= key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < WIDTH - self.widht:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < HEIGHT - self.height:
            self.rect.y += self.speed
            
class Enemy(GameSprite):
    def __init__(self,x,y):
        super().__init__('cyborg.png', x, y, 75, 75 )
        self.speed = 4
        self.direction = 'left'

    def update(self):
        if self.rect.x <= HEIGHT - 700:
            self.direction = 'right'
        if self.rect.x >= HEIGHT - 0:
            self.direction= 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

     

class Wall(sprite.Sprite):
    def __init__(self, x , y, width, height, color = (190,128,129)):
        super().__init__()
        self.img = Surface((width, height))
        self.rect = self.img.get_rect()
        self.img.fill(color)
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
    
    def draw(self):
        window.blit(self.img, self.rect)

class Treasure(GameSprite):
    def __init__(self):
        super().__init__('treasure.png', WIDTH - 530,HEIGHT- 380 , 75, 75)
        
bg_image = transform.scale(image.load('background.jpg'),(WIDTH,HEIGHT))
player = Player()
cyborg = Enemy(WIDTH - 160,HEIGHT - 200)

gold = Treasure()

wall1 = Wall(x= 0,y = 0,width = 20,height =  910)
wall2 = Wall(x= 20,y = 0,width = 1000,height = 20)
wall3 = Wall(x= 120,y = 100,width = 220,height = 100)
wall4 = Wall(x= 430,y = 400,width = 20,height = 100)
wall5 = Wall(x= 416,y = 0,width = 20,height = 300)
wall6 = Wall(x= 200,y = 0,width = 240,height = 20)
wall7 = Wall(x= 0,y = 400,width = 240,height = 20)
wall8 = Wall(x= 120,y = 200,width = 20,height = 110)
wall9 = Wall(x= 220,y = 300,width = 20,height = 110)
wall10 = Wall(x= 320,y = 200,width = 20,height = 210)
wall11 = Wall(x= 340,y = 390,width = 575,height = 20)
wall12 = Wall(x= 517,y = 100,width = 20,height = 300)
wall13 = Wall(x= 616,y = 0,width = 20,height = 310)
wall14 = Wall(x= 718,y = 100,width = 20,height = 310)
wall15 = Wall(x= 833,y = 0,width = 20,height = 300)
wall16 = Wall(x= 990,y = 0,width = 20,height = 800)
wall17 = Wall(x= 840,y = 278,width = 150,height = 20)
wall18 = Wall(x= 0,y = 780,width = 1000,height = 20)
wall19 = Wall(x= 100,y = 500,width = 350,height = 20)
wall20 = Wall(x= 100,y = 500,width = 20,height = 100)
wall21 = Wall(x= 100,y = 680,width = 320,height = 20)
wall22 = Wall(x= 400,y = 700,width = 20,height = 200)
wall23 = Wall(x= 200,y = 560,width = 100,height = 20)
wall24 = Wall(x= 200,y = 520,width = 20,height = 50)
wall25 = Wall(x= 300,y = 520,width = 20,height = 60)
wall26 = Wall(x= 400,y = 520,width = 50,height = 60)
wall27 = Wall(x= 500,y = 680,width = 20,height = 100)
wall28 = Wall(x= 500,y = 680,width = 80,height = 20)
wall29 = Wall(x= 895,y = 400,width = 20,height = 300)
wall30 = Wall(x= 800,y = 680,width = 20,height = 150)
wall31 = Wall(x=580,y = 680,width = 20,height = 100)
wall32 = Wall(x=680,y = 680,width = 20,height = 100)
wall33 = Wall(x=680,y = 680,width = 120,height = 20)
wall34 = Wall(x=400,y = 530,width = 420,height = 50)
walls =[wall1,wall2,wall3,wall4,wall5,wall6,wall7,wall8,wall9,wall10,wall11,wall12,wall13,wall14,wall15,wall16,wall17,wall18,wall19,wall19,wall20,wall21,wall22,wall23,wall24,wall25,wall26,wall27,wall28,wall29,wall30,wall31,wall32,wall33,wall34]

dificulty = 1
def start_game():
    global run
    run = True
    menu.disable
while run:    
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                menu.enable()
                menu.mainloop(window)


    if not finish:

        player.update()
        cyborg.update()

        if sprite.collide_rect(player, gold):
            result = font1.render('you win',True, (1,250,1))
            finish = True
            win_soud.play()

        if sprite.collide_rect(player, cyborg):
            result = font1.render('you loser',True, (255,0,0))
            finish = True
            kick_soud.play()

        window.blit(bg_image, (0,0))
        for w in walls:
            w.draw()
            if sprite.collide_rect(player, w):
                result = font1.render('you loser',True, (255,0,0))
                finish = True
                kick_soud.play()

        gold.draw()
        player.draw()
        cyborg.draw()
    else:
        window.blit(result, (400, 350))
    display.update()
    clock.tick(FPS)
#створи вікно гри
#задай фон сцени
#створи 2 спрайти та розмісти їх на сцені
##оброби подію «клік за кнопкою "Закрити вікно"»