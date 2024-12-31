import pygame
import random
import json

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quiz Tower Defense")
clock = pygame.time.Clock()

# Fonts and colors
FONT = pygame.font.Font(None, 36)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

with open("c:/Users/alvin/code/python/games/towerDefense/questions.json", "r") as file:
    questions = json.load(file)

# Game variables
current_question = random.choice(questions)
score = 0
wave = 1
lives = 3

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.hover_color if self.is_hovered else self.color, self.rect)
        text_surface = FONT.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def check_click(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

buttons = []
button_width, button_height = 300, 50
button_y_start = 300
button_spacing = 20
for i, option in enumerate(current_question["options"]):
    button_x = (WIDTH - button_width) // 2
    button_y = button_y_start + i * (button_height + button_spacing)
    button = Button(button_x, button_y, button_width, button_height, option, GREEN, BLUE)
    buttons.append(button)

# Main game loop
running = True
questioning = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttons:
                if button.check_click(mouse_pos):
                    if button.text == current_question["answer"]:
                        score += 1
                        questioning = False
                        screen.fill(GREEN)
                        correctText = FONT.render("Correct!", True, WHITE)
                        correctTextRect = correctText.get_rect(center=(WIDTH // 2, HEIGHT // 2))
                        correctText.blit(screen, correctTextRect)
                        lastNotQuestioning = pygame.time.get_ticks()
                    else:
                        lives -= 1
                        print("Incorrect!")

                    
                    elapsedTime = pygame.time.get_ticks() - lastNotQuestioning
                    
                    # Load a new question or end the game
                    if lives > 0:
                        current_question = random.choice(questions)
                        buttons = []
                        for i, option in enumerate(current_question["options"]):
                            button_y = button_y_start + i * (button_height + button_spacing)
                            button = Button(button_x, button_y, button_width, button_height, option, GREEN, BLUE)
                            buttons.append(button)
                    else:
                        print("Game Over!")
                        running = False

    # Update button hover states
    mouse_pos = pygame.mouse.get_pos()
    for button in buttons:
        button.check_hover(mouse_pos)

    if elapsedTime >= 1000:
        questioning = True
        question_text = FONT.render(current_question["question"], True, WHITE)
        if questioning:
            # Draw question
            screen.blit(question_text, (20, 20))
    # Draw buttons
    for button in buttons:
        button.draw(screen)

    # Draw score and lives
    score_text = FONT.render(f"Score: {score}", True, WHITE)
    lives_text = FONT.render(f"Lives: {lives}", True, WHITE)
    screen.blit(score_text, (WIDTH - 150, 20))
    screen.blit(lives_text, (WIDTH - 150, 60))

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

