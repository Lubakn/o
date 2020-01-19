import pygame
import sys
import os
import random

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

class Cactus(pygame.sprite.Sprite):

    def __init__(self, group):
        super().__init__(group)
        self.image = load_image(names_images[random.randrange(3)], -1)
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 220

    def update(self, *args):
        self.rect = self.rect.move(-5, 0)
        '''if dino.rect.x + :
            self.image = self.image_boom'''

running = True
size = weidth, height = 900, 400
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
all_sprites = pygame.sprite.Group()
all_sprites2 = pygame.sprite.Group()
dino = pygame.sprite.Sprite()
dino.image = load_image("trex_1.png", -1)
dino.rect = dino.image.get_rect()
all_sprites.add(dino)
dino.rect.x = 20
dino.rect.y = 220
im = []
im.append("trex_2.png")
im.append("trex_3.png")
flag = False
pic = 0
names_images = []
names_images.append('cactus_1.png')
names_images.append('cactus_2.png')
names_images.append('cactus_3.png')
pygame.draw.line(screen, pygame.Color('black'), (0, 300), (900, 300), 5)
screen.fill(pygame.Color('grey'), pygame.Rect(0, 300, 900, 400))
all_sprites.draw(screen)
clock = pygame.time.Clock()
v = 500
v2 = 60
a = 9.8
fps = 60
t = 0
jump = False
MYEVENTTYPE = 30
MYEVENTTYPE2 = 30
pygame.time.set_timer(MYEVENTTYPE, 80)
times = []
time = random.randrange(500, 3000)
flag2 = False
death = False
pygame.font.init()
font = pygame.font.Font(None, 30)
text = font.render('0', 1, (0, 0, 0))
text_x = 800
text_y = 50
text_w = text.get_width()
text_h = text.get_height()
screen.blit(text, (text_x, text_y))
while running:
    if not death:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                flag = True
                if event.key == 273:
                    jump = True
                    clock.tick(fps)
                    dino.rect = dino.rect.move(0, -1)
                    times.append(pygame.time.get_ticks())
            if event.type == MYEVENTTYPE and not jump:
                pic += 1
                dino.image = load_image(im[pic % 2], -1)
        if flag:
            screen.fill((255, 255, 255))
            pygame.draw.line(screen, pygame.Color('black'), (0, 300), (900, 300), 5)
            screen.fill(pygame.Color('grey'), pygame.Rect(0, 300, 900, 400))
            if pygame.time.get_ticks() - times[len(times) - 1] >= time:
                times.append(pygame.time.get_ticks())
                time = random.randrange(1000, 3000)
                Cactus(all_sprites2)
            if jump:
                dino.image = load_image("trex_1.png", -1)
                if v > 60:
                    dino.rect = dino.rect.move(0, -1 * int((t * v) / 1000))
                    v -= a
                elif dino.rect.y < 220:
                    dino.rect = dino.rect.move(0, int((t * v2) / 1000))
                    v2 += a
                else:
                    jump = False
                    v = 500
                    v2 = 60
                t = clock.tick(fps)
            all_sprites.draw(screen)
            all_sprites2.draw(screen)
            all_sprites2.update()
            death = pygame.sprite.spritecollide(dino, all_sprites2, False)
            text = font.render(str(int(round(pygame.time.get_ticks() - times[0]) // 1000)), 1, (0, 0, 0))
            screen.blit(text, (text_x, text_y))
        pygame.display.flip()
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
pygame.quit()
sys.exit()