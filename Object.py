import pygame
import sys
from random import randint

class Bird(pygame.sprite.Sprite):
    img1 = pygame.image.load(".\\image\\role1.png")
    img2 = pygame.image.load(".\\image\\role2.png")
    img3 = pygame.image.load(".\\image\\role3.png")
    image = img1
    rect = image.get_rect()
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.rect.center = [150,425]
        self.speed = [0,0]

    def move_up(self):
        self.rect = self.rect.move([4,-6])
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.right >= 1260:
            self.rect.right = 1260

    def move_down(self):
        self.rect = self.rect.move([-1,2])
        if self.rect.bottom >= 850:
            self.rect.bottom = 850
        if self.rect.left <= 150:
            self.rect.left = 150


virus_blue = pygame.image.load(".\\image\\blue.png")
virus_red = pygame.image.load(".\\image\\red.png")
virus_green = pygame.image.load(".\\image\\green.png")

class Virus_Blue(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        y = randint(80,700)
        position = [1280,y]

        self.image = virus_blue
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed_factor = 3
        self.left_move_speed = -4
        self.direction = randint(-1,1) # -1表示向上移，1表示向下移

    def check_edges(self):
        if self.rect.top <= 0:
            return True
        elif self.rect.bottom >= 850:
            return True

    def move(self):
        self.rect.x += self.left_move_speed
        self.rect.y += (self.speed_factor * self.direction)
        if self.check_edges():
            self.direction *= -1



class Virus_Red(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        y = randint(80, 700)
        position = [1280, y]

        self.image = virus_red
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed_factor = 1
        self.left_move_speed = -2
        self.direction = randint(-1,1) # -1表示向上移，1表示向下移

    def check_edges(self):
        if self.rect.top <= 0:
            return True
        elif self.rect.bottom >= 850:
            return True

    def move(self):
        self.rect.x += self.left_move_speed
        self.rect.y += (self.speed_factor * self.direction)
        if self.check_edges():
            self.direction *= -1


class Virus_Green(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        y = randint(80, 700)
        position = [1280, y]

        self.image = virus_green
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.speed_factor = 2
        self.left_move_speed = -5
        self.direction = randint(-1,1) # -1表示向上移，1表示向下移

    def check_edges(self):
        if self.rect.top <= 0:
            return True
        elif self.rect.bottom >= 850:
            return True

    def move(self):
        self.rect.x += self.left_move_speed
        self.rect.y += (self.speed_factor * self.direction)
        if self.check_edges():
            self.direction *= -1

class Mask(pygame.sprite.Sprite):
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load(".\\image\\mask.png")
        self.rect = self.image.get_rect()
        self.rect.center = [1100,300]
        self.direction = 1

    def check_edges(self):
        if self.rect.top <= 100:
            return True
        elif self.rect.bottom >= 600:
            return True

    def move(self):
        self.rect.y += (2 * self.direction)
        if self.check_edges():
            self.direction *= -1
