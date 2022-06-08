import doctest
from email.mime import base
import time
import pygame

SPACE_PER_PEG = 200

def hanoi(pegs, start, target, n):
    assert len(pegs[start]) >= n
    if n == 1:
        pegs[target].append(pegs[start].pop())
        yield pegs
    else:
        aux = 3 - start - target
        for i in hanoi(pegs, start, aux, n-1): yield i
        for i in hanoi(pegs, start, target, 1): yield i
        for i in hanoi(pegs, aux, target, n-1): yield i

def display_pile_of_pegs(pegs, start_x, start_y, peg_height, screen):
    for i, pegwidth in enumerate(pegs):

        pygame.draw.rect(
            screen,
            (255-pegwidth, 255-pegwidth, 255-pegwidth),
            (
                start_x + (SPACE_PER_PEG - pegwidth)/2 ,
                start_y - peg_height * i,
                pegwidth,
                peg_height
            )
        )

def visual_hanoi_simulation(number_of_pegs, base_width, peg_height, sleeping_interval):
    pegs = [[i * base_width for i in reversed(range(1,number_of_pegs+1))],[], []]
    positions = hanoi(pegs, 0, 2, number_of_pegs)

    pygame.init()
    screen = pygame.display.set_mode((650, 650))
    pygame.display.set_caption('Torre de Hanoi')

    for position in positions:
        screen.fill((255, 255, 255))
        for i, pile in enumerate(position):
            display_pile_of_pegs(pile, 50 + SPACE_PER_PEG * i, 500, peg_height, screen)
        pygame.display.update()
        time.sleep(sleeping_interval)
    
    pygame.quit()

if __name__ == "__main__":
    doctest.testmod()
    visual_hanoi_simulation(
        number_of_pegs= 4,
        base_width= 30,
        peg_height= 40,
        sleeping_interval= 0.5
    )
    visual_hanoi_simulation(
        number_of_pegs= 8,
        base_width= 20,
        peg_height= 30,
        sleeping_interval= 0.2
    )
