import pygame
from src.board import Board

pygame.init()
pygame.font.init()
SIZE = WIDTH, HEIGHT = (600,400)
BGCOLOR = (0,0,0)

window = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
pygame.display.set_caption("Biogus")
clock = pygame.time.Clock()

BOARD_DIM = (10,10)
BOARD_BASE_POSITION = (100,600,0)
NOISE_RANGE = (-10,10)
POINT_DISTANCE =20
myboard = Board(BOARD_DIM, BOARD_BASE_POSITION,NOISE_RANGE, POINT_DISTANCE)

def main():
    running = True

    while running:
        clock.tick(60)
        window.fill(BGCOLOR)

        myboard.update()

        myboard.show(window)

        pygame.display.update()


if __name__ == '__main__':
    main()