import pygame
import random

pygame.init()

# Screen
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pet Food Collection Game")

# Load background image
background = pygame.image.load("white bg.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Pet class
class Pet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 200, 0))

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= 5

        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        if keys[pygame.K_UP]:
            self.rect.y -= 5

        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        # Keep pet inside the screen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


# Food class
class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 150, 0))

        self.rect = self.image.get_rect()

        # Random position
        self.rect.x = random.randint(0, WIDTH - 30)
        self.rect.y = random.randint(0, HEIGHT - 30)


# Create pet
pet = Pet()

# Create sprite groups
all_sprites = pygame.sprite.Group()
food_group = pygame.sprite.Group()

all_sprites.add(pet)

# Create 10 food items
for i in range(10):
    food = Food()
    food_group.add(food)
    all_sprites.add(food)


# Named system font
font = pygame.font.SysFont("Arial", 50)

# Game loop
clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update pet
    pet.update()

    # Detect food collision
    collected = pygame.sprite.spritecollide(
        pet,
        food_group,
        True
    )

    # Draw background
    screen.blit(background, (0, 0))

    # Draw sprites
    all_sprites.draw(screen)

    # Check if all food is collected
    if len(food_group) == 0:

        message = font.render(
            "All Food Collected!",
            True,
            WHITE
        )

        message_rect = message.get_rect(
            center=(WIDTH // 2, HEIGHT // 2)
        )

        screen.blit(message, message_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()