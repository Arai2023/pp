import pygame
pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Japan flag :)")
pygame.display.set_icon(pygame.image.load("Heart_illustration_In_Pixel_Shape.bmp"))


RED = (255, 0 , 0)
WHITE = (255, 255, 255)


x = W // 2
y = H // 2
speed = 20


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= speed
            elif event.key == pygame.K_RIGHT:
                x += speed 
            elif event.key == pygame.K_UP:
                y -= speed
            elif event.key == pygame.K_DOWN:
                y += speed     
    sc.fill(WHITE)
    pygame.draw.circle(sc, RED, (x, y), 50)
    
    pygame.display.update()
    