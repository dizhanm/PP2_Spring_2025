import pygame
pygame.mixer.init()
pygame.init()
running=True
screen=pygame.display.set_mode((800,750))
pygame.display.set_caption("Player")
freestyle=pygame.transform.scale(pygame.image.load("lilbaby.jpeg"),(800,750))
winslosses=pygame.transform.scale(pygame.image.load("meekmill.jpeg"),(800,750))
zeze=pygame.transform.scale(pygame.image.load("zeze.jpeg"),(800,750))
arrP=[freestyle, winslosses, zeze]
arrM=[
"Lil Baby - Freestyle.mp3",
"Meek-Mill-Wins-Losses-(HipHopKit.com).mp3",
"Kodak Black ft. Travis Scott,Offset - ZEZE.mp3"
]
index=0
pygame.mixer.music.load(arrM[index])
pygame.mixer.music.play()
paused=False
while running:
    screen.blit(arrP[index], (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                index=(index+1)%3
                pygame.mixer.music.load(arrM[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT:
                index = (index - 1) % 3
                pygame.mixer.music.load(arrM[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
                paused = not paused