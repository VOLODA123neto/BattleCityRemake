import pygame

WHITE = (255, 255, 255)

class GameManager:
    def __init__(self, screen, screen_width, screen_height):
        self.running = True
        self.state = "menu"
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.menu_image = pygame.image.load("assets/menu_background.png")
        self.menu_image = pygame.transform.scale(self.menu_image, (self.screen_width, self.screen_height)) 

    def load_screen(self, state):
        self.state = state

    def update(self):
        if self.state == "menu":
            self.show_menu()
        elif self.state == "victory":
            self.show_victory()
        elif self.state == "defeat":
            self.show_defeat()

    def show_menu(self):
        self.screen.blit(self.menu_image, (0, 0))
        font = pygame.font.SysFont("Arial", 36)
        text = font.render("Press SPACE to Start", True, WHITE)
        self.screen.blit(text, (self.screen_width // 2 - 150, 300))
        pygame.display.flip()

    def show_victory(self):
        self.screen.fill(WHITE)
        font = pygame.font.SysFont("Arial", 36)
        text = font.render("You Win!", True, WHITE)
        self.screen.blit(text, (self.screen_width // 2 - 100, self.screen_height // 2))
        pygame.display.flip()

    def show_defeat(self):
        self.screen.fill(WHITE)
        font = pygame.font.SysFont("Arial", 36)
        text = font.render("Game Over!", True, WHITE)
        self.screen.blit(text, (self.screen_width // 2 - 150, self.screen_height // 2))
        pygame.display.flip()