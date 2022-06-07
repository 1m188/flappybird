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
     * 资源加载数目
     */
    static num = 0;

    /**
     * 0-9的数字，应是一个数组存储
     */
    static numbers = new Array();

    /**
     * 白天背景
     */
    static background_day = new Image();

    /**
     * 黑夜背景
     */
    static background_night = new Image();

    /**
     * 地面
     */
    static base = new Image();

    /**
     * 游戏结束标志
     */
    static gameover = new Image();

    /**
     * 游戏开始信息
     */
    static message = new Image();

    /**
     * 水管-绿色
     */
    static pipe_green = new Image();

    /**
     * 水管-红色
     */
    static pipe_red = new Image();

    /**
     * 蓝鸟-翅膀向下
     */
    static bluebird_downflap = new Image();

    /**
     * 蓝鸟-翅膀向中
     */
    static bluebird_midflap = new Image();

    /**
     * 蓝鸟-翅膀向上
     */
    static bluebird_upflap = new Image();

    /**
     * 红鸟-翅膀向下
     */
    static redbird_downflap = new Image();

    /**
     * 红鸟-翅膀向中
     */
    static redbird_midflap = new Image();

    /**
     * 红鸟-翅膀向上
     */
    static redbird_upflap = new Image();

    /**
     * 黄鸟-翅膀向下
     */
    static yellowbird_downflap = new Image();

    /**
     * 黄鸟-翅膀向中
     */
    static yellowbird_midflap = new Image();

    /**
     * 黄鸟-翅膀向上
     */
    static yellowbird_upflap = new Image();

    /**
     * 加载所有图片资源
     */
    static load() {
        if (Res_img.numbers.length != 0) return;

        for (let i = 0; i <= 9; i++) {
            let img = new Image();
            img.src = "../asset/image/" + String(i) + ".png";
            img.onload = function () { Res_img.num++; }
            Res_img.numbers.push(img);
        }

        Res_img.background_day.src = "../asset/image/background-day.png"
        Res_img.background_day.onload = function () { Res_img.num++ };

        Res_img.background_night.src = "../asset/image/background-night.png"
        Res_img.background_night.onload = function () { Res_img.num++ };

        Res_img.base.src = "../asset/image/base.png"
        Res_img.base.onload = function () { Res_img.num++ };

        Res_img.gameover.src = "../asset/image/gameover.png"
        Res_img.gameover.onload = function () { Res_img.num++ };

        Res_img.message.src = "../asset/image/message.png"
        Res_img.message.onload = function () { Res_img.num++ };

        Res_img.pipe_green.src = "../asset/image/pipe-green.png"
        Res_img.pipe_green.onload = function () { Res_img.num++ };

        Res_img.pipe_red.src = "../asset/image/pipe-red.png"
        Res_img.pipe_red.onload = function () { Res_img.num++ };

        Res_img.bluebird_downflap.src = "../asset/image/bluebird-downflap.png"
        Res_img.bluebird_downflap.onload = function () { Res_img.num++ };

        Res_img.bluebird_midflap.src = "../asset/image/bluebird-midflap.png"
        Res_img.bluebird_midflap.onload = function () { Res_img.num++ };

        Res_img.bluebird_upflap.src = "../asset/image/bluebird-upflap.png"
        Res_img.bluebird_upflap.onload = function () { Res_img.num++ };

        Res_img.redbird_downflap.src = "../asset/image/redbird-downflap.png"
        Res_img.redbird_downflap.onload = function () { Res_img.num++ };

        Res_img.redbird_midflap.src = "../asset/image/redbird-midflap.png"
        Res_img.redbird_midflap.onload = function () { Res_img.num++ };

        Res_img.redbird_upflap.src = "../asset/image/redbird-upflap.png"
        Res_img.redbird_upflap.onload = function () { Res_img.num++ };

        Res_img.yellowbird_downflap.src = "../asset/image/yellowbird-downflap.png"
        Res_img.yellowbird_downflap.onload = function () { Res_img.num++ };

        Res_img.yellowbird_midflap.src = "../asset/image/yellowbird-midflap.png"
        Res_img.yellowbird_midflap.onload = function () { Res_img.num++ };

        Res_img.yellowbird_upflap.src = "../asset/image/yellowbird-upflap.png"
        Res_img.yellowbird_upflap.onload = function () { Res_img.num++ };
    }

    static is_ready() {
        return Res_img.num == 26;
    }
};

Res_img.load();

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