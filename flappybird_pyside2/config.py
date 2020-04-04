from PySide2.QtGui import QPixmap
from PySide2.QtMultimedia import QSound

# 这里记录一些资源的路径及获取方法

# 图片资源路径
imgPath = {}

imgPathPrefix = "../asset/image"

# 图标
imgPath["icon"] = f"{imgPathPrefix}/bird_icon.png"

# 某些游戏信息图片路径
imgPath["message"] = f"{imgPathPrefix}/message.png"
imgPath["gameover"] = f"{imgPathPrefix}/gameover.png"

# 背景及下边界
for i in ("day", "night"):
    imgPath[f"background-{i}"] = f"{imgPathPrefix}/background-{i}.png"
imgPath["base"] = f"{imgPathPrefix}/base.png"

# 几种颜色的鸟以及其各种形态
for i in ("red", "blue", "yellow"):
    imgPath[f"{i}bird-downflap"] = f"{imgPathPrefix}/{i}bird-downflap.png"
    imgPath[f"{i}bird-midflap"] = f"{imgPathPrefix}/{i}bird-midflap.png"
    imgPath[f"{i}bird-upflap"] = f"{imgPathPrefix}/{i}bird-upflap.png"

# 水管
for i in ("green", "red"):
    imgPath[f"pipe-{i}"] = f"{imgPathPrefix}/pipe-{i}.png"

# 数字
for i in range(10):
    imgPath[str(i)] = f"{imgPathPrefix}/{str(i)}.png"


# 图片资源
class ImgRes:

    # 获取资源
    @staticmethod
    def getRes(resPath: str) -> QPixmap:
        return QPixmap(imgPath[resPath])

    # 加载所有资源
    @classmethod
    def loadAll(cls):

        cls.icon = cls.getRes("icon")

        cls.message = cls.getRes("message")
        cls.gameover = cls.getRes("gameover")

        cls.background = {}
        cls.background["day"] = cls.getRes("background-day")
        cls.background["night"] = cls.getRes("background-night")
        cls.base = cls.getRes("base")

        cls.bird = {}
        cls.bird["red"] = (cls.getRes("redbird-downflap"), cls.getRes("redbird-midflap"), cls.getRes("redbird-upflap"))
        cls.bird["blue"] = (cls.getRes("bluebird-downflap"), cls.getRes("bluebird-midflap"), cls.getRes("bluebird-upflap"))
        cls.bird["yellow"] = (cls.getRes("yellowbird-downflap"), cls.getRes("yellowbird-midflap"), cls.getRes("yellowbird-upflap"))

        cls.pipe = {}
        cls.pipe["red"] = cls.getRes("pipe-red")
        cls.pipe["green"] = cls.getRes("pipe-green")

        cls.num = {}
        for i in range(10):
            cls.num[i] = cls.getRes(str(i))


# 音乐资源路径
audPath = {}
audPathPrefix = "../asset/audio"
audPath["die"] = f"{audPathPrefix}/die.ogg"  # 死亡
audPath["hit"] = f"{audPathPrefix}/hit.ogg"  # 撞到某些东西
audPath["point"] = f"{audPathPrefix}/point.ogg"  # 得分
audPath["wing"] = f"{audPathPrefix}/wing.ogg"  # 点击向上飞时


# 音乐资源
class AudRes:

    # 资源获取
    @staticmethod
    def getRes(resPath: str) -> QSound:
        return QSound(resPath)

    # 加载所有资源
    @classmethod
    def loadAll(cls):
        cls.die = cls.getRes(audPath["die"])
        cls.hit = cls.getRes(audPath["hit"])
        cls.point = cls.getRes(audPath["point"])
        cls.wing = cls.getRes(audPath["wing"])


# 这里记录一些配置，包括各种大小速度等的参数，以及各种资源的加载路径
# 需要注意的是这里所有的数字变量都是正值，因此如果要使用的话要结合实际的需要判定方向

# 帧率
FPS = 60

# 游戏窗口大小（与背景大小相同）
screenWidth = 288
screenHeight = 512

# 背景移动速度
backgroundScrollSpeed = 1

gravity = 0.3  # 鸟收到的重力
birdRevSpd = 6  # 按下按键之后的速度反转
birdChangeImgEventID = 1  # 鸟切换图片事件id
birdImgChangeEventInterval = 200  # 鸟切换显示图片间隔时间 单位ms

pipeScrollSpeed = 2  # 水管移动速度
pipeInterval = 100  # 上下两个水管之间的距离
pipeLimit = 20  # 水管距离相同边界的最小距离
pipeGenEventID = 2  # 水管生成事件id
pipeGenEventInterval = 1800  # 水管生成时间间隔 ms

baseScrollSpeed = 2  # 地面移动速度

gameoverScrollSpeed = 5  # 游戏结束信息移动速度
