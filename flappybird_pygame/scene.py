import sys
import pygame
import config
from sprite import Pipe, Message, Gameover


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
        message = Message()

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

        # 这一组始终最多只有一组水管，为了判断鸟是否死亡使用，在渲染组中的是为了渲染，因为当鸟刚刚飞过水管而水管还没有从地图中消失的时候那一段过程需要考虑
        self.nowPipeGroup = pygame.sprite.Group(Pipe.genPair(self.base))

        self.pipeGroup.add(self.nowPipeGroup)  # 添加水管
        self.renderGroup.add(self.background, self.pipeGroup, self.base, self.bird, self.score)  # 渲染组（按添加顺序渲染）

        pygame.time.set_timer(pygame.USEREVENT + config.pipeGenEventID, config.pipeGenEventInterval)  # 每过一段时间生成水管并且添加到组里

    def eventHandle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:  # 单击鼠标让鸟儿跳起来
            config.AudRes.wing.play()
            self.bird.speedReverse()
        elif event.type == pygame.USEREVENT + config.birdChangeImgEventID:  # 鸟儿切换图片
            self.bird.changeImg()
        elif event.type == pygame.USEREVENT + config.pipeGenEventID:  # 生成一组新的水管加到需要渲染的水管组中，如果判定水管组中没有水管，说明上一次判定过后新的水管还没有来，那么现在需要把新的水管也加到判定组中
            pa, pb = Pipe.genPair(self.base)
            self.pipeGroup.add(pa, pb)
            if not self.nowPipeGroup:
                self.nowPipeGroup.add(pa, pb)
            self.renderGroup.empty()
            self.renderGroup.add(self.background, self.pipeGroup, self.base, self.bird, self.score)

    def update(self, *args, **kwargs):
        # 鸟死亡，结束游戏场景，进入下一个场景
        if self.bird.isDead(self.base, self.nowPipeGroup):
            config.AudRes.hit.play()
            self.isRunning = False
        else:
            # 这里对判定水管组的第一个水管进行横坐标的判定（因为两个水管横坐标相同）
            # 为了防止某种鸟儿过了水管但是下一组水管还没来导致判定组为空的情况特地加了判定判定组为空的条件
            # 如果鸟儿过了当前的这组水管，就把判定组清空，以后不再判定，但是由于这组水管还没有走出地图边界，因此还会留在渲染组中继续渲染
            # 之后如果水管组中下一组水管已经来了，也就是水管组中有至少四个元素（刚刚过了的一组水管+下一组已经开始渲染的水管）就把下一组水管加到判定组中开始针对下一组水管判定
            # 否则就让判定组为空，直到下一组水管到来
            pipeSprites = self.pipeGroup.sprites()
            nowPipeSprites = self.nowPipeGroup.sprites()
            # 如果这一组水管过去了的话就加入新的水管并且分数+1
            if self.nowPipeGroup and self.bird.rect.left >= nowPipeSprites[0].rect.right:
                self.nowPipeGroup.empty()
                if len(pipeSprites) >= 4:
                    self.nowPipeGroup.add(pipeSprites[2], pipeSprites[3])
                self.score.score += 1
                config.AudRes.point.play()

        self.renderGroup.update()


# 游戏结束场景
# 需要注意的是这个场景之中每一帧没有update，也没接收鸟切换图片动画事件，才能够保持所有的精灵的静止不动
class GameoverScene(Scene):
    def prepare(self, *args, **kwargs):
        config.AudRes.die.play()

        # 添加各种精灵
        self.background = kwargs["background"]
        self.base = kwargs["base"]
        self.bird = kwargs["bird"]
        self.pipeGroup = kwargs["pipeGroup"]
        self.score = kwargs["score"]
        self.gameover = Gameover()

        self.renderGroup.add(self.background, self.pipeGroup, self.base, self.bird, self.score, self.gameover)

    def eventHandle(self, event):
        # 让玩家接收自己失败的事实
        if event.type == pygame.MOUSEBUTTONDOWN and self.gameover.scrollAnimEnd:
            self.isRunning = False

    def update(self, *args, **kwargs):
        self.gameover.scrollAnim()

    def end(self, *args, **kwargs):
        # 游戏结束，重置一些信息，然后重新开始
        self.bird.init()
        self.score.score = 0
        self.pipeGroup.empty()
