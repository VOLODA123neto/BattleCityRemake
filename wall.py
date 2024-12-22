import pygame

class Wall:
    def __init__(self, x, y, width, height, wall_type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.wall_type = wall_type  
        self.is_destroyed = False
        if self.wall_type == 1:
            self.image = pygame.image.load("assets/wall_indestructible.png")
        elif self.wall_type == 2:
            self.image = pygame.image.load("assets/wall_destroyable.png")
        elif self.wall_type == 3:
            self.image = pygame.image.load("assets/wall_passable.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, screen):
        if not self.is_destroyed:
            screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def check_collision_with_bullet(self, bullet):
        if self.wall_type == 2: 
            if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)):
                self.is_destroyed = True
                return True  
        elif self.wall_type == 1: 
            if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)):
                return True 
        return False