import pygame, math, random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, player) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,30))
        self.image.fill((40,190,30))
        self.rect = self.image.get_rect()
        self.pose = pygame.math.Vector2(random.randint(350, 550), random.randint(350, 550))
        self.rect.center = self.pose
        self.speed = 1.5
        self.player = player

    def update(self) -> None:
        dx = self.player.pose.x - self.rect.centerx
        dy = self.player.pose.y - self.rect.centery
        distance = math.sqrt(dx**2 + dy**2)

        if distance < 50:
            self.speed = 2.5
        elif distance > 51 and distance < 80:
            self.speed = 2
        else:
            self.speed = 1.5
        
        if distance != 0:
            dx /= distance
            dy /= distance
        
        self.rect.centerx += dx * self.speed
        self.rect.centery += dy * self.speed
