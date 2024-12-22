import pygame

WHITE = (255, 255, 255)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 40
        self.speed = 5
        self.direction = "UP"  

        self.textures = {
            "UP": pygame.image.load("assets/tank_up.png"),
            "DOWN": pygame.image.load("assets/tank_down.png"),
            "LEFT": pygame.image.load("assets/tank_left.png"),
            "RIGHT": pygame.image.load("assets/tank_right.png")
        }
        
        self.textures["UP"] = pygame.transform.scale(self.textures["UP"], (self.width, self.height))
        self.textures["DOWN"] = pygame.transform.scale(self.textures["DOWN"], (self.width, self.height))
        self.textures["LEFT"] = pygame.transform.scale(self.textures["LEFT"], (self.width, self.height))
        self.textures["RIGHT"] = pygame.transform.scale(self.textures["RIGHT"], (self.width, self.height))

    def move(self, keys, walls):
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
        if not any(player_rect.colliderect(wall.get_rect()) for wall in walls):
            self.x, self.y = new_x, new_y

    def draw(self, screen):
        screen.blit(self.textures[self.direction], (self.x, self.y))