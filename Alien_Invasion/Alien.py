import pygame
from alien_animation import AlienAnimation
from random import choice

class Alien(pygame.sprite.Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.al = AlienAnimation()
        self.metasprite = [self.al.sprites1,self.al.sprites2,self.al.sprites3,self.al.sprites4]
        self.Rsprite = choice(self.metasprite)
        self.current_sprite = 0
        self.image = self.Rsprite[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.settings.alien_speed *
                 self.settings.fleet_direction)
        self.rect.x = self.x
        #Animates Aliens
        self.current_sprite += 0.005
        if self.current_sprite >= 10:
            self.current_sprite = 0

        self.image = self.Rsprite[int(self.current_sprite)]

