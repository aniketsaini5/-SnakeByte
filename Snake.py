import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Load assets
background_image = pygame.image.load('bdj.jpg')  # Absolute path
start_sound = pygame.mixer.Sound('start.wav')
game_over_sound = pygame.mixer.Sound('end.wav')

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display dimensions
display_info = pygame.display.Info()
display_width = display_info.current_w
display_height = display_info.current_h

# Initialize game display
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

# Set clock
clock = pygame.time.Clock()

# Snake block size and speed
snake_block = 20
snake_speed = 15

# Font styles
font_style = pygame.font.SysFont('impact', 150)
score_font = pygame.font.SysFont(None, 38)

# Function to display the player's score
def display_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    display.blit(value, [0, 0])

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

# Function to display the end game message
def message(msg, color, position, font_size):
    font = pygame.font.SysFont(None, font_size)
    mesg = font.render(msg, True, color)
    display.blit(mesg, position)

# Function to draw a button with customizable font size
def draw_button(text, color, text_color, position, font_size=40):
    button_font = pygame.font.SysFont(None, font_size)
    button_surface = button_font.render(text, True, text_color)
    button_rect = button_surface.get_rect(center=position)
    pygame.draw.rect(display, color, button_rect.inflate(20, 10))  # Button background with padding
    display.blit(button_surface, button_rect)
    return button_rect

# Function to check for collision with food
def check_collision(x1, y1, foodx, foody, snake_block):
    if (x1 < foodx + snake_block and x1 + snake_block > foodx) and (y1 < foody + snake_block and y1 + snake_block > foody):
        return True
    return False

# Function to handle button clicks
def handle_buttons(mouse_pos):
    start_button_rect = pygame.Rect(display_width / 2 - 100, display_height / 2 - 50, 200, 50)
    quit_button_rect = pygame.Rect(display_width / 2 - 100, display_height / 2 + 50, 200, 50)
    if quit_button_rect.collidepoint(mouse_pos):
        return 'quit'
    if start_button_rect.collidepoint(mouse_pos):
        return 'play_again'
    return None

# Function to display the start screen
def show_start_screen():
    display.blit(background_image, [0, 0])
    
    # Display the game title
    title_font = pygame.font.SysFont('impact', 120)
    title_message = title_font.render("Snake byte", True, blue)
    display.blit(title_message, [display_width / 2 - title_message.get_width() / 2, display_height / 4 - title_message.get_height() / 2])
    
    # Draw Start Game button
    draw_button("Start Game", green, black, (display_width / 2, display_height / 2 - 50), font_size=70)
    # Draw Quit button
    draw_button("Quit", red, white, (display_width / 2, display_height / 2 + 50), font_size=70)
    
    # Display instructions
    instruction_font = pygame.font.SysFont(None, 25)
    start_instruction = instruction_font.render("Press Enter", True, white)
    quit_instruction = instruction_font.render("Press ESC", True, white)
    display.blit(start_instruction, [display_width / 2 - start_instruction.get_width() / 2, display_height / 2 - 10])
    display.blit(quit_instruction, [display_width / 2 - quit_instruction.get_width() / 2, display_height / 2 + 85])
    
    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter key
                    waiting = False
                elif event.key == pygame.K_ESCAPE:  # ESC key
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                action = handle_buttons(event.pos)
                if action == 'quit':
                    pygame.quit()
                    sys.exit()
                elif action == 'play_again':
                    waiting = False

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Display the start screen
    show_start_screen()

    x1 = display_width / 2
    y1 = display_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, display_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, display_height - snake_block) / snake_block) * snake_block

    # Play start sound
    start_sound.play()

    while not game_over:

        while game_close:
            display.blit(background_image, [0, 0])
            message("THE END", red, (display_width / 2 - 210, display_height / 2 - 200), font_size=150)
            draw_button("Quit [ESC]", red, white, (display_width / 2, display_height / 2 + 50), font_size=70)
            draw_button("Play Again [ENTER]", green, black, (display_width / 2, display_height / 2 + 150), font_size=70)
            display_score(length_of_snake - 1)
            pygame.display.update()

            # Stop the start sound and play the game over sound for 5 seconds
            start_sound.stop()
            game_over_sound.play()
            pygame.time.wait(6000)  # Wait for 5 seconds

            action_taken = False
            while not action_taken:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        action = handle_buttons(event.pos)
                        if action == 'quit':
                            pygame.quit()
                            sys.exit()
                        elif action == 'play_again':
                            gameLoop()
                            action_taken = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:  # ESC key
                            pygame.quit()
                            sys.exit()
                        elif event.key == pygame.K_RETURN:  # Enter key
                            gameLoop()
                            action_taken = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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
                elif event.key == pygame.K_ESCAPE:  # ESC key to quit
                    pygame.quit()
                    sys.exit()

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.blit(background_image, [0, 0])
        pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])  # Draw food after background
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(snake_block, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        if check_collision(x1, y1, foodx, foody, snake_block):
            foodx = round(random.randrange(0, display_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, display_height - snake_block) / snake_block) * snake_block
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

gameLoop()
