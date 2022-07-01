
import pygame
pygame.init
#Class Game
class Game:
    def __init__(self):
        self.player = Player()

#Class Player
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack_damage = 10
        self.velocity = 10
        self.image = pygame.image.load('C:\\Users\\miraille\\Desktop\\Python\\test_jeu_1\\Image_pour_jeu\\player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 600
        self.rect.y = 700

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

#Fenetre du jeu
pygame.display.set_caption('Jeu De Tir')
screen = pygame.display.set_mode((1500, 1000))

background = pygame.image.load ('C:\\Users\\miraille\\Desktop\\Python\\test_jeu_1\\Image_pour_jeu\\bg.jpg')
player = Player()

game = Game()

#Game Loop
running = True

while running :


    screen.blit(background , (0, 0))
    screen.blit(player.image, player.rect)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit
            #Detect Key
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.player.move_right
            elif event.key == pygame.K_LEFT:
                game.player.move_left()

