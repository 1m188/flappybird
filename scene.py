import sys
import pygame
import config
from sprite import getPipe


# 场景
class Scene:
    def __init__(self):
        self.clock = pygame.time.Clock()  # 用作帧率控制的钟
        self.fps = config.FPS  # 帧率值，默认为config中定义的值
        self.isRunning = False  # 场景是否正在运行
        self.renderGroup = pygame.sprite.OrderedUpdates()  # 渲染组

    # 设置帧率
    def setFps(self, fps: int):
        self.fps = fps

    # 场景开始前的准备
    def prepare(self, *args, **kwargs):
        pass

    def eventHandle(self, event):
        pass

    # 每一帧的数据更新
    def update(self, *args, **kwargs):
        pass

    # 每一帧的绘制
    # 传入一个参数 窗口surface
    def paint(self, *args, **kwargs):
        screen = kwargs["screen"]
        screen.fill((0, 0, 0, 0))
        self.renderGroup.draw(screen)
        pygame.display.flip()  # 双缓冲绘制窗口内容

    # 场景结束后的操作
    def end(self, *args, **kwargs):
        pass

    # 场景运行
    def run(self, *args, **kwargs):

        # 场景开始前的准备
        self.prepare(*args, **kwargs)

        self.isRunning = True

        # 每一帧的内容
        while self.isRunning:
            self.clock.tick_busy_loop(self.fps)  # 帧率控制

            # 事件处理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                else:
                    self.eventHandle(event)  # 除了某些通用处理外的事件处理

            self.update(*args, **kwargs)  # 每一帧的数据更新
            self.paint(*args, **kwargs)  # 每一帧的图像绘制

        self.end(*args, **kwargs)  # 场景结束之后的处理


# 开始场景
class StartScene(Scene):
    def prepare(self, *args, **kwargs):
        # 添加各种精灵
        self.background = kwargs["background"]
        self.base = kwargs["base"]
        self.bird = kwargs["bird"]
        message = kwargs["message"]

        # 渲染组（按添加顺序渲染）
        self.renderGroup.add(self.background, self.base, self.bird, message)

    def eventHandle(self, event):
        if event.type == pygame.USEREVENT + config.birdChangeImgEventID:  # 鸟切换图片保持动画
            self.bird.changeImg()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 如果单击鼠标则结束当前场景进入到下一个场景
            self.isRunning = False

    def update(self, *args, **kwargs):
        # 保持背景和地面的移动
        self.background.update()
        self.base.update()


# 游戏场景
class GameScene(Scene):
    def prepare(self, *args, **kwargs):
        # 添加各种精灵
        self.background = kwargs["background"]
        self.base = kwargs["base"]
        self.bird = kwargs["bird"]
        self.pipeGroup = kwargs["pipeGroup"]
        self.score = kwargs["score"]

        self.pipeGroup.add(getPipe(self.base.rect.height))  # 添加水管
        self.renderGroup.add(self.background, self.pipeGroup, self.base, self.bird, self.score)  # 渲染组（按添加顺序渲染）

    def eventHandle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # 单击鼠标让鸟儿跳起来
            self.bird.speedReverse()
        elif event.type == pygame.USEREVENT + config.birdChangeImgEventID:
            self.bird.changeImg()

    def update(self, *args, **kwargs):
        # 鸟死亡，结束游戏场景，进入下一个场景
        if self.bird.isDead(self.base.rect.top, self.pipeGroup):
            self.isRunning = False
        else:
            # 如果这一组水管过去了的话就加入新的水管并且分数+1
            if not self.pipeGroup:
                self.pipeGroup.add(getPipe(self.base.rect.height))
                self.renderGroup.empty()
                self.renderGroup.add(self.background, self.pipeGroup, self.base, self.bird, self.score)
                self.score.score += 1

            self.renderGroup.update()


# 游戏结束场景
# 需要注意的是这个场景之中每一帧没有update，也没接收鸟切换图片动画事件，才能够保持所有的精灵的静止不动
class GameoverScene(Scene):
    def prepare(self, *args, **kwargs):
        # 添加各种精灵
        self.background = kwargs["background"]
        self.base = kwargs["base"]
        self.bird = kwargs["bird"]
        self.pipeGroup = kwargs["pipeGroup"]
        self.score = kwargs["score"]
        gameover = kwargs["gameover"]

        self.renderGroup.add(self.background, self.pipeGroup, self.base, self.bird, self.score, gameover)

    def eventHandle(self, event):
        # 让玩家接收自己失败的事实
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.isRunning = False

    def end(self, *args, **kwargs):
        # 游戏结束，重置一些信息，然后重新开始
        self.bird.init()
        self.score.score = 0
        self.pipeGroup.empty()
