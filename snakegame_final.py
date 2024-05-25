import pygame
import random

pygame.init()

WHITE = (255, 183, 3)
YELLOW = (174, 217, 224)
BLACK = (149, 213, 178)
RED = (255, 166, 158)
GREEN = (247, 37, 133)
BLUE = (0, 18, 25)

DIS_WIDTH = 800
DIS_HEIGHT = 600

# Set font and font sizes
FONT_PATH = r"C:\Users\sharm\OneDrive\Desktop\c++\SuperPixel-m2L8j.ttf"
FONT_SIZE_LARGE = 25
FONT_SIZE_SMALL = 15

# Set the clock
clock = pygame.time.Clock()

# Initialize the game window
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake Game')

# Set fonts
font_style = pygame.font.Font(FONT_PATH, FONT_SIZE_LARGE)
menu_font = pygame.font.Font(FONT_PATH, FONT_SIZE_SMALL)

# Set block size and speed
snake_block = 10
snake_speed = 15

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, BLACK, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    mesg_rect = mesg.get_rect(center=(DIS_WIDTH / 2, DIS_HEIGHT / 2))
    dis.blit(mesg, mesg_rect.topleft)

def your_score(score):
    value = menu_font.render("Your Score: " + str(score), True, BLACK)
    value_rect = value.get_rect(center=(DIS_WIDTH / 2, DIS_HEIGHT / 6))
    dis.blit(value, value_rect.topleft)

def start_window():
    menu_options = ["Press 'S' to Start New Game", "Press 'R' to View Rules"]
    
    while True:
        dis.fill(BLUE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    gameLoop()
                elif event.key == pygame.K_r:
                    show_rules()

        for i, option in enumerate(menu_options):
            color = YELLOW
            text = menu_font.render(option, True, color)
            text_rect = text.get_rect(center=(DIS_WIDTH / 2, DIS_HEIGHT / 2 + i * 50))
            dis.blit(text, text_rect.topleft)

        pygame.display.update()
        clock.tick(10)

def gameLoop():
    game_over = False
    game_close = False

    x1 = DIS_WIDTH / 2
    y1 = DIS_HEIGHT / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, DIS_WIDTH - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, DIS_HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= DIS_WIDTH or x1 < 0 or y1 >= DIS_HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(BLUE)
        pygame.draw.rect(dis, GREEN, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, DIS_WIDTH - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, DIS_HEIGHT - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

def show_rules():
    rules_text = [
        "Rules of the Snake Game:",
        "",
        "1. Use arrow keys to control the snake's movement.",
        "2. The snake grows longer as it eats food.",
        "3. Avoid running into the walls or the snake's own body.",
        "4. The game ends if the snake collides with a wall or itself.",
        "5. Eat as much food as possible to increase your score.",
        "",
        "Press 'S' to Start the Game or any other key to go back to the menu."
    ]

    while True:
        dis.fill(BLUE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    gameLoop()
                else:
                    start_window()

        y_offset = 150
        for line in rules_text:
            text = menu_font.render(line, True, WHITE)
            text_rect = text.get_rect(center=(DIS_WIDTH / 2, y_offset))
            dis.blit(text, text_rect.topleft)
            y_offset += 20

        pygame.display.update()

start_window()
