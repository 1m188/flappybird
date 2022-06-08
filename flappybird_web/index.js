const canvas = document.getElementsByTagName("canvas")[0];
const ctx = canvas.getContext("2d");

canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

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
    static load(afterload) {
        if (Res_img.numbers.length != 0) return; // 已经加载完了就不必再加载了

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

        let timer = setInterval(function () {
            if (!Res_img.is_ready()) return;
            clearInterval(timer);
            afterload();
        }, 10);
    }

    static is_ready() {
        return Res_img.num == 26;
    }
};

/**
 * 精灵类
 */
class Sprite {
    constructor(img) {
        this.img = img;
        this.x = 0;
        this.y = 0;
        this.width = img.width;
        this.height = img.height;
    }

    draw() {
        ctx.drawImage(this.img, this.x, this.y, this.width, this.height);
    }

    before_draw() {
    }

    after_draw() {
    }

    run() {
        this.before_draw();
        this.draw();
        this.after_draw();
    }

    move(dx, dy) {
        this.x += dx;
        this.y += dy;
    }

    moveTo(x, y) {
        this.x = x;
        this.y = y;
    }
};

/**
 * 背景
 */
class Background extends Sprite {
    constructor(img) {
        super(img);
        this.width = canvas.height / this.height * this.width;
        this.height = canvas.height;
    }

    after_draw() {
        let end = this.x + this.width;
        while (end < canvas.width) {
            ctx.drawImage(this.img, end, 0, this.width, this.height);
            end += this.width;
        }

        this.move(-1, 0);

        if (this.x + this.width <= 0) {
            this.moveTo(0, 0);
        }
    }
};

Res_img.load(main);

function main() {

    let background_day = new Background(Res_img.background_day);

    setInterval(function () {

        ctx.clearRect(0, 0, canvas.width, canvas.height);

        background_day.run();

    }, 1000 / 60);
}