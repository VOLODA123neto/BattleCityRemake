import pygame
from bullet import Bullet

WHITE = (255, 255, 255)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.speed = 5
        self.direction = "UP"
        self.lives = 3 

        self.textures = {
            "UP": pygame.image.load("assets/tank_up.png"),
            "DOWN": pygame.image.load("assets/tank_down.png"),
            "LEFT": pygame.image.load("assets/tank_left.png"),
            "RIGHT": pygame.image.load("assets/tank_right.png")
        }
        
        for key in self.textures:
            self.textures[key] = pygame.transform.scale(self.textures[key], (self.width, self.height))

    def move(self, keys, walls, enemies):
        new_x, new_y = self.x, self.y

        if keys[pygame.K_w]:
            new_y -= self.speed
            self.direction = "UP"
        if keys[pygame.K_s]:
            new_y += self.speed
            self.direction = "DOWN"
        if keys[pygame.K_a]:
            new_x -= self.speed
            self.direction = "LEFT"
        if keys[pygame.K_d]:
            new_x += self.speed
            self.direction = "RIGHT"

        player_rect = pygame.Rect(new_x, new_y, self.width, self.height)

        if not any(player_rect.colliderect(wall.get_rect()) for wall in walls if not wall.is_destroyed) and \
           not any(player_rect.colliderect(enemy.get_rect()) for enemy in enemies):
            self.x, self.y = new_x, new_y

    def draw(self, screen):
        screen.blit(self.textures[self.direction], (self.x, self.y))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def shoot(self, bullets):
        bullet = Bullet(self.x + self.width // 2, self.y, self.direction)
        bullets.append(bullet)

    def take_damage(self):
        self.lives -= 1
        print(f"Player lives: {self.lives}")
        if self.lives <= 0:
            print("Game Over!")

    def check_collision_with_enemy(self, enemy):
        player_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)

        if player_rect.colliderect(enemy_rect):
            self.take_damage()
            return True
        return False