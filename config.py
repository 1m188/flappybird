import pygame

# 这里记录一些配置，包括各种大小速度等的参数，以及各种资源的加载路径
# 需要注意的是这里所有的数字变量都是正值，因此如果要使用的话要结合实际的需要判定方向

# 帧率
FPS = 60

# 图片资源路径
imgPath = {}

# 某些游戏信息图片路径
imgPath["message"] = "img/message.png"
imgPath["gameover"] = "img/gameover.png"

# 背景及下边界
for i in ("day", "night"):
    imgPath[f"background-{i}"] = f"img/background-{i}.png"
imgPath["base"] = "img/base.png"

# 几种颜色的鸟以及其各种形态
for i in ("red", "blue", "yellow"):
    imgPath[f"{i}bird-downflap"] = f"img/{i}bird-downflap.png"
    imgPath[f"{i}bird-midflap"] = f"img/{i}bird-midflap.png"
    imgPath[f"{i}bird-upflap"] = f"img/{i}bird-upflap.png"

# 水管
for i in ("green", "red"):
    imgPath[f"pipe-{i}"] = f"img/pipe-{i}.png"

# 数字
for i in range(10):
    imgPath[str(i)] = f"img/{str(i)}.png"

# 音乐资源路径
audPath = {}
audPath["die"] = "audio/die.ogg"  # 死亡
audPath["hit"] = "audio/hit.ogg"  # 撞到某些东西
audPath["point"] = "audio/point.ogg"  # 得分
audPath["wing"] = "audio/wing.ogg"  # 点击向上飞时

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

baseScrollSpeed = 2  # 地面移动速度

gameoverScrollSpeed = 5  # 游戏结束信息移动速度


# 图片资源获取
def getImgRes(res: str) -> pygame.surface.Surface:
    return pygame.image.load(imgPath[res]).convert_alpha()


# 音乐资源获取
def getAudRes(res: str) -> pygame.mixer.Sound:
    return pygame.mixer.Sound(res)


# 资源加载
class ResourcesLoader:
    @classmethod
    def loadAllResources(cls):

        cls.messageImg = getImgRes("message")
        cls.gameoverImg = getImgRes("gameover")

        cls.backgroundImg = {}
        cls.backgroundImg["day"] = getImgRes("background-day")
        cls.backgroundImg["night"] = getImgRes("background-night")
        cls.baseImg = getImgRes("base")

        cls.birdImg = {}
        cls.birdImg["red"] = (getImgRes("redbird-downflap"), getImgRes("redbird-midflap"), getImgRes("redbird-upflap"))
        cls.birdImg["blue"] = (getImgRes("bluebird-downflap"), getImgRes("bluebird-midflap"), getImgRes("bluebird-upflap"))
        cls.birdImg["yellow"] = (getImgRes("yellowbird-downflap"), getImgRes("yellowbird-midflap"), getImgRes("yellowbird-upflap"))

        cls.pipeImg = {}
        cls.pipeImg["red"] = getImgRes("pipe-red")
        cls.pipeImg["green"] = getImgRes("pipe-green")

        cls.numImg = {}
        for i in range(10):
            cls.numImg[i] = getImgRes(str(i))

        cls.dieAud = getAudRes(audPath["die"])
        cls.hitAud = getAudRes(audPath["hit"])
        cls.pointAud = getAudRes(audPath["point"])
        cls.wingAud = getAudRes(audPath["wing"])
