import pygame

pygame.init()

win = pygame.display.set_mode((800, 800))
pygame.display.set_caption("First Game")

x = 380
y = 380
width = 40
height = 60
vel = 5


def gravity(y):
    y += 3.2

FPS = 60
clock = pygame.time.Clock()
run = True
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    y += 3.2

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((255, 255, 255))
    pygame.draw.circle(win, (255, 0, 0), (x, y), radius=20)
    pygame.display.update()


pygame.quit()