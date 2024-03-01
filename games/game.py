import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define constants
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SIZE = 20
PADDLE_SPEED = 5
BALL_SPEED_X = 3
BALL_SPEED_Y = 3

# Create paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, up_key, down_key):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, HEIGHT // 2)
        self.up_key = up_key
        self.down_key = down_key

    def update(self):
        keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if keys[self.up_key]:
                self.rect.y -= PADDLE_SPEED
        if self.rect.bottom < HEIGHT:
            if keys[self.down_key]:
                self.rect.y += PADDLE_SPEED

# Create ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = BALL_SPEED_X * random.choice((1, -1))
        self.speed_y = BALL_SPEED_Y * random.choice((1, -1))

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Ball collision with walls
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1
        if self.rect.left <= 0:
            # If the ball hits the left side, player 2 scores
            self.rect.center = (WIDTH // 2, HEIGHT // 2)
            self.speed_x *= -1
            return "player2"
        if self.rect.right >= WIDTH:
            # If the ball hits the right side, player 1 scores
            self.rect.center = (WIDTH // 2, HEIGHT // 2)
            self.speed_x *= -1
            return "player1"

# Create sprite groups
all_sprites = pygame.sprite.Group()
paddles = pygame.sprite.Group()
ball_sprites = pygame.sprite.Group()

# Create paddles
player1 = Paddle(PADDLE_WIDTH, pygame.K_w, pygame.K_s)
player2 = Paddle(WIDTH - PADDLE_WIDTH, pygame.K_UP, pygame.K_DOWN)
all_sprites.add(player1, player2)
paddles.add(player1, player2)

# Create ball
ball = Ball()
all_sprites.add(ball)
ball_sprites.add(ball)

# Scores
player1_score = 0
player2_score = 0

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Ball collision with paddles
    hits = pygame.sprite.spritecollide(ball, paddles, False)
    if hits:
        ball.speed_x *= -1

    # Check for scoring
    score = ball.update()
    if score == "player1":
        player1_score += 1
    elif score == "player2":
        player2_score += 1

    # Draw
    screen.fill(BLACK)
    all_sprites.draw(screen)
    
    # Display scores
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Player 1: {player1_score}  Player 2: {player2_score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
