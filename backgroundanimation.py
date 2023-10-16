"""
import pygame 
pygame.init()
x=800
y=600
screen = pygame.display.set_mode((x,y))
pygame.display.set_caption("Coyote e Papaleguas")



background = pygame.image.load("/home/aurelio/Documents/projects/python_projects/animated_python_game/background.png").convert_alpha()
background = pygame.transform.scale(background, (x, y))
running = True

while running:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
               rodando = False
    screen.blit(background, (0, 0))

    rel_x = x % background.get_rect().width
    screen.blit(background, (rel_x - background.get_rect().width,0))#cria background
    if rel_x < 800:
         screen.blit(background, (rel_x, 0))


    x-=2    
    pygame.display.update()
    """