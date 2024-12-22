import pygame
import sys
from game_manager import GameManager
from player import Player
from bullet import Bullet
from create_map import create_map
from map_data import map_data

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Battle City Remake")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 60

game_manager = GameManager(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)
bullets = []

walls = create_map(map_data, SCREEN_WIDTH, SCREEN_HEIGHT)

shoot_sound = pygame.mixer.Sound("assets/shoot.wav")
pygame.mixer.music.load("assets/menu_music.mp3")
music_played = False

font = pygame.font.Font(None, 50)

while game_manager.running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_manager.running = False
        if event.type == pygame.KEYDOWN and game_manager.state == "menu":
            if event.key == pygame.K_SPACE:
                game_manager.load_screen("game")
                pygame.mixer.music.stop()
        if event.type == pygame.KEYDOWN and game_manager.state == "game":
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.x + player.width // 2, player.y))
                shoot_sound.play()

    if game_manager.state == "menu":
        if not music_played:
            pygame.mixer.music.play()
            music_played = True
        game_manager.update()
    elif game_manager.state == "game":
        player.move(keys, walls)
        for bullet in bullets:
            bullet.move()

        bullets = [bullet for bullet in bullets if bullet.y > 0 and not bullet.check_collision_with_walls(walls)]

        screen.fill(BLACK)
        for wall in walls:
            wall.draw(screen)
        player.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        pygame.display.flip()
    else:
        game_manager.update()

    clock.tick(FPS)

pygame.quit()
sys.exit()