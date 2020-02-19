import pygame
from sprite import Background, Base, Bird, Score, Message, Gameover
from scene import StartScene, GameScene, GameoverScene
import config

pygame.init()

pygame.display.set_caption("Flappy Bird")
screen = pygame.display.set_mode((config.screenWidth, config.screenHeight))

# 加载所有的资源
config.ResourcesLoader.loadAllResources()

# 加载所有的游戏精灵
background = Background()
bird = Bird()
base = Base()
pipeGroup = pygame.sprite.Group()
score = Score()
message = Message()
gameover = Gameover()

# 游戏循环
while True:
    # 开始场景
    startScene = StartScene()
    startScene.run(screen=screen, background=background, base=base, bird=bird)

    # 游戏场景
    gameScene = GameScene()
    gameScene.run(screen=screen, background=background, base=base, bird=bird, pipeGroup=pipeGroup, score=score)

    # 结束场景
    gameoverScene = GameoverScene()
    gameoverScene.run(screen=screen, background=background, base=base, bird=bird, pipeGroup=pipeGroup, score=score)
