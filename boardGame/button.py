import pygame


class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        font = pygame.font.SysFont(None, 30)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print("kliknieto w myszkę")
                # print("{} {}".format(self.rect.topleft, self.rect.bottomright))
                # print(pygame.mouse.get_pos())
                if self.rect.collidepoint(pygame.mouse.get_pos()):
                    # print("kliknieto w przycisk")
                    return True
        return False