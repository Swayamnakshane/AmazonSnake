import pygame
import random
import sys
import time
import math

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 100, 0)
GRAY = (100, 100, 100)
PINK = (255, 192, 203)
WALL_COLOR = (139, 69, 19)  # Brown color for walls

# Game dimensions
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080
BLOCK_SIZE = 20

# Initialize the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Game clock
clock = pygame.time.Clock()
FPS = 10  # Set to 10 for moderate snake movement speed

# Fonts
font = pygame.font.SysFont('arial', 50)
small_font = pygame.font.SysFont('arial', 35)

# Load sound (optional)
try:
    eat_sound = pygame.mixer.Sound('eat.wav')
except:
    eat_sound = None
    print("Sound file not found. Game will run without sound.")

# Create maze walls
def create_maze():
    """Create maze walls"""
    walls = []

    # Create some horizontal walls
    walls.append(pygame.Rect(400, 300, 400, BLOCK_SIZE))
    walls.append(pygame.Rect(1000, 300, 500, BLOCK_SIZE))
    walls.append(pygame.Rect(400, 700, 600, BLOCK_SIZE))
    walls.append(pygame.Rect(1200, 700, 300, BLOCK_SIZE))

    # Create some vertical walls
    walls.append(pygame.Rect(600, 400, BLOCK_SIZE, 300))
    walls.append(pygame.Rect(1200, 400, BLOCK_SIZE, 300))
    walls.append(pygame.Rect(800, 100, BLOCK_SIZE, 200))
    walls.append(pygame.Rect(800, 700, BLOCK_SIZE, 200))

    # Create some L-shaped walls
    walls.append(pygame.Rect(300, 500, 200, BLOCK_SIZE))
    walls.append(pygame.Rect(300, 500, BLOCK_SIZE, 150))

    walls.append(pygame.Rect(1400, 500, 200, BLOCK_SIZE))
    walls.append(pygame.Rect(1400, 500, BLOCK_SIZE, 150))

    return walls

# Create the maze
maze_walls = create_maze()

def display_score(score):
    """Display the current score on the screen"""
    score_text = font.render(f"Score: {score}", True, WHITE)
    window.blit(score_text, [10, 10])

def draw_snake(snake_blocks):
    """Draw the snake on the screen with normal green color and oval face with eyes"""
    for i, block in enumerate(snake_blocks):
        # Snake head with oval face and eyes
        if i == len(snake_blocks) - 1:  # Snake head
            # Draw the main head block (slightly oval by making it wider)
            head_width = int(BLOCK_SIZE * 1.3)
            head_rect = pygame.Rect(block[0] - (head_width - BLOCK_SIZE) // 2, block[1], head_width, BLOCK_SIZE)
            pygame.draw.ellipse(window, GREEN, head_rect)

            # Determine eye direction based on movement
            eye_offset_x = 0
            eye_offset_y = 0

            # Adjust eye position based on direction
            if len(snake_blocks) > 1:
                prev_block = snake_blocks[-2]
                if block[0] > prev_block[0]:  # Moving right
                    eye_offset_x = 4
                    eye_offset_y = 0
                elif block[0] < prev_block[0]:  # Moving left
                    eye_offset_x = -4
                    eye_offset_y = 0
                elif block[1] > prev_block[1]:  # Moving down
                    eye_offset_x = 0
                    eye_offset_y = 4
                elif block[1] < prev_block[1]:  # Moving up
                    eye_offset_x = 0
                    eye_offset_y = -4

            # Draw eyes (white part)
            left_eye_x = block[0] + BLOCK_SIZE // 4 - 2 + eye_offset_x
            right_eye_x = block[0] + 3 * BLOCK_SIZE // 4 - 2 + eye_offset_x
            eye_y = block[1] + BLOCK_SIZE // 3 + eye_offset_y

            pygame.draw.ellipse(window, WHITE, [left_eye_x, eye_y, 6, 6])
            pygame.draw.ellipse(window, WHITE, [right_eye_x, eye_y, 6, 6])

            # Draw pupils (black part)
            pygame.draw.ellipse(window, BLACK, [left_eye_x + 2, eye_y + 2, 3, 3])
            pygame.draw.ellipse(window, BLACK, [right_eye_x + 2, eye_y + 2, 3, 3])

        else:
            # Normal green body
            pygame.draw.rect(window, DARK_GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])
            # Add a small highlight to make segments more distinct
            highlight = pygame.Rect(block[0] + 2, block[1] + 2, BLOCK_SIZE - 4, BLOCK_SIZE - 4)
            pygame.draw.rect(window, GREEN, highlight)

