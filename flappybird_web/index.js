let canvas = document.getElementById("main-window");
let ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

/**
 * 设置
 */
class Config {

    /**
     * 帧数
     */
    static FPS = 60;

    /**
     * 每帧的更新时间
     */
    static frameUpdateTime = 1000 / this.FPS;

    /**
     * 背景在每帧中移动的距离
     */
    static background_dx = 0.5;
};

/**
 * 图片资源
 */
class Res_img {

    /**
     * 0-9的数字，应是一个数组存储
     */
    static numbers = null;

    /**
     * 白天背景
     */
    static background_day = null;

    /**
     * 黑夜背景
     */
    static background_night = null;

    /**
     * 地面
     */
    static base = null;

    /**
     * 游戏结束标志
     */
    static gameover = null;

    /**
     * 游戏开始信息
     */
    static message = null;

    /**
     * 水管-绿色
     */
    static pipe_green = null;

    /**
     * 水管-红色
     */
    static pipe_red = null;

    /**
     * 蓝鸟-翅膀向下
     */
    static bluebird_downflap = null;

    /**
     * 蓝鸟-翅膀向中
     */
    static bluebird_midflap = null;

    /**
     * 蓝鸟-翅膀向上
     */
    static bluebird_upflap = null;

    /**
     * 红鸟-翅膀向下
     */
    static redbird_downflap = null;

    /**
     * 红鸟-翅膀向中
     */
    static redbird_midflap = null;

    /**
     * 红鸟-翅膀向上
     */
    static redbird_upflap = null;

    /**
     * 黄鸟-翅膀向下
     */
    static yellowbird_downflap = null;

    /**
     * 黄鸟-翅膀向中
     */
    static yellowbird_midflap = null;

    /**
     * 黄鸟-翅膀向上
     */
    static yellowbird_upflap = null;
};


let img = new Image();
img.src = "../asset/image/background-day.png";
img.onload = function () {

    let arr = new Array();

    let num = (Math.floor(canvas.width / img.width) + 1) * 2;
    for (let i = 0; i < num; i++) {
        arr.push(i * img.width);
    }

    setInterval(() => {

        for (let i = 0; i < arr.length; i++) {
            ctx.drawImage(img, arr[i], 0, img.width, canvas.height);
            arr[i] -= Config.background_dx;
        }
        if (arr[0] <= -img.width) {
            for (let i = 0; i < arr.length; i++) {
                arr[i] += img.width;
            }
        }

    }, Config.frameUpdateTime);
};