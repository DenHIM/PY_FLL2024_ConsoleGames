import asyncio
import pygame

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)

pygame.init()
clock = pygame.time.Clock()

def new_screen(title):
    global screen
    pygame.display.set_caption(title)
    screen = pygame.display.set_mode((640, 360))
    return screen

async def main():
  # using the whole display.
  screen = new_screen("TEST")

  count = 10

  while True:
      print(f"{count}: Hello from Pygame")
      print("=== Started game loop ===")
      screen.fill(WHITE)
      pygame.draw.rect(screen, GREEN, (20, 20, 40, 40))
      pygame.display.update()
      await asyncio.sleep(0)  # You must include this statement in your main loop. Keep the argument at 0.

      if not count:
          print("=== exiting ===")
          pygame.quit()
          return
      
      count -= 1
      clock.tick(60)

asyncio.run(main())