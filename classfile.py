import pygame
import random
import environment
import random

class Ball(object):
    
    def __init__(self,ai_settings):
        self.ball_size = ai_settings.ball_size
        self.ball_pos = ai_settings.ball_iniPos
        self.ball_rect = pygame.Rect(self.ball_pos+self.ball_size)
        self.ball_surface = pygame.Surface(self.ball_size)
        self.color = ai_settings.ball_iniCol
        self.ball_surface.fill(pygame.Color(self.color))
        self.left = ai_settings.ball_left
        self.right = ai_settings.ball_right
        self.speed = ai_settings.ball_speed
    
    def checkDead(self, screen_size):
        if self.ball_rect.left <= 0 or self.ball_rect.right >= screen_size[0] \
            or self.ball_rect.top <= 0 or self.ball_rect.bottom >= screen_size[1]:
            return True
        else:
            return False

class Slot(object):

    def __init__(self, screen_size, prev_slot_level, prev_slot_height):
        self.level = prev_slot_level + random.randint(-10, 10)
        if self.level <= 0:
            self.level = 1
        elif self.level >= screen_size[1] - 600:
            self.level = screen_size[1] - 601
        self.height = prev_slot_height + random.randint(-10, 10)
        if self.height <= 400:
            self.height = 401
        elif self.height >= 600:
            self.height = 599
        self.bottom_slot_rect = pygame.Rect(screen_size[0] - 16, screen_size[1] - self.level, 16, self.level)
        self.bottom_slot_surface = pygame.Surface((16, self.level))
        self.bottom_slot_surface.fill((178, 233, 238))
        self.top_slot_rect = pygame.Rect(screen_size[0] - 16, 0, 16, screen_size[1] - self.level - self.height)
        self.top_slot_surface = pygame.Surface((16, screen_size[1] - self.level - self.height))
        self.top_slot_surface.fill((178, 233, 238))
        
    def updateSlot(self):
        self.bottom_slot_rect[0] -= 1
        self.top_slot_rect[0] -= 1

        
class Biofilm(object):
    def __init__(self, ai_settings):
        self.name = "biofilm"
        self.film_pos = ai_settings.film_iniPos
        self.film_rect = pygame.Rect((self.film_pos,0)+ai_settings.film_size)
        self.film_surface = pygame.Surface(ai_settings.film_size)
        self.film_color_order = ai_settings.color_order
        self.film_color_order.append("white")
        self.film_color = self.film_color_order[random.randint(0,len(self.film_color_order)-1)]
        # self.film_color = "green"
        self.film_surface.fill(pygame.Color(self.film_color))
        self.film_speed = ai_settings.film_speed
        