def draw_food(x, y):
    """Draw food as a mouse"""
    # Mouse body (gray oval)
    mouse_body = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
    pygame.draw.ellipse(window, GRAY, mouse_body)

    # Mouse head (slightly darker gray)
    head_size = BLOCK_SIZE // 2
    head_x = x + BLOCK_SIZE - head_size // 2
    head_y = y + (BLOCK_SIZE - head_size) // 2
    mouse_head = pygame.Rect(head_x, head_y, head_size, head_size)
    pygame.draw.ellipse(window, (80, 80, 80), mouse_head)

    # Mouse ears
    ear_size = BLOCK_SIZE // 4
    pygame.draw.ellipse(window, PINK, [head_x, head_y - ear_size // 2, ear_size, ear_size])
    pygame.draw.ellipse(window, PINK, [head_x + head_size - ear_size, head_y - ear_size // 2, ear_size, ear_size])

    # Mouse eyes
    eye_size = BLOCK_SIZE // 8
    pygame.draw.ellipse(window, BLACK, [head_x + head_size - eye_size - 1, head_y + head_size // 3, eye_size, eye_size])

    # Mouse tail
    tail_start_x = x
    tail_start_y = y + BLOCK_SIZE // 2
    tail_end_x = x - BLOCK_SIZE // 2
    tail_end_y = y + BLOCK_SIZE // 2 - BLOCK_SIZE // 4
    pygame.draw.line(window, GRAY, (tail_start_x, tail_start_y), (tail_end_x, tail_end_y), 2)

def draw_walls():
    """Draw the maze walls"""
    # Draw border walls
    pygame.draw.rect(window, WALL_COLOR, [0, 0, WINDOW_WIDTH, BLOCK_SIZE])  # Top
    pygame.draw.rect(window, WALL_COLOR, [0, WINDOW_HEIGHT - BLOCK_SIZE, WINDOW_WIDTH, BLOCK_SIZE])  # Bottom
    pygame.draw.rect(window, WALL_COLOR, [0, 0, BLOCK_SIZE, WINDOW_HEIGHT])  # Left
    pygame.draw.rect(window, WALL_COLOR, [WINDOW_WIDTH - BLOCK_SIZE, 0, BLOCK_SIZE, WINDOW_HEIGHT])  # Right

    # Draw maze walls
    for wall in maze_walls:
        pygame.draw.rect(window, WALL_COLOR, wall)
        # Add texture to walls
        for i in range(0, wall.width, BLOCK_SIZE):
            for j in range(0, wall.height, BLOCK_SIZE):
                if i + BLOCK_SIZE <= wall.width and j + BLOCK_SIZE <= wall.height:
                    pygame.draw.line(window, (160, 82, 45),
                                    (wall.x + i, wall.y + j),
                                    (wall.x + i + BLOCK_SIZE, wall.y + j + BLOCK_SIZE), 1)
                    pygame.draw.line(window, (160, 82, 45),
                                    (wall.x + i, wall.y + j + BLOCK_SIZE),
                                    (wall.x + i + BLOCK_SIZE, wall.y + j), 1)

def generate_food():
    """Generate food at a random position that's not on a wall"""
    valid_position = False
    food_x, food_y = 0, 0

    while not valid_position:
        food_x = round(random.randrange(BLOCK_SIZE, WINDOW_WIDTH - 2*BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        food_y = round(random.randrange(BLOCK_SIZE, WINDOW_HEIGHT - 2*BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

        # Check if food is on a wall
        food_rect = pygame.Rect(food_x, food_y, BLOCK_SIZE, BLOCK_SIZE)
        valid_position = True

        # Check against maze walls
        for wall in maze_walls:
            if food_rect.colliderect(wall):
                valid_position = False
                break

    return food_x, food_y

def check_collision_with_walls(x, y):
    """Check if the snake collides with any wall"""
    snake_rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)

    # Check border walls
    if (x < BLOCK_SIZE or x >= WINDOW_WIDTH - BLOCK_SIZE or
        y < BLOCK_SIZE or y >= WINDOW_HEIGHT - BLOCK_SIZE):
        return True

    # Check maze walls
    for wall in maze_walls:
        if snake_rect.colliderect(wall):
            return True

    return False

def display_message(msg, color, y_displacement=0):
    """Display a message on the screen"""
    message = font.render(msg, True, color)
    message_rect = message.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 + y_displacement))
    window.blit(message, message_rect)

def game_over_screen(score):
    """Display game over screen with final score and restart option"""
    window.fill(BLACK)
    display_message("GAME OVER", RED)
    display_message(f"Your Score: {score}", WHITE, 50)
    display_message("Press R to Restart or Q to Quit", WHITE, 100)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    waiting = False
                    game_loop()

def game_loop():
    """Main game loop"""
    # Initial snake position and direction
    x = WINDOW_WIDTH / 2
    y = WINDOW_HEIGHT / 2
    x_change = BLOCK_SIZE
    y_change = 0

    # Snake body
    snake_blocks = []
    snake_length = 1

    # Generate first food
    food_x, food_y = generate_food()

    # Score
    score = 0

    # Game state
    game_over = False
    paused = False

    # Main game loop
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle key presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = BLOCK_SIZE
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = BLOCK_SIZE
                    x_change = 0
                elif event.key == pygame.K_p:  # Pause game when 'P' is pressed
                    paused = not paused
                    if paused:
                        # Display pause message
                        pause_text = font.render("PAUSED - Press P to Continue", True, WHITE)
                        pause_rect = pause_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
                        window.blit(pause_text, pause_rect)
                        pygame.display.update()

        # Skip game logic if paused
        if paused:
            clock.tick(FPS)
            continue

        # Update snake position
        x += x_change
        y += y_change

        # Check for collision with walls
        if check_collision_with_walls(x, y):
            game_over_screen(score)

        # Fill the background
        window.fill(BLACK)

        # Draw walls
        draw_walls()

        # Draw food as a mouse
        draw_food(food_x, food_y)

        # Update snake
        snake_head = [x, y]
        snake_blocks.append(snake_head)

        if len(snake_blocks) > snake_length:
            del snake_blocks[0]

        # Check if snake hits itself
        for block in snake_blocks[:-1]:
            if block == snake_head:
                game_over_screen(score)

        # Draw snake
        draw_snake(snake_blocks)

        # Display score
        display_score(score)

        # Update display
        pygame.display.update()

        # Check if snake eats food
        if x == food_x and y == food_y:
            food_x, food_y = generate_food()
            snake_length += 1
            score += 10

            # Play sound if available
            if eat_sound:
                eat_sound.play()

        # Control game speed
        clock.tick(FPS)

# Start the game
def main():
    window.fill(BLACK)
    display_message("Snake Game", GREEN)
    display_message("Press any key to start", WHITE, 50)
    display_message("Press P to pause during game", WHITE, 100)
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

    game_loop()

if __name__ == "__main__":
    main()
