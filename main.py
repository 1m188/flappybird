import sys
import pygame
from bird import Bird
from background import Background
from base import Base
from pipe import getPipe
from score import Score
import config
from resources_loader import ResourcesLoader

pygame.init()

pygame.display.set_caption("Flappy Bird")
screen = pygame.display.set_mode((config.screenWidth, config.screenHeight))

ResourcesLoader.loadAllResources()

background = Background()
bird = Bird()
base = Base()
pipeGroup = pygame.sprite.Group()
score = Score()

clock = pygame.time.Clock()


def startScene():
    messageSprite = pygame.sprite.Sprite()
    messageSprite.image = ResourcesLoader.message
    messageSprite.rect = messageSprite.image.get_rect()
    messageSprite.rect.center = (config.screenWidth / 2, config.screenHeight / 2)
    messageSprite.rect.top -= config.screenHeight / 6

    renderGroup = pygame.sprite.OrderedUpdates(background, base, bird, messageSprite)

    isBreak = False

    while True:
        clock.tick_busy_loop(config.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.USEREVENT + config.birdChangeImgEventID:
                bird.changeImg()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                isBreak = True

        if isBreak:
            break

        background.update()
        base.update()

        screen.fill((0, 0, 0, 0))
        renderGroup.draw(screen)
        pygame.display.flip()


def gameScene():
    pipeGroup.add(getPipe(base.rect.height))
    renderGroup = pygame.sprite.OrderedUpdates(background, pipeGroup, base, bird, score)

    while True:
        clock.tick_busy_loop(config.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                bird.speedReverse()
            elif event.type == pygame.USEREVENT + config.birdChangeImgEventID:
                bird.changeImg()

        if bird.isDead(base.rect.top, pipeGroup):
            break

        if not pipeGroup:
            pipeGroup.add(getPipe(base.rect.height))
            renderGroup.empty()
            renderGroup.add(background, pipeGroup, base, bird, score)
            score.score += 1

        renderGroup.update()

        screen.fill((0, 0, 0, 0))
        renderGroup.draw(screen)
        pygame.display.flip()


def gameOverScene():
    gameOverSprite = pygame.sprite.Sprite()
    gameOverSprite.image = ResourcesLoader.gameover
    gameOverSprite.rect = gameOverSprite.image.get_rect()
    gameOverSprite.rect.center = (config.screenWidth / 2, config.screenHeight / 2)
    gameOverSprite.rect.top -= config.screenHeight / 8

    renderGroup = pygame.sprite.OrderedUpdates(background, pipeGroup, base, bird, score, gameOverSprite)
    isBreak = False

    while True:
        clock.tick_busy_loop(config.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                isBreak = True

        if isBreak:
            break

        screen.fill((0, 0, 0, 0))
        renderGroup.draw(screen)
        pygame.display.flip()

    bird.init()
    score.score = 0
    pipeGroup.empty()


while True:
    startScene()
    gameScene()
    gameOverScene()
