import sys
import pygame
from sprite import Background, Base, Bird, getPipe, Score
import config
from resources_loader import ResourcesLoader

pygame.init()

pygame.display.set_caption("Flappy Bird")
screen = pygame.display.set_mode((config.screenWidth, config.screenHeight))

# 加载所有的资源
ResourcesLoader.loadAllResources()

background = Background()
bird = Bird()
base = Base()
pipeGroup = pygame.sprite.Group()
score = Score()

# 用于控制帧率
clock = pygame.time.Clock()


# 开始场景
def startScene():
    # 添加信息图片
    messageSprite = pygame.sprite.Sprite()
    messageSprite.image = ResourcesLoader.message
    messageSprite.rect = messageSprite.image.get_rect()
    messageSprite.rect.center = (config.screenWidth / 2, config.screenHeight / 2)
    messageSprite.rect.top -= config.screenHeight / 6

    # 渲染组（按添加顺序渲染）
    renderGroup = pygame.sprite.OrderedUpdates(background, base, bird, messageSprite)

    isBreak = False

    while True:
        clock.tick_busy_loop(config.FPS)  # 帧率保持

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.USEREVENT + config.birdChangeImgEventID:  # 这里的鸟仍然需要切换图片保持动画
                bird.changeImg()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 如果单击鼠标则跳出循环进入到下一个场景（开始游戏）
                isBreak = True

        if isBreak:
            break

        # 保持背景和地面的移动
        background.update()
        base.update()

        # 双缓冲绘制窗口内容
        screen.fill((0, 0, 0, 0))
        renderGroup.draw(screen)
        pygame.display.flip()


# 游戏场景
def gameScene():
    pipeGroup.add(getPipe(base.rect.height))  # 添加水管
    renderGroup = pygame.sprite.OrderedUpdates(background, pipeGroup, base, bird, score)

    while True:
        clock.tick_busy_loop(config.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 单击鼠标让鸟儿跳起来
                bird.speedReverse()
            elif event.type == pygame.USEREVENT + config.birdChangeImgEventID:  # 保持动画
                bird.changeImg()

        if bird.isDead(base.rect.top, pipeGroup):  # 鸟死亡，游戏结束，进入到游戏结束场景
            break

        # 如果这一组水管过去了的话就加入新的水管并且分数+1
        if not pipeGroup:
            pipeGroup.add(getPipe(base.rect.height))
            renderGroup.empty()
            renderGroup.add(background, pipeGroup, base, bird, score)
            score.score += 1

        renderGroup.update()

        screen.fill((0, 0, 0, 0))
        renderGroup.draw(screen)
        pygame.display.flip()


# 游戏结束场景
def gameOverScene():
    # 添加游戏结束图片
    gameOverSprite = pygame.sprite.Sprite()
    gameOverSprite.image = ResourcesLoader.gameover
    gameOverSprite.rect = gameOverSprite.image.get_rect()
    gameOverSprite.rect.center = (config.screenWidth / 2, config.screenHeight / 2)
    gameOverSprite.rect.top -= config.screenHeight / 8

    renderGroup = pygame.sprite.OrderedUpdates(background, pipeGroup, base, bird, score, gameOverSprite)
    isBreak = False

    # 需要注意的是这个场景之中每一帧没有update，也没接收鸟切换图片动画事件，才能够保持所有的精灵的静止不动
    # 让玩家接收自己失败的事实
    while True:
        clock.tick_busy_loop(config.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # 单击任意鼠标按键接收自己失败的事实，退出渲染循环进入到下一个场景（重新开始）
                isBreak = True

        if isBreak:
            break

        screen.fill((0, 0, 0, 0))
        renderGroup.draw(screen)
        pygame.display.flip()

    # 游戏结束，重置一些信息，然后重新开始
    bird.init()
    score.score = 0
    pipeGroup.empty()


# 游戏结束之后重新开始
# 退出的话每个事件循环之中都有检测退出操作的代码
while True:
    startScene()
    gameScene()
    gameOverScene()
