import pygame

class Wall:
    def __init__(self, x, y, width, height, wall_type):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.wall_type = wall_type
        self.is_destroyed = False

        # Залежно від типу стіни завантажуємо відповідне зображення
        if self.wall_type == 1:
            self.image = pygame.image.load("assets/images/walls/indestructible_wall.png")
        elif self.wall_type == 2:
            self.image = pygame.image.load("assets/images/walls/destroyable_wall.png")
        elif self.wall_type == 3:
            self.image = pygame.image.load("assets/images/walls/passable_wall.png")
        elif self.wall_type == 4:  # Невидимий бар'єр (не має текстури)
            self.image = None  # Для невидимого бар'єра зображення не потрібне

        # Перетворюємо зображення на відповідний розмір
        if self.image:
            self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def draw(self, screen):
        if not self.is_destroyed and self.image:  # Перевірка, щоб не малювати, якщо зображення відсутнє
            screen.blit(self.image, (self.x, self.y))

    def get_rect(self):
        if not self.is_destroyed:
            return pygame.Rect(self.x, self.y, self.width, self.height)
        return pygame.Rect(0, 0, 0, 0)

    def check_collision_with_bullet(self, bullet):
        if self.wall_type == 2 and not self.is_destroyed:
            if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(
                pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
            ):
                self.is_destroyed = True
                return True
        elif self.wall_type == 1:
            if pygame.Rect(self.x, self.y, self.width, self.height).colliderect(
                pygame.Rect(bullet.x, bullet.y, bullet.width, bullet.height)
            ):
                return True
        return False