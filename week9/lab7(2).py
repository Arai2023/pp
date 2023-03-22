import pygame
pygame.init()

pygame.mixer.music.load("birds.mp3")
pygame.mixer.music.play(0)

W, H = 500, 300
sc = pygame.display.set_mode((W, H))

flPause = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                flPause = not flPause
                if flPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()