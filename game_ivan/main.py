import asyncio
import pygame
import random
import time



# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 4, 4
CARD_WIDTH, CARD_HEIGHT = WIDTH // COLS, HEIGHT // ROWS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (196, 196, 196)
GREEN = (0, 255, 0)

# load my images
def load_images():
    images = []
    for i in range(8):
        image = pygame.image.load(f'image_{i}.png') #loading all images one by one
        image = pygame.transform.scale(image, (CARD_WIDTH, CARD_HEIGHT))
        images.append(image)
    return images

async def main():
    # Function to draw the cards
    def draw_cards():
        for i in range(ROWS):
            for j in range(COLS):
                card_index = i * COLS + j
                if card_index in matched or card_index in flipped:
                    screen.blit(images[card_index], (j * CARD_WIDTH, i * CARD_HEIGHT))
                else:
                    pygame.draw.rect(screen, GRAY, (j * CARD_WIDTH, i * CARD_HEIGHT, CARD_WIDTH, CARD_HEIGHT))

    images = load_images()
    images = images * 2
    random.shuffle(images) #shuffle images in list

    # Game screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ivan's Memory Match Game - 2024")

    # Game variables
    matched = []
    flipped = []
    running = True
    first_click = None

    counter = 0    #counter of clicks         

    # Main game loop
    while running:
        screen.fill(WHITE)
        draw_cards()
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                counter = counter + 1
                print("%d clicks "% counter)
                x, y = event.pos
                row, col = y // CARD_HEIGHT, x // CARD_WIDTH
                card_index = row * COLS + col

                if card_index not in flipped and card_index not in matched:
                    flipped.append(card_index)

                    if first_click is None:
                        first_click = card_index
                    else:
                        if images[first_click] == images[card_index]:
                            matched.append(first_click)
                            matched.append(card_index)
                        time.sleep(0.5) #how long to show your image
                        flipped = []
                        first_click = None
        
        await asyncio.sleep(0)  # You must include this statement in your main loop. Keep the argument at 0.

        if len(matched) == len(images):
            print("You won!")
            print("and finished at %d clicks!" % counter) 
            running = False

    pygame.quit()
    return

asyncio.run(main())
