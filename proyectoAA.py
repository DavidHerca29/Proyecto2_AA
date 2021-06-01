import pygame, math

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()


def drawTree(x1, y1, angle, depth, decremento, pixeles):
    fork_angle = 20
    base_len = 10.0
    #print(len(pixeles))
    if depth > 0:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * base_len)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * base_len) - decremento
        pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), pixeles)
        drawTree(x2, y2, angle - fork_angle, depth - 1, decremento * 4 / 3, pixeles)
        drawTree(x2, y2, angle + fork_angle, depth - 1, decremento * 4 / 3, pixeles)


def input(event):
    if event.type == pygame.QUIT:
        exit(0)

drawTree(300, 550, -90, 9, 3, 2)
pygame.display.flip()

#pygame.image.save(window, "scrennArbolpy2.jpeg")
while True:
    input(pygame.event.wait())
