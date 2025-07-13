import pygamen has occurred: ModuleNotFoundError
No module named 'py
import random
import time

# Initialize pygame
pygame.init()

# Game window dimensions
WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for FPS
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 25)


def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))


def draw_food(food_position):
    pygame.draw.rect(window, RED, (food_position[0], food_position[1], CELL_SIZE, CELL_SIZE))


def show_score(score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, [10, 10])


def game_over(score):
    window.fill(BLACK)
    message = font.render("Game Over! Score: " + str(score), True, WHITE)
    window.blit(message, [WIDTH // 3, HEIGHT // 3])
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    quit()


def main():
    snake = [[100, 50]]
    direction = 'RIGHT'
    change_to = direction
    score = 0

    food = [random.randrange(0, WIDTH, CELL_SIZE),
            random.randrange(0, HEIGHT, CELL_SIZE)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Arrow key input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        direction = change_to
        head_x, head_y = snake[0]

        if direction == 'UP':
            head_y -= CELL_SIZE
        elif direction == 'DOWN':
            head_y += CELL_SIZE
        elif direction == 'LEFT':
            head_x -= CELL_SIZE
        elif direction == 'RIGHT':
            head_x += CELL_SIZE

        new_head = [head_x, head_y]

        # Game Over Conditions
        if (
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            new_head in snake
        ):
            game_over(score)

        snake.insert(0, new_head)

        # Snake eats food
        if head_x == food[0] and head_y == food[1]:
            score += 1
            food = [random.randrange(0, WIDTH, CELL_SIZE),
                    random.randrange(0, HEIGHT, CELL_SIZE)]
        else:
            snake.pop()

        window.fill(BLACK)
        draw_snake(snake)
        draw_food(food)
        show_score(score)
        pygame.display.update()
        clock.tick(10)  # control speed


if __name__ == "__main__":
    main()
