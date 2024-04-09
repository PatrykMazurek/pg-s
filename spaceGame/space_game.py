import pygame, os, random
from ship import Ship
from asteroid import Asteroid
from laser import Laser

BLACK = (0,0,0)

FPS = 60

WIDTH, HEIGHT = 800, 650

background = pygame.image.load(os.path.join("assets", "Nebula1.png"))

pygame.display.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("space Game")
clock = pygame.time.Clock()
run = True

spaceShip = Ship(pygame.math.Vector2(300, 500),
                 pygame.math.Vector2( 0,0 ))

asteroids = []
for i in range(0,5):
    aX = random.randint(5, WIDTH - 100)
    aY = random.randint(-400, -100)
    asteroids.append(Asteroid(pygame.math.Vector2(aX, aY) ))

lasers = []

def draw_window(win, spaceShip, asteroids, lasers):
    win.fill(BLACK)
    win.blit(background, (0,0))
    spaceShip.update_position(HEIGHT, WIDTH)
    spaceShip.draw_ship(win)
    for aster in asteroids:
        aster.update_position()
        aster.draw_aseroid(win)
    for laser in lasers:
        laser.draw_laser(win)
    pygame.display.update()
while run:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                lasers.append(Laser(pygame.math.Vector2( spaceShip.position.x + spaceShip.img.get_width()/2,
                                                        spaceShip.position.y)))

    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_w] and spaceShip.position.y > 0:
        spaceShip.speed.y -= 0.2
        # spaceShip.position.y -= 1
    if keyPressed[pygame.K_s] and spaceShip.position.y + (spaceShip.size.height/2) < HEIGHT:
        spaceShip.speed.y += 0.2
        # spaceShip.position.y += 1
    if keyPressed[pygame.K_d] and spaceShip.position.x > 0:
        spaceShip.speed.x += 0.2
        # spaceShip.position.x += 1
    if keyPressed[pygame.K_a] and spaceShip.position.x + (spaceShip.size.width/2) < WIDTH:
        spaceShip.speed.x -= 0.2
        # spaceShip.position.x -= 1

    for ast in asteroids:
        if ast.position.y + 5 > HEIGHT:
            asteroids.remove(ast)
            aX = random.randint(5, WIDTH - 100)
            aY = random.randint(-400, -100)
            asteroids.append(Asteroid(pygame.math.Vector2(aX, aY)) )

    for laser in lasers:
        laser.update()
        if laser.position.y < 0:
            lasers.remove(laser)


    draw_window(win, spaceShip, asteroids, lasers)
pygame.quit()
