import pygame
import time
import random
 
pygame.init()
 
# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
# Set screen dimensions
width = 600
height = 400

# Set block size and speed
block_size = 10
speed = 0.00005
 
clock = pygame.time.Clock()
FPS = 30  # or any other desired frame rate

# Create the game screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')
 
# Define the snake
def snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], block_size, block_size])
    pygame.display.update()

# # Define the food
# def food():
#     food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
#     food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
#     return food_x, food_y

def food(block_size):
    # Generate multiple food positions
    food_positions = []
    for i in range(3):
        food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0
        food_positions.append([food_x, food_y])
        
    # Draw each food at its position
    for pos in food_positions:
        pygame.draw.rect(screen, red, [pos[0], pos[1], block_size, block_size])
    
    # Return the list of food positions
    return food_positions


# Main game loop
def gameLoop():
    game_exit = False
    game_over = False

    # Set the starting position of the snake
    lead_x = width / 2
    lead_y = height / 2
    lead_x_change = 0
    lead_y_change = 0

    # Define the snake's starting length and position
    snake_list = []
    snake_length = 1

    # Generate the initial food positions
    food_positions = food(block_size)


    while not game_exit:

        # If the game is over, display the appropriate message
        while game_over == True:
            screen.fill(white)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render('Game Over!', True, red)
            screen.blit(message, [width / 2 - 100, height / 2 - 50])
            message2 = font_style.render('Press Q: Quit or A: Play Again', True, black)
            screen.blit(message2, [width / 2 - 200, height / 2 + 50])
            
            pygame.display.update()
            pygame.time.delay(100)

            # Handle the user's input to either quit or restart the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_a:
                        gameLoop()

        # Handle the user's input to move the snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
        clock.tick(FPS)  # Limit the frame rate to the desired FPS
        # Update the snake's position based on user input
        lead_x += lead_x_change
        lead_y += lead_y_change
        # Create the snake's head and append it to the snake list
        snake_head = []
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)

        # Remove the last block of the snake if its length exceeds snake_length
        if len(snake_list) > snake_length:
            del snake_list[0]

        # If the snake collides with the edges of the screen, end the game
        if lead_x >= width or lead_x < 0 or lead_y >= height or lead_y < 0:
            game_over = True

        
            
            # # Generate a new food location
            # food_x = round(random.randrange(0, width - block_size) / 10.0) * 10.0
            # food_y = round(random.randrange(0, height - block_size) / 10.0) * 10.0    
        # Draw the snake on the screen
        screen.fill(white)
        
        # food(food_x, food_y)
        # pygame.draw.rect(screen, red, [food_x, food_y, block_size, block_size])
         # Draw the food
        # pygame.display.update()
        for pos in food_positions:
            pygame.draw.rect(screen, red, [pos[0], pos[1], block_size, block_size])
        
        # for pos in food_positions:
            # Check if the snake's head collides with the food
        if (lead_x, lead_y) in food_positions:
            # Increase the snake's length
            snake_length += 1
            # Remove the food that the snake ate from the list
            # food_positions.remove((lead_x, lead_y))
            # # Add a new food to the list
            # food_positions.append(generate_food_position())
            # Add a new block to the snake's body
            last_block = snake_list[-1]
            new_block = (last_block[0]+block_size, last_block[1]+block_size)
            # if direction == "right":
            #     new_block = (last_block[0]-block_size, last_block[1])
            # elif direction == "left":
            #     new_block = (last_block[0]+block_size, last_block[1])
            # elif direction == "up":
            #     new_block = (last_block[0], last_block[1]+block_size)
            # elif direction == "down":
            #     new_block = (last_block[0], last_block[1]-block_size)
            snake_list.append(new_block)
            snake(block_size, snake_list)
        snake(block_size, snake_list)
        pygame.display.update()
        # clock.tick(speed)

    # Quit the game
    pygame.quit()
    quit()


gameLoop()



