
'''
def game(hiddenNumber, low, high):
    if low > high:
        return "Error"

    mid = (low + high) // 2
    print(f"Is the number {mid}?")

    answ = input("Enter 'H' for higher, 'L' for lower, or 'Y' if correct: ").strip().lower()

    if answ == "h":
        return game(hiddenNumber, mid + 1, high)
    elif answ == "l":
        return game(hiddenNumber, low, mid - 1)
    elif answ == "y":
        return f"Game Over: The hidden number was {hiddenNumber}!"
    else:
        print("Invalid input. Please type 'H', 'L', or 'Y'.")
        return game(hiddenNumber, low, high)


hiddenNumber = random.randint(1, 100)
print("Welcome to the Guessing Game!")
print("guess a number from 1 to 100.")
print(game(hiddenNumber, 1, 100))

'''

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guessing Game")

#ICON = pygame.image.load("icon.png")

#pygame.display.set_icon(pygame.image.load(ICON)

#BACKGROUND = pygame.image.load("images/background.jpg")

#FONT = pygame.font.SysFont()

CLOCK = pygame.time.Clock()


def test():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Код отображения

        SCREEN.fill(("white"))
        square_size = 100
        square_position = (WIDTH // 2 - square_size // 2, HEIGHT // 2 - square_size // 2)
        pygame.draw.rect(SCREEN, "blue", (*square_position, square_size, square_size))

        pygame.display.update()

        CLOCK.tick(30)

test()