import pygame
import random

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders - Part 1")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Player Sprite
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 50)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Keep player inside screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH


# Enemy Sprite
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((40, 30))
        self.image.fill(RED)

        self.rect = self.image.get_rect()

        # Random position
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = random.randint(50, 300)


# Create player
player = Player()

# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

all_sprites.add(player)

# Create 7 enemies
for i in range(7):
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)


# Score
score = 0

# Font
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update sprites
    all_sprites.update()

    # Check collision between player and enemies
    collisions = pygame.sprite.spritecollide(
        player,
        enemies,
        True
    )

    # Increase score for every collision
    score += len(collisions)

    # Draw
    screen.fill(BLACK)

    all_sprites.draw(screen)

    # Display score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()