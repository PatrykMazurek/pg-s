import pygame, os, random
from ship import Ship
from asteroid import Asteroid

BLACK = (0,0,0)

FPS = 60

WIDTH, HEIGHT = 700, 800

pygame.display.init()
win = pygame.display.set_mode((HEIGHT, WIDTH))
pygame.display.set_caption("space Game")
clock = pygame.time.Clock()
run = True


spaceShip = Ship(pygame.math.Vector2(200, 500),
                 pygame.math.Vector2( 0,0 ))
spaceShip.img = pygame.image.load(os.path.join("spaceGame", "assets", "ship.png"))
spaceShip.size = spaceShip.img.get_rect()
spaceShip.img = pygame.transform.scale(spaceShip.img, (spaceShip.img.get_width() /2,
                                                       spaceShip.img.get_height() /2 ))
spaceShip.size = spaceShip.img.get_rect()

tempTab = ["a10000.png", "a30000.png", "a30013.png"]
asteroids = []
for i in range(0,5):
    pathImg = random.choice(tempTab)
    aX = random.randint(5, WIDTH - 100)
    aY = random.randint(-400, -100)
    asteroids.append(Asteroid(pygame.math.Vector2(aX, aY), 
                              pygame.math.Vector2( 0, 3), 
                              os.path.join("spaceGame","assets", pathImg)))

def draw_window(win, spaceShip, asteroids):
    win.fill(BLACK)
    spaceShip.update_position(WIDTH, HEIGHT)
    spaceShip.draw_ship(win)
    for aster in asteroids:
        aster.update_position()
        aster.draw_aseroid(win)
    pygame.display.update()
while run:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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

    draw_window(win, spaceShip, asteroids)
pygame.quit()
