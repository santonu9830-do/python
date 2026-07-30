import pygame

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Smart Traffic Signal Simulator")

clock = pygame.time.Clock()

# Custom Event
SIGNAL_CHANGE = pygame.USEREVENT + 1

# Colors
WHITE = (255, 255, 255)
GRAY = (60, 60, 60)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 120, 255)
YELLOW = (255, 255, 0)


# -----------------------------
# Car Sprite Class
# -----------------------------
class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface((60, 30))
        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = HEIGHT // 2 - 15

        self.velocity = 4

    def update(self):
        self.rect.x += self.velocity

        # When car reaches boundary,
        # post a custom event
        if self.rect.right >= WIDTH - 50:
            pygame.event.post(
                pygame.event.Event(SIGNAL_CHANGE)
            )


# -----------------------------
# Create Sprite Group
# -----------------------------
all_sprites = pygame.sprite.Group()

car = Car()
all_sprites.add(car)

# Traffic Signal State
signal_green = True

running = True

while running:

    # -------------------------
    # Event Handling
    # -------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == SIGNAL_CHANGE:

            # Toggle traffic signal
            signal_green = not signal_green

            # Change car color
            if signal_green:
                car.image.fill(BLUE)
                car.rect.left = 50
            else:
                car.image.fill(YELLOW)

    # -------------------------
    # Update
    # -------------------------
    if signal_green:
        all_sprites.update()

    # -------------------------
    # Draw
    # -------------------------
    screen.fill(WHITE)

    # Road
    pygame.draw.rect(
        screen,
        GRAY,
        (0, HEIGHT // 2 - 40, WIDTH, 80)
    )

    # Traffic Signal Pole
    pygame.draw.rect(
        screen,
        (50, 50, 50),
        (WIDTH - 70, HEIGHT // 2 - 100, 10, 100)
    )

    # Traffic Signal Light
    signal_color = GREEN if signal_green else RED
    pygame.draw.circle(
        screen,
        signal_color,
        (WIDTH - 65, HEIGHT // 2 - 110),
        15
    )

    # Draw Sprites
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()