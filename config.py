# 这个文件记录一些配置，包括各种大小速度等的参数，以及各种资源的加载路径
# 需要注意的是这里所有的数字变量都是正值，因此如果要使用的话要结合实际的需要判定方向

# 帧率
FPS = 60

# 资源路径
resourcesPath = {}

# 某些信息
resourcesPath["message"] = "img/message.png"
resourcesPath["gameover"] = "img/gameover.png"

# 背景及下边界
for i in ("day", "night"):
    resourcesPath[f"background-{i}"] = f"img/background-{i}.png"
resourcesPath["base"] = "img/base.png"

# 几种颜色的鸟以及其各种形态
for i in ("red", "blue", "yellow"):
    resourcesPath[f"{i}bird-downflap"] = f"img/{i}bird-downflap.png"
    resourcesPath[f"{i}bird-midflap"] = f"img/{i}bird-midflap.png"
    resourcesPath[f"{i}bird-upflap"] = f"img/{i}bird-upflap.png"

# 水管
for i in ("green", "red"):
    resourcesPath[f"pipe-{i}"] = f"img/pipe-{i}.png"

# 数字
for i in range(10):
    resourcesPath[str(i)] = f"img/{str(i)}.png"

# 游戏窗口大小
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
