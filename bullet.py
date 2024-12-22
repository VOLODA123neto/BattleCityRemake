import pygame

YELLOW = (255, 255, 0)

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 10
        self.speed = -7

    def move(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, (self.x, self.y, self.width, self.height))

    def check_collision_with_walls(self, walls):
        for wall in walls:
            if wall.check_collision_with_bullet(self):  
                return True  
        return False