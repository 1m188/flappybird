import random
from collections import Iterable
from typing import List

from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QPainter, QPixmap
from PySide2.QtCore import QTimer, Slot

import config
from sprite import Sprite, Bird, Background, Message, OverMsg, Base


# 场景类
class Scene(QWidget):
    def __init__(self, parent: QWidget, *args, **kwargs):
        super().__init__(parent)
        self.resize(self.parentWidget().size())  # 使场景和窗口大小一样大

        # 渲染列表，其中可以是sprite，也可以是其他可迭代对象，
        # 但最终都要是sprite
        # 先加入的对象先渲染，尾部对象最后渲染
        self.renderl = []

        self.prepare(*args, **kwargs)  # 场景开始前的准备

    def paintEvent(self, event):
        painter = QPainter(self)
        rl = self.renderl.copy()
        rl.reverse()
        while rl:
            s = rl.pop()
            if isinstance(s, Iterable):
                rl.extend(list(reversed(s)))
            else:
                painter.drawPixmap(s.x, s.y, s.spriteImg)

    # 场景启动，使用定时器控制帧数
    def run(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.frame)
        self.timer.start(1000 / config.FPS)

    # 场景停止，进入扫尾阶段
    def stop(self):
        self.timer.stop()
        self.end()

    # 每帧的内容
    @Slot()
    def frame(self):
        self.statusUpdate()
        self.update()  # 刷新重绘

    def prepare(self, *args, **kwargs):
        pass

    # 场景每帧的某些状态的变化
    def statusUpdate(self):
        pass

    # 场景结束的扫尾
    def end(self):
        pass


# 开始场景
class StartScene(Scene):
    def prepare(self, background: Background, bird: Bird, base: Base):
        self.background = background  # 背景
        self.base = base  # 地板

        self.base.y = self.height() - self.base.height

        # 鸟
        self.bird = bird
        self.bird.x = self.width() / 8
        self.bird.y = self.height() / 3 + 42

        # 开场信息
        self.message = Message()
        self.message.x = self.width() / 2 - self.message.width / 2
        self.message.y = self.height() / 12

        self.renderl.extend(
            (self.background, self.base, self.message, self.bird))

    def statusUpdate(self):
        self.background.moveLeft()  # 背景移动，制造前飞效果
        self.base.moveLeft()
        self.bird.changeImg()  # 鸟更换图片，制造翅膀效果

    # 一旦鼠标点击，立刻停止开始场景，进入下一个游戏场景
    def mousePressEvent(self, event):
        self.stop()
        super().mousePressEvent(event)

    # 扫尾，生成游戏场景并准备进入
    def end(self):
        self.deleteLater()
        gameScene = GameScene(self.parent(), self.background, self.bird,
                              self.base)
        gameScene.show()
        gameScene.run()


# 游戏场景
class GameScene(Scene):
    def prepare(self, background: Background, bird: Bird, base: Base):
        self.background = background
        self.base = base
        self.pipes = []  # 水管
        self.bird = bird
        self.bird.initStatus()  # 初始化小鸟状态
        self.bird.passPipe.connect(self.getPipe)
        self.bird.passPipe.emit()
        self.isEnd = False  # 游戏是否结束
        # 分数
        self.score = 0
        self.scoresp: List[Sprite] = []
        self.changeScore(self.score)

        self.renderl.extend(
            (self.background, self.bird, self.pipes, self.base, self.scoresp))

    def mousePressEvent(self, event):
        # 点击鼠标让小鸟往上飞
        self.bird.v = -config.birdRevSpd
        config.AudRes.wing.play()
        super().mousePressEvent(event)

    def changeScore(self, val: int):
        '''改变分数'''
        self.score = val
        self.scoresp.clear()

        if not val:  # 单独零分特殊考虑
            sp = Sprite(config.ImgRes.num[0])
            sp.x = self.width() / 2 - sp.width / 2
            sp.y = self.height() / 10
            self.scoresp.append(sp)
            return

        while val:
            img = config.ImgRes.num[val % 10]
            self.scoresp.append(Sprite(img))
            val //= 10
        self.scoresp.reverse()
        lx = self.width() / 2 - len(self.scoresp) * self.scoresp[0].width / 2
        for i in self.scoresp:
            i.x = lx
            lx += i.width
            i.y = self.height() / 10

    # 背景不断移动
    # 同时每帧的变化小鸟需要按照一定加速度向下走
    def statusUpdate(self):
        self.background.moveLeft()
        self.base.moveLeft()
        self.bird.changeImg()

        self.bird.v += config.gravity
        self.bird.y += self.bird.v

        for i in self.pipes:
            i.x -= config.pipeScrollSpeed

        if self.pipes[0].x + self.pipes[0].width < 0:
            self.bird.passPipe.emit()
            self.score += 1
            self.changeScore(self.score)
            config.AudRes.point.play()

        self.isEnd = self.collide()
        if self.isEnd:
            self.stop()

    def collide(self) -> bool:
        '''小鸟的碰撞检测'''
        if self.bird.y <= 0 or self.bird.y + self.bird.height >= self.base.y:
            return True
        for p in self.pipes:
            f = self.bird.x + self.bird.width < p.x or \
                self.bird.x > p.x + p.width or \
                self.bird.y + self.bird.height < p.y or \
                self.bird.y > p.y + p.height
            if not f:
                config.AudRes.hit.play()
                return True
        return False

    @Slot()
    def getPipe(self):
        '''获得新水管'''
        index = random.randint(0, len(config.ImgRes.pipe) - 1)
        key = list(config.ImgRes.pipe)[index]
        image = config.ImgRes.pipe[key]
        pipeDown = Sprite(
            QPixmap.fromImage(image.toImage().mirrored(False, True)))
        pipeUp = Sprite(image)
        pipeUp.x = self.width()
        pipeDown.x = self.width()
        pipeUp.y = random.randint(config.pipeLimit + config.pipeInterval,
                                  self.base.y - config.pipeLimit)
        pipeDown.y = pipeUp.y - config.pipeInterval - pipeDown.height
        self.pipes.clear()
        self.pipes.extend((pipeUp, pipeDown))

    def end(self):
        '''结束游戏，进入结算界面'''
        self.deleteLater()
        over = GameoverScene(self.parent(), self.background, self.bird,
                             self.pipes, self.score, self.scoresp, self.base)
        over.show()
        over.run()


class GameoverScene(Scene):
    '''游戏结束场景'''
    def prepare(self, background: Background, bird: Bird, pipes: tuple,
                score: int, scoresp: List[Sprite], base: Base):
        self.background = background
        self.base = base
        self.bird = bird
        self.pipes = pipes
        self.score = score
        self.scoresp = scoresp

        self.msg = OverMsg()  # 游戏结束标题
        self.msg.x = self.width() / 2 - self.msg.width / 2
        self.msg.y = self.height()

        self.isEnd = False  # 过场动画是否结束

        self.renderl.extend((self.background, self.bird, self.pipes, self.base,
                             self.msg, self.scoresp))

        config.AudRes.die.play()

    def statusUpdate(self):
        # 游戏结束信息移动
        if self.msg.y + self.msg.height / 2 > self.height() / 3:
            self.msg.y -= config.gameoverScrollSpeed
        else:
            self.isEnd = True

    def mousePressEvent(self, event):
        if self.isEnd:
            self.stop()

    def end(self):
        '''重新进入开始界面'''
        self.deleteLater()
        startScene = StartScene(self.parent(), self.background, self.bird,
                                self.base)
        startScene.show()
        startScene.run()
