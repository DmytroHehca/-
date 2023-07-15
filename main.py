import pygame

pygame.init()

# вікно створити
window = pygame.display.set_mode((700, 500))
fps = pygame.time.Clock()



class Sprite:
    def __init__(self, speed, spriteName, x, y, w, h):
        self.image = pygame.transform.scale(pygame.image.load(spriteName), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def draw(self, window):
        window.blit(self.image, [self.rect.x, self.rect.y])


class Player(Sprite):
    def __init__(self, x, y, filename, speed, w, h):
        super().__init__(x, y, filename, speed, w, h)


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            if self.rect.y > 0:
                self.rect.y -= self.speed

        if keys[pygame.K_s]:
            if self.rect.y < 380:
                self.rect.y += self.speed
    def draw(self, window):
        window.blit(self.image, [self.rect.x, self.rect.y])
        super(Player, self).draw(window)



class Player2(Sprite):
    def __init__(self, x, y, filename, speed, w, h):
        super().__init__(x, y, filename, speed, w, h)


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if self.rect.y > 0:
                self.rect.y -= self.speed

        if keys[pygame.K_DOWN]:
            if self.rect.y < 380:
                self.rect.y += self.speed

        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
    def draw(self, window):
        window.blit(self.image, [self.rect.x, self.rect.y])
        super(Player2, self).draw(window)

WHITE = (255, 255, 255)
class Button:

    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text

    def draw(self):
        pygame.draw.rect(window, WHITE, self.rect)
        font = pygame.font.Font(None, 23)
        text = font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        window.blit(text, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


class Ball(Sprite):
    def __init__(self, x, y, filename, speed, w, h):
        super().__init__(x, y, filename, speed, w, h)


    def update(self):

        self.rect.x += self.speed
        self.rect.y += self.speed



    def draw(self, window):
        window.blit(self.image, [self.rect.x, self.rect.y])
        super(Ball, self).draw(window)




def playgame():
    # з правої сторони 610, 10
    menu_button = Button(325, 10, 80, 20, "Меню")





    player = Player(7, "platf.png", 0, 385, 50, 110)
    player2 = Player2(7, "platf2.png", 650, 385, 50, 110)
    ball = Ball(7, "ball.png", 320, 230, 80, 90)
    background = pygame.transform.scale(pygame.image.load("sky.png"), (700, 500))


    game = True
    while game:
        # обробка подій
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if menu_button.is_clicked(pygame.mouse.get_pos()):
                    print("Клік по кнопці 'Меню'")
        # оновлення
        player.update()
        player2.update()
        ball.update()
        # відмалювання
        window.blit(background, [0, 0])
        player.draw(window)
        player2.draw(window)
        ball.draw(window)

        menu_button.draw()

        pygame.display.flip()
        fps.tick(60)