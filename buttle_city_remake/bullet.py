import pygame

class Bullet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 10
        self.speed = 7
        self.direction = direction

        # Зображення кулі (можете змінити шлях до файлу)
        self.image = pygame.image.load("assets/images/other/bullet.png")
        self.image = pygame.transform.scale(self.image, (self.width, self.height))  # Масштабування кулі

    def move(self):
        # Рух кулі в залежності від напрямку
        if self.direction == "UP":
            self.y -= self.speed
        elif self.direction == "DOWN":
            self.y += self.speed
        elif self.direction == "LEFT":
            self.x -= self.speed
        elif self.direction == "RIGHT":
            self.x += self.speed

    def draw(self, screen):
        # Малювання кулі на екрані
        screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        # Повертає прямокутник кулі для колізій
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def check_collision_with_walls(self, walls):
        for wall in walls:
            if wall.get_rect().colliderect(self.get_rect()):
                return True
        return False