import pygame
from bullet import Bullet

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.speed = 2
        self.direction = "DOWN"
        self.last_shot_time = pygame.time.get_ticks()
        self.is_alive = True 
        self.textures = {
            "UP": pygame.image.load("assets/images/tanks/tank_up.png"),
            "DOWN": pygame.image.load("assets/images/tanks/tank_down.png"),
            "LEFT": pygame.image.load("assets/images/tanks/tank_left.png"),
            "RIGHT": pygame.image.load("assets/images/tanks/tank_right.png"),
        }
        for key in self.textures:
            self.textures[key] = pygame.transform.scale(self.textures[key], (self.width, self.height))

    def move(self, walls, player):
        if not self.is_alive:
            return  

        target_x, target_y = player.x, player.y
        if abs(self.x - target_x) > abs(self.y - target_y):
            if self.x < target_x:
                new_x, new_y = self.x + self.speed, self.y
                self.direction = "RIGHT"
            else:
                new_x, new_y = self.x - self.speed, self.y
                self.direction = "LEFT"
        else:
            if self.y < target_y:
                new_x, new_y = self.x, self.y + self.speed
                self.direction = "DOWN"
            else:
                new_x, new_y = self.x, self.y - self.speed
                self.direction = "UP"

        enemy_rect = pygame.Rect(new_x, new_y, self.width, self.height)
        if not any(enemy_rect.colliderect(wall.get_rect()) for wall in walls if not wall.is_destroyed) and not enemy_rect.colliderect(player.get_rect()):
            self.x, self.y = new_x, new_y

    def shoot(self, bullets):
        if not self.is_alive:
            return  

        current_time = pygame.time.get_ticks()
        if current_time - self.last_shot_time > 2000:
            if self.direction == "UP":
                bullets.append(Bullet(self.x + self.width // 2, self.y, self.direction))
            elif self.direction == "DOWN":
                bullets.append(Bullet(self.x + self.width // 2, self.y + self.height, self.direction))
            elif self.direction == "LEFT":
                bullets.append(Bullet(self.x, self.y + self.height // 2, self.direction))
            elif self.direction == "RIGHT":
                bullets.append(Bullet(self.x + self.width, self.y + self.height // 2, self.direction))
            self.last_shot_time = current_time

    def draw(self, screen):
        if self.is_alive:
            screen.blit(self.textures[self.direction], (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def check_collision_with_bullet(self, bullet):
        enemy_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        bullet_rect = pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)

        if enemy_rect.colliderect(bullet_rect):
            self.die() 
            return True
        return False

    def die(self):
        self.is_alive = False  