import pygame
import datetime

pygame.init()
isDone = True
screen = pygame.display.set_mode((450, 400))
pygame.display.set_caption("Clock")
white = (255, 255, 255)
screen.fill(white)
clock = pygame.image.load("mickeyWithoutArms.png")
leftArmIMAGE = pygame.image.load("leftarm.png")
rightArmIMAGE = pygame.image.load("rightarm.png")
pygame.display.update()

leftArmAngle = 0
rightArmAngle = 0
leftArmSecondImage = pygame.transform.scale(leftArmIMAGE, (20, leftArmIMAGE.get_height() // 3 - 20))
rightArmMinuteImage = pygame.transform.scale(rightArmIMAGE, (rightArmIMAGE.get_width() // 3,rightArmIMAGE.get_height() // 3))
print(datetime.datetime.now())
while isDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False
            pygame.quit()
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    leftArmAngle = second * (-6)
    rightArmAngle = (minute+10) * (-6)

    clock1 = pygame.transform.scale(clock, (clock.get_width() // 3, clock.get_height() // 3))
    screen.blit(clock1, (0, 0))

    left = pygame.transform.rotate(leftArmSecondImage, leftArmAngle)
    leftIMAGE = left.get_rect(center=(230, 175))

    right = pygame.transform.rotate(rightArmMinuteImage, rightArmAngle)
    rightIMAGE = right.get_rect(center=(230, 175))

    screen.blit(left, leftIMAGE.topleft)
    screen.blit(right, rightIMAGE.topleft)


    pygame.display.update()
    pygame.display.flip()