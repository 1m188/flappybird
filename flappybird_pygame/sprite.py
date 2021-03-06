import random
import pygame
import config


# 背景
class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # 这里生成一个宽度为窗口宽度两倍大的surface，在上面并排画两个背景，每次绘制只会
        # 绘制一个背景的大小，不断左移制造出小鸟向右飞的感觉，并且在背景左移快超出边界的时候
        # 重新设置为一开始的坐标反复循环制造出一种背景不断向左移并且不间断的感觉
        kind = ("day", "night")
        image = config.ImgRes.background[random.sample(kind, 1)[0]]
        self.rect = pygame.Rect(0, 0, config.screenWidth * 2, config.screenHeight)
        self.image = pygame.surface.Surface(self.rect.size).convert()
        self.image.blit(image, pygame.Rect(0, 0, self.rect.width / 2, self.rect.height))
        self.image.blit(image, pygame.Rect(self.rect.width / 2, 0, self.rect.width / 2, self.rect.height))

    # 每帧都会移动
    def update(self):
        self.rect.left -= config.backgroundScrollSpeed
        if self.rect.right <= config.screenWidth:
            self.rect.left = 0


# 地面
class Base(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # 用的方法和背景一样，两倍宽，不断向左移
        image = config.ImgRes.base
        self.rect = pygame.Rect(0, 0, image.get_width() * 2, image.get_height())
        self.rect.bottom = config.screenHeight
        self.image = pygame.surface.Surface(self.rect.size).convert()
        self.image.blit(image, pygame.Rect(0, 0, self.rect.width / 2, self.rect.height))
        self.image.blit(image, pygame.Rect(self.rect.width / 2, 0, self.rect.width / 2, self.rect.height))

    def update(self):
        self.rect.left -= config.baseScrollSpeed
        if self.rect.right <= config.screenWidth:
            self.rect.left = 0


# 鸟
class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # 这里获取鸟翅膀从上到下再到上的图片列表，以便于不断地更换显示图片制造出动画的感觉
        kind = ("yellow", "red", "blue")
        self.imgTpl = list(config.ImgRes.bird[random.sample(kind, 1)[0]])
        temp = self.imgTpl.copy()
        temp.reverse()
        temp.pop(0)
        temp.pop(-1)
        self.imgTpl += temp

        self.imgIndex = 0
        self.image = self.imgTpl[self.imgIndex]
        self.rect = self.image.get_rect()
        self.init()

        # 切换图像显示事件
        pygame.time.set_timer(pygame.USEREVENT + config.birdChangeImgEventID, config.birdImgChangeEventInterval)

    # 初始化 鸟的坐标和初速度
    # 实例化鸟类之后要调用这个函数
    def init(self):
        self.speed = 0
        self.rect.top = config.screenHeight / 2 - 49
        self.rect.left = config.screenWidth / 10

    # 这里模拟加速度的感觉，每次更新的时候速度都会向下增加一个加速度
    # 并且以当前速度移动
    def update(self):
        self.speed += config.gravity
        self.rect.top += self.speed

    # 小鸟的速度置零并且给一个向上的初速度
    # 本来只是想要单纯给一个向上的初速度的，但是后来发现做不出经典flappy bird的感觉
    def speedReverse(self):
        self.speed = -config.birdRevSpd

    # 更换显示图片函数
    def changeImg(self):
        self.imgIndex += 1
        index = self.imgIndex % len(self.imgTpl)
        self.image = self.imgTpl[index]

    # 判定小鸟是否死亡
    # 传入参数 地面的精灵对象以及加有水管的Group类实例
    def isDead(self, base: pygame.sprite.Sprite, pipeGroup: pygame.sprite.Group):
        if self.rect.bottom >= base.rect.top or self.rect.top <= 0:
            return True
        if pygame.sprite.spritecollide(self, pipeGroup, False):
            return True
        return False


# 水管
class Pipe(pygame.sprite.Sprite):
    # 生成一对水管
    @classmethod
    def genPair(cls, base: pygame.sprite.Sprite) -> tuple:
        kind = ("green", "red")
        image = config.ImgRes.pipe[random.sample(kind, 1)[0]]

        pipeBelow = cls()
        pipeBelow.image = image
        pipeBelow.rect = pipeBelow.image.get_rect()
        pipeBelow.rect.left = config.screenWidth  # 这里初始化了x坐标，在地图边界右侧，使其一旦移动能够从右侧进入窗口
        pipeBelow.rect.top = random.randint(config.pipeLimit + config.pipeInterval, base.rect.top - config.pipeLimit)

        pipeAbove = cls()
        pipeAbove.image = pygame.transform.flip(image, False, True)
        pipeAbove.rect = pipeAbove.image.get_rect()
        pipeAbove.rect.left = config.screenWidth
        pipeAbove.rect.bottom = pipeBelow.rect.top - config.pipeInterval

        return pipeAbove, pipeBelow

    def update(self):
        self.rect.left -= config.pipeScrollSpeed
        if self.rect.right <= 0:  # 这里一旦水管移动出边界立刻在所有的组里去除以便于检测鸟是否通过这一组水管
            self.kill()


# 分数
class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # 这里分数的surface高度为单个数字的高度，宽度为整个窗口的宽度
        # 考虑到可能玩到很高的分数需要多位数字表示的时候尽量在整个窗口的中间
        self.numDict = config.ImgRes.num
        self.numWidth, self.numHeight = self.numDict[0].get_size()
        self.rect = pygame.Rect(0, config.screenHeight / 8 - self.numHeight / 2, config.screenWidth, self.numHeight)
        self.image = pygame.surface.Surface(self.rect.size).convert_alpha()
        self.score = 0

    # 这里更新的时候尽量将数字分数图片摆在窗口的中间
    def update(self):
        self.image.fill((0, 0, 0, 0))
        score = str(self.score)
        length = len(score)
        scoreWidth = length * self.numWidth
        startX = config.screenWidth / 2 - scoreWidth / 2
        for i in score:
            self.image.blit(self.numDict[int(i)], pygame.Rect(startX, 0, self.numWidth, self.numHeight))
            startX += self.numWidth


# 开场信息
class Message(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = config.ImgRes.message
        self.rect = self.image.get_rect()
        self.rect.center = (config.screenWidth / 2, config.screenHeight / 2)
        self.rect.top -= config.screenHeight / 6


# 游戏结束信息
class Gameover(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = config.ImgRes.gameover
        self.rect = self.image.get_rect()
        self.rect.centerx = config.screenWidth / 2
        self.rect.top = config.screenHeight
        self.scrollAnimEnd = False

    def scrollAnim(self):
        self.rect.top -= config.gameoverScrollSpeed
        if self.rect.top <= config.screenHeight / 2 - self.rect.height / 2 - config.screenHeight / 8:
            self.rect.top += config.gameoverScrollSpeed
            self.scrollAnimEnd = True
