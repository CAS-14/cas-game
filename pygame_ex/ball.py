import sys, pygame
pygame.init()

size = width, height = 640, 480
speed = [3, 3]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("assets/jimmy1.png")
ballrect = ball.get_rect()

clock = pygame.time.Clock()

animation_frames = ["assets/jimmy1.png", "assets/jimmy2.png"]
current_frame = 0

def switch():
    global current_frame
    current_frame = 1 if current_frame == 0 else 0
    return pygame.image.load(animation_frames[current_frame])

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
        ball = switch()
        
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
        ball = switch()

    screen.fill("#ffffff")
    screen.blit(ball, ballrect)
    pygame.display.flip()

    clock.tick(60)